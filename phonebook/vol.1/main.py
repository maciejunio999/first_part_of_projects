from tkinter import *
import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type

def phone_validator(phone):
    try:
        phonenumbers.parse(phone)
        return True
    except phonenumbers.phonenumberutil.NumberParseException:
        return False

def name_validator(name, surname):
    return ((len(name) > 0) and (len(surname) > 0)) 

###
###     'main_window' window is top level window that contains everything alse and does not have a parent
###
main_window = Tk()
main_window.title("Phone book") # window title
main_window.geometry("430x260")


main_window.grid_columnconfigure(0, minsize=10)
main_window.grid_columnconfigure(2, minsize=40)
main_window.grid_columnconfigure(4, minsize=10)
main_window.grid_rowconfigure(0, minsize=10)
main_window.grid_rowconfigure(2, minsize=30)
main_window.grid_rowconfigure(4, minsize=30)
main_window.grid_rowconfigure(6, minsize=30)


# action on first button clicked
def add_button_clicked():
    p, s, n = phone_entry.get(), surname_entry.get(), name_entry.get()
    if phone_validator(p) and name_validator(n, s):
        main_window.geometry("430x260")
        info_label.config(text="Added: " + n + "\n" + p)
    else:
        info_label.config(text="not good")


# action on close button
def close_window():
    main_window.destroy()

###
###     All buttons
###
add_button = Button(main_window, text = "App to phonebook" ,
             fg = "black", command=add_button_clicked)
add_button.grid(column=4, row=7)

close_button = Button(main_window, text='Close',
                      fg = "black", command=close_window)
close_button.grid(column=4,row=8)


###
###     All entries
###
name_entry = Entry(main_window, width=25)
name_entry.grid(column=3, row=1)

surname_entry = Entry(main_window, width=25)
surname_entry.grid(column=3, row=3)

phone_entry = Entry(main_window, width=25)
phone_entry.grid(column=3, row=5)


###
###     All lables
###
name_label = Label(main_window, text='Name: ')
name_label.grid(column=1 ,row=1)

surname_label = Label(main_window, text='Surname: ')
surname_label.grid(column=1 ,row=3)

phone_label = Label(main_window, text='Phone number: ')
phone_label.grid(column=1 ,row=5)

info_label = Label(main_window, text='')
info_label.grid(column=1 ,row=10)


# run
if __name__=="__main__":
    main_window.mainloop()
