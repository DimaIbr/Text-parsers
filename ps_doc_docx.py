#pip install python-docx
import docx

path="pr.docx"
doc = docx.Document(path)
text = []
for paragraph in doc.paragraphs:
    text.append(paragraph.text)
print('\n'.join(text))