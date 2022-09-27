import pyttsx3
import PyPDF2
from tkinter import filedialog


book_string = ""

file = filedialog.askopenfile(mode='r')
print(file.name)

filename = file.name.split('/')[-1]
print(filename)

path = file.name.replace(filename, "")
print(path)

# Read the PDF file
pdfFileObj = open(file.name, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

page_no = int(pdfReader.numPages)

for num in range(page_no):
    pageObj = pdfReader.getPage(num)
    book_string += (pageObj.extractText())

pdfFileObj.close()

# Converting text-to-speech
engine = pyttsx3.init()
""" RATE"""
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)

"""VOLUME"""
volume = engine.getProperty('volume')
engine.setProperty('volume', 1.0)

"""VOICE"""
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.runAndWait()
engine.stop()

"""Saving Voice to a file"""
engine.save_to_file(book_string, f"{path}{filename[:-4]}.mp3")
engine.stop()

