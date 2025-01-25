import os
from pdfminer.high_level import extract_text
import docx

def extract_text_from_file(file) -> str:
    """
    Extract text from an uploaded file.
    """
    if file.filename.endswith(".txt"):
        content = file.file.read().decode("utf-8")
    elif file.filename.endswith(".pdf"):
        with open(file.filename, "wb") as f:
            f.write(file.file.read())
        content = extract_text(file.filename)
        os.remove(file.filename)
    elif file.filename.endswith(".docx"):
        with open(file.filename, "wb") as f:
            f.write(file.file.read())
        doc = docx.Document(file.filename)
        content = "\n".join([para.text for para in doc.paragraphs])
        os.remove(file.filename)
    else:
        raise ValueError("Unsupported file type")

    if not content.strip():  # Check if the extracted text is empty
        raise ValueError("The uploaded file contains no readable text.")

    return content

