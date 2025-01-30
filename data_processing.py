import camelot
import pandas as pd
import fitz  # PyMuPDF
import re

def preprocess_pdf(pdf_path):
    """Preprocess the PDF by removing images."""
    doc = fitz.open(pdf_path)
    for page in doc:
        for image in page.get_images():
            page.delete_image(image)
    doc.save("preprocessed.pdf")

def extract_pnl_data(pdf_path):
    """Extracts tables from a PDF file and structures it into a DataFrame."""
    try:
        # Pre-process the PDF to remove images
        preprocess_pdf(pdf_path)
        preprocessed_path = "preprocessed.pdf"
        tables = camelot.read_pdf(preprocessed_path, flavor='stream', pages='all')

        all_data = []

        for table in tables:
            for row in table.df.values:
                text = ' '.join(str(cell) for cell in row)  # Concatenate cells
                
                # Use regex to match specific patterns:
                match = re.search(r'(.*?)\s+(\d[\d,.]*)\s+(\d[\d,.]*)\s+(\d[\d,.]*)\s+(\d[\d,.]*)', text)
                
                if match:
                    label = match.group(1).strip()
                    values = [match.group(i).strip().replace(',', '') for i in range(2, 6)]
                    all_data.append([label] + values)

        df = pd.DataFrame(all_data, columns=['Item'] + [f'Column_{i}' for i in range(4)])
        return df  # Return the extracted DataFrame

    except Exception as e:
        print(f"Error during extraction: {e}")
        return None  # Return None in case of error




