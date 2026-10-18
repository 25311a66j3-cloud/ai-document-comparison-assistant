
# AI Document Comparison Assistant

## Xpert Champs AI Engineering Internship

An AI-powered web application that compares two PDF documents using Google Gemini.

## Features

- Upload two PDF documents
- Extract PDF text using pypdf
- Generate separate document summaries
- Identify similarities and differences
- Compare important dates, names and requirements
- Generate an overall conclusion
- Download a DOCX comparison report

## Technologies

- Python
- Streamlit
- Google Gemini API
- pypdf
- python-dotenv
- python-docx

## Installation

1. Clone the repository.
2. Install dependencies:

   pip install -r requirements.txt

3. Create a .env file containing:

   GEMINI_API_KEY=your_api_key

4. Run the application:

   python -m streamlit run app.py

## Limitations

- Text-based PDFs are supported.
- Scanned PDFs may require OCR.
- Long documents are limited in the current version.
- AI-generated results should be verified against the source PDFs.

## Internship

Xpert Champs - AI Engineering Internship
