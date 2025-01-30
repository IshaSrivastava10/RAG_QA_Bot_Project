import streamlit as st
from data_processing import extract_pnl_data
from embedding_retrieval import create_faiss_index, query_faiss
import os

st.title("Financial QA Bot")

uploaded_file = st.file_uploader("Upload a P&L PDF", type="pdf")

if uploaded_file:
    st.write("Processing your file...")
    # Create the input_pdfs directory if it doesn't exist
    input_dir = 'input_pdfs'
    os.makedirs(input_dir, exist_ok=True)
    
    # Save the uploaded file
    file_path = os.path.join(input_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    # Extract and preprocess data
    df = extract_pnl_data(file_path)
    st.write("Extracted Data:")
    st.dataframe(df)

    if df is not None:
        # Convert data to a list of strings for embedding
        data_list = df.apply(lambda x: " ".join(x.dropna()), axis=1).tolist()
        index, _ = create_faiss_index(data_list)

        question = st.text_input("Ask a question about the financial data:")
        if question:
            answer = query_faiss(index, question, data_list)
            st.write("Answer:", answer)
    else:
        st.write("Extraction failed.")
