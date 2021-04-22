from tkinter import *

window = Tk()

window.title("Flash Card Program")
window.geometry("1000x750")

def button_click1():
    text = "The CPU is responsible for all processes in the computer. \n\
The CPU is where processes such as calculating, sorting and searching take place. \n\
The CPU is made up of three main components, the control unit , the immediate access store and the arithmetic and logic unit ."

    output_text.delete(0.0, END)
    manipulated_text = text

    output_text.insert(END, manipulated_text)

def button_click2():
    text = "Memory is an internal component of all computer systems which stores short term, currently-needed files and data. \n\
Memory is volatile and is primary storage."

    output_text.delete(0.0, END)
    manipulated_text = text

    output_text.insert(END, manipulated_text)

def button_click3():
    text = "I/O is the abreviation of Input/Output and refers to the collection of peripherals or connected, \
external devices that may interact with the computer system, "

    output_text.delete(0.0, END)
    manipulated_text = text

    output_text.insert(END, manipulated_text)

def button_click4():
    text = "A computer's motherboard is the mainframew of the computer and allow the CPU or 'Central Processing Unit' to \n\
interact with the other peripherals (both external and internal) connected to the computer. \n\
The Motherboard helps the cpu to communicate with I/O, Primary and Secondary storage and other aspects while also providing sufficient \n\
power delivery to the CPU, GPU and such."

    output_text.delete(0.0, END)
    manipulated_text = text

    output_text.insert(END, manipulated_text)

def button_click5():
    text = "Storage devices are what are used to store data both for short term (primary storage) and long term (secondary storage) \n\
Storage devices in at least some form are downright REQUIRED for a computer system to function. \n\
Primary Storage includes RAM and Secondary Storage solutions include Optical, Flash and Magnetic storage."

    output_text.delete(0.0, END)
    manipulated_text = text

    output_text.insert(END, manipulated_text)

button1 = Button(window, text="The CPU", width=13, command=button_click1)
button1.grid(row=1, column=0, sticky=W)

button2 = Button(window, text="Memory", width=13, command=button_click2)
button2.grid(row=2, column=0, sticky=W)

button3 = Button(window, text="I/O", width=13, command=button_click3)
button3.grid(row=3, column=0, sticky=W)

button4 = Button(window, text="Motherboard", width=13, command=button_click4)
button4.grid(row=4, column=0, sticky=W)

button5 = Button(window, text="Storage Devices", width=13, command=button_click5)
button5.grid(row=5, column=0, sticky=W)



output_text = Text(window, width=50, height=50, wrap=WORD, background="Light Blue")
output_text.grid(row=1, column=5, columnspan=7, sticky=E)

