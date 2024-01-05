# PDF2Text Converter

[English Document](README-en.md)。

这个Python工具 `pdf2text.py` 能将PDF文档转换为纯文本格式，并处理单词和句子中的换行问题。该脚本也能读取其他类型的文件，但主要是为处理PDF文件而设计的。

### 特点
- 提取PDF及[Apache Tika](https://tika.apache.org/)支持的其他文档格式的文本内容。
- 利用[wordninja](https://github.com/keredson/wordninja/)纠正由连字符引起的单词换行问题（例如，"low- power" -> "low-power"，"im- plement" -> "implement"）。
- （可选）纠正PDF排版导致的句子换行问题。

### 安装
1. 克隆此仓库或下载源代码。
2. 确保安装有java环境并配置了正确的路径，可以执行`java`命令。
3. 运行下面的命令来安装所需的依赖项：
   ```
   pip install -r requirements.txt
   ```

### 用法
要将文件转换为文本，请使用`pdf2text`函数。

```python
from pdf2text import pdf2text

file_path = 'path_to_your_pdf_file.pdf'
with open(file_path, 'rb') as file:
    text_content = pdf2text(file, word_line_break=True, sentence_line_break=False)
    print(text_content)
```
