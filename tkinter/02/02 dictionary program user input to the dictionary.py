##Imports

from tkinter import *


window = Tk()

window.title("Dictionary Program")
window.geometry("1000x800")



# def button_click():                           ## Old code and doesnt support error handling.
#     typed_text= entry1.get()
# 
#     output_text.delete(0.0, END)
#     meaning= my_dictionary[typed_text]
# 
#     output_text.insert(END, meaning)



def button_click():
    typed_text= entrySearch.get()
    output_text.delete(0.0, END)
    
    try:
        meaning= my_dictionary[typed_text]
    except:
        meaning= "The word you entered could not be found"
        
    output_text.insert(END, meaning)



def add_word():

    global my_dictionary
    
    typed_word= entryWord.get()
    output_text.delete(0.0, END)
    
    typed_meaning= entryMeaning.get()
    my_dictionary[typed_word] = typed_meaning
    
    added= "Your word has been added to the dictionary!"
    output_text.insert(END, added)





my_dictionary= {"hello": "A common expression used to greet a person.",
                "goodbye": "A common expression used to express good wishes when parting or at the end of a conversation."}




output_text = Text(window, width=50, height=30, wrap=WORD, background="Dark Green")
output_text.place(x= 600, y= 100)




## Main Dictionary

labelSearch= Label(window, text= "Search the dictionary!")
labelSearch.place(x= 100, y= 75)

entrySearch= Entry(window, width= 20, bg= "Light Grey")
entrySearch.place(x= 100, y= 100)

buttonSearch = Button(window, text="Search...", width=13, command=button_click)
buttonSearch.place(x= 100, y= 150)




## Add to the dictionary


label2= Label(window, text= "Add to the dictionary!")
label2.place(x= 100, y= 225)


# Labels for entry boxes...
labelWord= Label(window, text= "Word: ")
labelWord.place(x= 30, y= 250)

labelMeaning= Label(window, text= "Meaning: ")
labelMeaning.place(x=30, y= 275)


#Entry Boxes
entryWord= Entry(window, width= 20, bg= "Light Grey")
entryWord.place(x= 100, y= 250)

entryMeaning= Entry(window, width= 20, bg= "Light Grey")
entryMeaning.place(x= 100, y= 275)


#Button
buttonAdd = Button(window, text="Add...", width=13, command=add_word)
buttonAdd.place(x= 100, y= 350)














mainloop()
