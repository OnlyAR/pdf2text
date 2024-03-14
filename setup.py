import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirements = [
    "certifi",
    "charset-normalizer",
    "idna",
    "requests",
    "tika",
    "urllib3",
    "wordninja",
]

setuptools.setup(
    name="pdf2text",
    version="0.0.1",
    author="Only(AR)",
    author_email="zhangjh@outlook.com",
    description="A small package to extract text from pdf",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OnlyAR/pdf2text",
    include_package_data=False,
    requires=requirements,
    py_modules=['pdf2text'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
