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
import sys

BOOK = ["example.pdf", "example2.pdf", "example.docx"] #input("Filename >") # file location
#example2.pdf pdf with encryption, passcode = PASSWORD

def document_t(document):
    if document.lower().endswith(".pdf"):
        return [document, "isPdf"]
    elif document.lower().endswith(".docx"):
        return [document, "isDocx"]
    else:
        print("Unsupported document type!")
        return None

def get_Text(listL):
    if  listL[1] == 'isPdf':
        return extract_Text_pdf(listL[0])
    else:
        return extract_Text_docx(listL[0])

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
        file_in = document_t(os.path.join("src", str(BOOK[2]))) #returns a file and its type
        if file_in is None:
            sys.exti(0)
        else:
            text = get_Text(file_in) #extracts text
            sayit(text) #text to speach
    except Exception as err:
        print(err)



if __name__ == "__main__":
    main()
