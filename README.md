# PDF2Text Converter

[中文文档](README-zh.md)

This Python utility, `pdf2text.py`, converts PDF documents into plain human-readable text format by processing line breaks in words and sentences. The script is capable of reading other file types too, but it's specially equipped to handle PDFs.

### Features
- Extracts text content from PDF and other document formats supported by [Apache Tika](https://tika.apache.org/).
- Corrects word breaks that occur due to hyphenation supported by [wordninja](https://github.com/keredson/wordninja/)(e.g., "low- power" -> "low-power", "im- plement" -> "implement").
- Optionally corrects sentence breaks that occur due to newline characters.

### Installation
1. Clone this repository or download the source code.
2. Make sure the java environment is installed and the correct path is configured to execute the `java` command.
3. Install the required dependencies by running:
   ```
   pip install -r requirements.txt
   ```

### Usage
To convert a file to text, use the `pdf2text` function.

```python
from pdf2text import pdf2text

file_path = 'path_to_your_pdf_file.pdf'
with open(file_path, 'rb') as file:
    text_content = pdf2text(file, word_line_break=True, sentence_line_break=False)
    print(text_content)
```

For further details and options, please refer to the Chinese .