from docx import Document


file_path = "words-list.docx"

def write_to_file(filename, data):
    """
    Writes a given string into a file.

    :param filename: Name of the file to write the data into.
    :param data: The data (string) to be written into the file.
    """
    with open(filename, 'w') as f:
        f.write(data)

def read_docx(file_path):
    """
    Reads a .docx file and extracts paragraphs that have length between 4 and 5 characters.

    :param file_path: Path to the .docx file.
    :return: A string consisting of selected paragraphs separated by newline characters.
    """
    # Initialize the Document object with the file path
    doc = Document(file_path)
    # Create a list of paragraphs that fulfill the character length criteria
    fullText = [para.text.strip() for para in doc.paragraphs if 3 < len(para.text.strip()) < 6]
    # Join the paragraphs into a single string separated by newlines
    return '\n'.join(fullText)

if __name__ == "__main__":

    selected_text = read_docx(file_path)

    write_to_file("extracted_text.txt", selected_text)