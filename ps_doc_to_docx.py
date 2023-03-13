import os.path
import win32com.client

file_path="C:/Users/Dima/PycharmProjects/ps_djvu/pr.doc"
docx_file=file_path+".docx"
word = win32com.client.Dispatch("Word.application")

wordDoc = word.Documents.Open(file_path, False, False, False)
wordDoc.SaveAs2(docx_file, FileFormat = 16)
wordDoc.Close()