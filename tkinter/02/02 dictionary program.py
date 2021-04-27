from tkinter import *

window = Tk()

window.title("Dictionary Program")
window.geometry("1000x750")

# def button_click():                           ## Old code and doesnt support error handling.
#     typed_text= entry1.get()
# 
#     output_text.delete(0.0, END)
#     meaning= my_dictionary[typed_text]
# 
#     output_text.insert(END, meaning)



def button_click():
    typed_text= entry1.get()
    output_text.delete(0.0, END)
    try:
        meaning= my_dictionary[typed_text]
    except:
        meaning= "The word you entered could not be found"
    output_text.insert(END, meaning)    




my_dictionary= {"hello": "A common expression used to greet a person.",
                "goodbye": "A common expression used to express good wishes when parting or at the end of a conversation."}



entry1= Entry(window, width= 20, bg= "Light Grey")
entry1.grid(row= 1, column= 0, sticky= E)

button1 = Button(window, text="Search", width=13, command=button_click)
button1.grid(row=3, column=0, sticky=W)

output_text = Text(window, width=50, height=50, wrap=WORD, background="Dark Green")
output_text.grid(row=1, column=5, columnspan=7, sticky=E)
