from tkinter import *

window = Tk()

window.title("My FIrst GUI")

def button_click():
    typed_text = entry1.get()

    output_text.delete(0.0, END)
    manipulated_text = "You just typed: " + typed_text

    output_text.insert(END, manipulated_text)



label1 = Label(window, text="Enter something here: ")
label1.grid(row=0, column=0, sticky=W)
entry1 = Entry(window, width=20, bg="Light Green")
entry1.grid(row=1, column=0, sticky=E)


button1 = Button(window, text="SUBMIT", width=5, command=button_click)
button1.grid(row=2, column=0, sticky=W)



output_text = Text(window, width=30, height=10, wrap=WORD, background="Light Blue")
output_text.grid(row=3, column=0, columnspan=2, sticky=W)








window.mainloop()

