import PyPDF2

file_obj = open("pdf_audio_reader_app/PyPDF2.pdf",  "rb")

pdf_file_reader = PyPDF2.PdfFileReader(file_obj)

extracted_text = ''

for pageNum in range(pdf_file_reader.numPages):
    pdf_page_obj = pdf_file_reader.getPage(pageNum)

    extracted_text += pdf_page_obj.extract_text()

file_obj.close()
print(extracted_text)
