from flask import Flask, request, render_template, redirect, url_for, session, flash
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)  # For session handling

# Azure Document Intelligence credentials
endpoint = os.getenv("AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT")
key = os.getenv("AZURE_DOCUMENT_INTELLIGENCE_API_KEY")

# Initialize the Document Analysis client
document_analysis_client = DocumentAnalysisClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)

@app.route('/')
def index():
    return render_template('index.html')

def format_table(table):
    formatted_table = []
    headers = [cell.content for cell in table.cells if cell.kind == "columnHeader"]
    for row in table.cells:
        if row.kind == "columnHeader":
            continue
        if row.row_index >= len(formatted_table):
            formatted_table.append({})
        formatted_table[row.row_index][headers[row.column_index]] = row.content
    return formatted_table

def safe_get_attribute(obj, attr, default="Not available"):
    return getattr(obj, attr, default)

@app.route('/analyze', methods=['POST'])
def analyze_document():
    if 'file' not in request.files:
        flash("No file part", "error")
        return redirect(url_for('index'))
    
    file = request.files['file']
    
    if file.filename == '':
        flash("No selected file", "error")
        return redirect(url_for('index'))
    
    if file:
        try:
            # Read the file content
            file_content = file.read()
            
            # Analyze the document
            poller = document_analysis_client.begin_analyze_document(
                "prebuilt-document", file_content
            )
            result = poller.result()
            
            # Process the results
            formatted_result = {
                "Document Summary": {
                    "Page Count": len(result.pages),
                    "Language": safe_get_attribute(result, 'locale', 'Not specified'),
                    "Content Type": safe_get_attribute(result, 'content_type'),
                    "Pages": len(result.pages)
                },
                "Key-Value Pairs": {kv.key.content: kv.value.content for kv in result.key_value_pairs},
                "Tables": [format_table(table) for table in result.tables],
                "Paragraphs": [para.content for para in result.paragraphs]
            }
            
            # Add document type if available
            doc_type = safe_get_attribute(result, 'document_type', None)
            if doc_type:
                formatted_result["Document Summary"]["Document Type"] = doc_type
            
            # Store the result in session
            session['analysis_result'] = formatted_result
            
            return redirect(url_for('result'))
        
        except Exception as e:
            app.logger.error(f"Error during document analysis: {str(e)}")
            flash(f"An error occurred during analysis: {str(e)}", "error")
            return redirect(url_for('index'))

@app.route('/result')
def result():
    analysis_result = session.get('analysis_result', None)
    if analysis_result is None:
        flash("No analysis result found. Please analyze a document first.", "warning")
        return redirect(url_for('index'))
    return render_template('result.html', data=analysis_result)

if __name__ == '__main__':
    app.run(debug=True)