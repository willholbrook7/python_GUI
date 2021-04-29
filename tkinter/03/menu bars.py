from tkinter import *
import time

window = Tk()

window.title("Menu Bars")
window.geometry("500x500")


def function1():
    textarea.delete(0.0, END)
    textarea.insert(END, "You have selected menu option ONE.")

def function2():
    textarea.delete(0.0, END)
    textarea.insert(END, "You have selected menu option TWO.")


def quitapp():
    textarea.delete(0.0, END)
    textarea.insert(END, "Quitting application...")

    quit_window = Tk()

    quit_window.title("Quit?")
    quit_window.geometry("250x125")

    labelquit= Label(quit_window, text= "Are you sure you want to quit?")
    labelquit.place(x= 20, y= 20)

    buttonquitYes = Button(quit_window, text="Yes", width=5, command=quitappYes)
    buttonquitYes.place(x= 75, y= 75)

    buttonquitNo = Button(quit_window, text="No", width=5, command=quitappNo)
    buttonquitNo.place(x= 125, y= 75)

    mainloop()



#definitions for quit window

def quitappYes():




def quitappNo():




#menu bar

menubar = Menu(window)


firstmenu = Menu(menubar, tearoff=0)
firstmenu.add_command(label="Test", command=function1)
firstmenu.add_command(label="Quit Application", command=quitapp)
menubar.add_cascade(label="Menu1", menu=firstmenu)


secondmenu = Menu(menubar, tearoff=0)
secondmenu.add_command(label="Test", command=function2)
secondmenu.add_command(label="Quit Application", command=quitapp)
menubar.add_cascade(label="Menu2", menu=secondmenu)


window.config(menu=menubar)


#text box

textarea = Text(window, width=35, height=10, wrap=WORD, bg="lightblue")
textarea.place(x= 125, y= 175)








#main loop called

mainloop()
