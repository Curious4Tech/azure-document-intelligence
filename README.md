# Azure Document Intelligence Web App

## Overview

This is a Flask-based web application that utilizes **Azure Document Intelligence** to perform automated document analysis, extract data, and provide insights from various document types such as invoices, receipts, and forms. The app integrates with the **Azure AI Services** to enhance document processing with AI-powered capabilities.

## Features

- **Document Upload**: Users can upload documents in various formats (PDF, JPG, PNG, etc.).
- **Data Extraction**: The app uses Azure Document Intelligence to extract key information like text, tables, and key-value pairs from the uploaded documents.
- **Data Presentation**: Extracted data is displayed in a user-friendly format within the app for review and download.
- **Scalable AI**: The application leverages Azure's AI models for powerful and accurate document analysis.
  
## Technologies Used

- **Flask (Python)**: Web framework used to build the web app.
- **Azure Document Intelligence API**: Azure's AI service used for document processing and extraction.
- **HTML, CSS,**: Front-end for user interface design and document interaction.

## Setup and Installation

### Prerequisites

- Python 3.x installed on your machine.
- Azure subscription and an Azure Document Intelligence resource set up.

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Curious4Tech/azure-document-intelligence.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd azure-document-intelligence
   ```

 3. **Install required dependencies**
       ```bash
          pip install -r requirements.txt
       ```
 4. **Set up Azure Credentials**:
   - Create a `.env` file in the root directory.
   - Add your Azure Document Intelligence API key and endpoint to the `.env` file:
     ```bash
     AZURE_DOCUMENT_INTELLIGENCE_KEY=your-api-key
     AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT=your-document-intelligent-endpoint
     ```

5. **Run the Flask App**:
   ```bash
   python app.py
   ```

6. **Access the Application**:
   Open your web browser and navigate to `http://127.0.0.1:5000` to start using the app.

## Usage

1. Upload a document using the upload form.
2. The app will process the document and extract data using Azure Document Intelligence.
3. Review and download the extracted data in JSON or other formats.

## Project Structure

```
|-- azure-document-intelligence
    |-- app.py                   # Main Flask application
    |-- templates/
         |---index.html          # HTML templates for the web pages
    |-- requirements.txt         # Python dependencies
    |-- README.md                # Project documentation (this file)
    |---.env                     # file that containts your document intelligence credentials
```

## Azure Document Intelligence Integration

To integrate with Azure Document Intelligence, the following Python SDKs are used:

- [Azure Form Recognizer SDK](https://learn.microsoft.com/en-us/azure/cognitive-services/form-recognizer/overview)
  
The app uses the Form Recognizer client to send documents for analysis and receive structured data in return.

## Contributing

Contributions are welcome! If you would like to contribute to this project, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
