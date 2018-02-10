#! python3
"""
#####################################################
#          (c) 2018 Maroko Gideon                   #
#               www.gmaroko.me                      #
#           marokogideon@gmail.com                  #
#        ============================               #
#   get_Text([]) : extracts text from 'book'        #
#   sayit(text) : reads the extracted_text          #
#####################################################
"""
from get import *
import os.path

BOOK = ["example.pdf", "example2.pdf", "example.docx"] #input("Filename >") # file location
#example2.pdf pdf with encryption, passcode = PASSWORD

def document_type(document):
    if document.lower().endswith(".pdf"):
        return [document, "isPdf"]
    elif document.lower().endswith(".docx"):
        return [document, "isDocx"]
    else:
        print("Unsupported document type!")

def get_Text(listL):
    if  listL[1] == 'isPdf':
        return extract_Text_pdf(list[0])
    else:
        return extract_Text_docx(list[0])

def sayit(text):
    v = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0" #windows
    if text is not None:
        from pyttsx3 import init
        engine = init()
        engine.setProperty('rate', 140)
        engine.setProperty('voice', v)
        engine.say(text)
        engine.runAndWait()
    else:
        pass


def main():
    try:
        fileinfo = document_type(BOOK[2])
        text = get_Text(fileinfo)
        sayit(text)
    except Exception as err:
        print(err)



if __name__ == "__main__":
    main()
