import re

import wordninja
from tika import parser


def _extract(file_buffer):
    """
    extract content from file bytes
    :param file_buffer:
    :return: plain text
    """
    doc = parser.from_buffer(file_buffer)
    return doc['content']


def _word_contact(word: str):
    """
    contact word with "- "
    example: "low- power" -> "low-power"
             "im- plement" -> "implement"
    :param word: word with "- "
    :return: processed word
    """
    comb = word.replace("- ", "")
    if len(wordninja.split(comb)) == 1:
        return comb
    return word.replace(" ", "")


def _process_line_break_words(article: str):
    pattern = re.compile(r'\b\w+-\s\w+\b')
    matches = pattern.findall(article)

    for match in matches:
        replacement = _word_contact(match)
        article = article.replace(match, replacement)
    return article


def _process_line_break_sentence(article):
    """
    process line break in sentence
    :param str article:
    :return: str
    """
    cn_characters = r"\u4e00-\u9fa5"
    en_characters = r"a-zA-Z0"
    digits = r"0-9"
    cn_punc = r"\u3000-\u303F\uFF01-\uFF0F\uFF1A-\uFF20\uFF3B-\uFF40\uFF5B-\uFF65"
    en_punc = r"!-/:-@[-`{-~"

    paragraph_end = r".?!。？！”"
    character_set = "[" + cn_characters + en_characters + cn_punc + en_punc + digits + "]"
    pattern = re.compile(character_set + '\n\n' + character_set)
    matches = pattern.findall(article)
    for match in matches:
        if match[0] in paragraph_end:
            continue
        replacement = match[0] + match[3]
        article = article.replace(match, replacement)
    return article


def pdf2text(file, word_line_break=True, sentence_line_break=False):
    """
    parse file bytes to human-readable text (.pdf, .doc, .docx, .xls, .xlsx, etc.)
    :param bytes file:
    :param bool word_line_break: process line break in word (e.g. low- power -> low-power)
    :param bool sentence_line_break: process line break in sentence (e.g. "我\n\n爱工作" -> "我爱工作")
    :return: str: plain text
    """
    article = _extract(file)
    article = re.sub(r'(?<!\n)\n(?!\n)', ' ', article)
    article = re.sub(r'\n{3,}', '\n\n', article)

    if word_line_break:
        article = _process_line_break_words(article)
    if sentence_line_break:
        article = _process_line_break_sentence(article)

    return article


def test():
    filename = "test-cn-doc.doc"
    with open('data/pdfs/{}'.format(filename), 'rb') as f:
        pdf = f.read()
    out_filename = ".".join(filename.split('.')[:-1]) + '.txt'
    with open('data/txts/{}'.format(out_filename), 'w', encoding='utf-8') as f:
        f.write(pdf2text(pdf))


if __name__ == '__main__':
    test()
