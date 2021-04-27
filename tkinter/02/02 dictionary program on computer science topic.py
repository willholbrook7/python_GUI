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
        meaning= my_dictionary[typed_text.lower()]## the .lower() additionb allows the program to only interpret input
                                                  ## as lower case in order to correctly function with the dictionary
    except:
        meaning= "The word you entered could not be found"
    output_text.insert(END, meaning)    




my_dictionary= {"motherboard": "The Motherboard resides within a computer and ",
                "ram": "RAM stands for Random Access Memory and refers to the volatile primary storage that resides internally connected to the motherboard through the use of channel assigned physical slots. RAM varies in both speed and size and even some versions tailor to different environments such as 'Non ECC' for desktop us and 'ECC' for server use.",
                "power supply": "The power supply can come in different form factords as well as different efficiencies and different power capabilities. It provides power to literally all aspects of the computer in which it is installed.",
                "ssd": "An SSD is a solid state storage drive that sotres data with the ability for super fast access and write speeds. They provide a less demanding, higher speed alternative to the Hard Disk Drive or 'HDD'.",
                "hdd": "A HDD is a Hard Disk Drive which is a mechanically designed storage drive designed for high capacities and frequent read and writes in comparison to SSD drives.",
                "case": "The case is the enclosure in which almost all computers are stored, parts such as the motherboard including its CPU,the PSU, the GPU, the Storage drive(s) and other internal components."}



entry1= Entry(window, width= 20, bg= "Light Grey")
entry1.grid(row= 2, column= 0, sticky= E)

button1 = Button(window, text="Search", width=13, command=button_click)
button1.grid(row=3, column=0, sticky=W)

output_text = Text(window, width=50, height=20, wrap=WORD, background="Light Green")
output_text.grid(row=2, column=3, columnspan=5, rowspan=4, sticky=E)


mainloop()
