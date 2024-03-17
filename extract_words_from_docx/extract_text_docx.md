# Extract Text from DOCX

This Python script facilitates reading a Word document (`.docx` file) to extract and then save specific paragraphs to a text file. It specifically focuses on paragraphs that have a length of between 4 and 5 characters, demonstrating a basic form of content filtering based on character count.

## Features

- **Read DOCX**: Efficiently read Word documents (`.docx` files).
- **Filter Content**: Extract paragraphs based on their character length.
- **Write to File**: Export the filtered content into a plain text file.

## Prerequisites

Before you begin, ensure you have installed the required Python version (3.x) and the `python-docx` library, which can be installed using pip:

```bash
pip install python-docx
```

## Getting Started

1. **Clone this repository** or download the Python script directly.
2. Place the `.docx` file you intend to process in the same directory as the script or modify the `file_path` variable to point to its location.
3. Run the script with Python:

```bash
python name_of_script.py
```

Replace `name_of_script.py` with the actual name of the Python script file.

## Usage

The script is straightforward to use. Modify the `file_path` variable in the script to point to the `.docx` file you wish to extract paragraphs from. By default, it searches for paragraphs with a character length between 4 and 5 but you can customize this range as needed within the `read_docx` function.

```python
# Example modification for different character lengths
fullText = [para.text.strip() for para in doc.paragraphs if X < len(para.text.strip()) < Y]
```

Replace `X` and `Y` with the desired minimum and maximum character lengths, respectively.
