
def extract_Text_pdf(book, passcode=None):
    import PyPDF2
    try:
        with open(book, "rb") as pdfFileObj:
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            if pdfReader.isEncrypted:
                try:
                    if passcode is None:
                        pdfReader.decrypt(str(input("Password>")))
                    else:
                        pdfReader.decrypt(str(passcode))
                except PyPDF2.utils.PdfReadError as e:
                    print(str(e))
            else:
                pass

            extracted_text = " "     #we'll append the extracted text here!

            for a_pageNum in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(a_pageNum)
                extracted_text += pageObj.extractText()
            return extracted_text

    except Exception as err:
        print(str(err))

def extract_Text_docx(book):
    import docx as d
    doc = d.Document(book)
    extracted_text = []
    for a_paragraph in doc.paragraphs:
        extracted_text.append(a_paragraph.text)
    return '\n'.join(extracted_text)
