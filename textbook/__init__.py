"""Read and vectorize the textbook for this course."""
from unstructured.partition.pdf import partition_pdf

from pathlib import Path


def _convert(file_path: str) -> str:
    """Convert a PDF file to text. Assumes text-readable PDF."""
    elements = partition_pdf(file_path)

    text: str = ""
    for element in elements:
        text += " " + element.text

    return text


def read_textbook(path: Path = Path.cwd() / "textbook.pdf") -> str:
    """Read the textbook and return it as a string."""
    return _convert(str(path.absolute()))
