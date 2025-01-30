# RAG QA Bot for Financial Data

## Overview
This project demonstrates a Retrieval-Augmented Generation (RAG) model for answering questions about financial data extracted from Profit & Loss (P&L) tables in PDFs.

## Model Architecture
The RAG model combines retrieval-based and generation-based techniques. The FAISS index is used for efficient retrieval, and Sentence Transformers are used for embedding financial terms.

## Data Extraction and Preprocessing
We use `camelot` and `pandas` to extract and preprocess financial data from PDFs. The data is structured into DataFrames for further processing.

## Generative Responses
The QA bot generates responses using pre-trained models from Sentence Transformers and leverages FAISS for efficient retrieval.

## Installation
To run the project locally, follow these steps:

1. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux

# Install the required libraries:

pip install camelot-py[cv] pandas sentence-transformers faiss-cpu pymupdf streamlit
Run the Streamlit app:

streamlit run app.py
# Usage
Upload PDF files containing P&L tables.

Ask financial questions and view the answers provided by the QA bot.

# Example Queries and Outputs
1. "What is the gross profit for Q3 2024?"

Response: The gross profit for Q3 2024 is ₹12,000 crore.

2. "How do the net income and operating expenses compare for Q1 2024?"

Response: The net income for Q1 2024 is ₹24,108 crore, and the operating expenses are ₹8,000 crore.

3. "What are the total expenses for Q2 2023?"

Response: The total expenses for Q2 2023 are ₹15,000 crore.

4. "Show the operating margin for the past 6 months."

Response: The operating margin for the past 6 months is 25%.

# Challenges and Solutions
Text Extraction: Some PDFs had non-searchable text. We used camelot to extract tables accurately.

Embedding Large Data: Efficient embedding of large datasets using Sentence Transformers and managing memory with FAISS.

# Conclusion
This project demonstrates the effective use of a RAG model to answer questions about financial data from P&L tables in PDFs. The interactive Streamlit app allows users to easily upload PDFs and query the financial data.

# Acknowledgements
Thank you for using this QA bot! If you have any questions or feedback, feel free to reach out.

