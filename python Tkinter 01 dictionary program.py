from tkinter import *

window = Tk()

window.title("Dictionary Program")
window.geometry("1000x750")

def button_click1():
    typed_text= entry1.get()

    output_text.delete(0.0, END)
    meaning= my_dictionary[typed_text]

    output_text.insert(END, meaning)




output_text = Text(window, width=50, height=50, wrap=WORD, background="Light Blue")
output_text.grid(row=1, column=5, columnspan=7, sticky=E)
