import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog
import speech_recognition as sr
from gtts import gTTS
import os
import pytesseract as tess
from PIL import Image


def speechToText():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            text_area.insert(tk.INSERT, "You said : {}".format(text))
        except:
            text_area.insert(tk.INSERT, "Sorry could not recognize what you said")


def imageToText():
    f = filedialog.askopenfilename(title='Choose a file', filetypes=[('image files', '.jpg'), ('image files', '.png')])
    tess.pytesseract.tesseract_cmd = r'C:\Users\Puneet Singh\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

    img = Image.open(f)
    text = tess.image_to_string(img)

    text_area.insert(tk.INSERT, text)


def textToAudio():
    mytext = text_area.get("1.0", tk.END)

    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("myaudio.mp3")
    os.system("myaudio.mp3")


def audioToText():
    f = filedialog.askopenfilename()
    r = sr.Recognizer()

    with sr.AudioFile(f) as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)

    try:
        text_area.insert(tk.INSERT, "Converted Audio Is : \n" + r.recognize_google(audio))
    except Exception as e:
        text_area.insert(tk.INSERT, "Sorry Try Again...")


o = Tk()
o.title("Convertor")
o.geometry("440x420")
o.minsize(440, 420)
o.maxsize(440, 420)
o.configure(bg='#060d3d')
o.title("Convertor")

title1 = Label(o, text="Convertor", font=("Comic Sans MS", 28, "bold"), fg='brown', bg="#0a0e2b", borderwidth=3,
               relief="groove").place(
    x=0, y=-2, relwidth=1, height=50)

title2 = Label(o, text="Processed Text", font=("Times New Roman", 20, "bold"), fg='brown', bg="#0a0e2b", borderwidth=3,
               relief="groove").place(
    x=0, y=88, relwidth=1, height=40)

text_area = scrolledtext.ScrolledText(o,
                                      wrap=WORD,
                                      width=40,
                                      height=10,
                                      font=("Times New Roman",
                                            15))
text_area.grid(column=0, pady=130, padx=10)

B1 = Button(o, text="Image To Text", command=imageToText, bg="orange", bd=4,
            activebackground="blue", activeforeground="red", relief="raised").place(x=20, y=55)
B2 = Button(o, text="Text To Audio", command=textToAudio, bg="orange", bd=4,
            activebackground="blue", activeforeground="red", relief="raised").place(x=180, y=55)
B3 = Button(o, text="Audio To Text", command=audioToText, bg="orange", bd=4,
            activebackground="blue", activeforeground="red", relief="raised").place(x=335, y=55)
B4 = Button(o, text="Speech To Text", command=speechToText, bg="orange", bd=8,
            activebackground="blue", activeforeground="red", relief="raised", font=0).place(x=135, y=365)

o.mainloop()
