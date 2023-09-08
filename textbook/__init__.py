"""Read and vectorize the textbook for this course."""
import PyPDF2

from pathlib import Path


def pdf_to_text(pdf_path, output_txt_path):
    # Open the PDF file in binary read mode
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(pdf_path)
        
        # Extract text from each page
        full_text = ""
        for page in pdf_reader.pages:
            full_text += page.extract_text()
        
    # Save the extracted text to the output text file
    with open(output_txt_path, 'w', encoding='utf-8') as output_file:
        output_file.write(full_text)


def read_textbook() -> str:
    """Read the textbook and return it as a string."""
    input_path = Path(__file__).parent.absolute() / "textbook.pdf"
    output_path = Path(__file__).parent.absolute() / "textbook.txt"
    return pdf_to_text(input_path, output_path)
