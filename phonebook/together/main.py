from tkinter import *
import phonenumbers
import json
from tkinter import messagebox


################################################################################################################################   
#   OTHER FUNCTIONS
################################################################################################################################   
def phone_validator(phone):
    try:
        phonenumbers.parse(phone)
        return True
    except phonenumbers.phonenumberutil.NumberParseException:
        return False


def name_validator(name, surname):
    return ((len(name) > 0) and (len(surname) > 0)) 
################################################################################################################################   



################################################################################################################################   
#   PHONEBOOK LIST
################################################################################################################################   
def show_book():

    d_label.config(text="")

    def Select_set() :
        contactlist.sort()
        select.delete(0,END)
        for name,phone in contactlist :
            select.insert (END, name)

    def VIEW():
        NAME, PHONE = contactlist[Selected()]
        infoo.config(text=NAME + " " + PHONE)
        selected_label.config(text='Selected: ')

    def Selected():
        if len(select.curselection()) == 0:
            selected_label.config(text='Select entity to view')
        else:
            return int(select.curselection()[0])
        
    def Delete_Entry():
        if len(select.curselection())!=0:
            result=messagebox.askyesno('Confirmation','You Want to Delete Contact\n Which you selected')
            if result==True:
                NAME, PHONE = contactlist[Selected()]
                del contactlist[Selected()]
                selected_label.config(text='Deleted: \n' + NAME + " " + PHONE)
                infoo.config(text='')
                Select_set()
        else:
            messagebox.showerror("Error", 'Please select the Contact')

    def close_list():
        json_data = {}
        with open(r"C:\Users\maciej.antosz\Desktop\priv\proj\phone_book\together\data.json", 'w', encoding='utf-8') as f:
            for contact in contactlist:
                json_data[contact[0]] = contact[1]
            json.dump(json_data, f, ensure_ascii=False, indent=4)
        list_window.destroy()

    ###
    ###     'list_window' window is top level window that contains list of contacts
    ###
    list_window = Toplevel()
    list_window.title("List of phone numbers") # window title
    list_window.geometry("500x500")

    # create frame
    frame = Frame(list_window)
    frame.pack(side = RIGHT)
    selected_label = Label(list_window, text = '')
    selected_label.place(x= 30, y=20)
    infoo = Label(list_window, text = '')
    infoo.place(x= 30, y=50)

    # adding scroll
    scroll = Scrollbar(frame, orient=VERTICAL)
    select = Listbox(frame, yscrollcommand=scroll.set,font=('Times new roman',16),bg="#f0fffc",width=20,height=20,borderwidth=3,relief="groove")
    scroll.config (command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT,  fill=BOTH, expand=1)
    Button(list_window,text="View", command = VIEW).place(x= 50, y=125)
    Button(list_window,text="Delete", command = Delete_Entry).place(x= 50, y=155)
    Button(list_window,text="Close", command = close_list).place(x= 50, y=185)

    with open(r"C:\Users\maciej.antosz\Desktop\priv\proj\phone_book\together\data.json", 'r', encoding='utf-8') as f:
        json_data = json.loads(f.read())
        contactlist = []
        for i in range(len(json_data.keys())):
            contactlist.append([list(json_data.keys())[i], list(json_data.values())[i]])

    for i in range(len(contactlist)):
        select.insert(1, contactlist[i][0])

    Select_set()

################################################################################################################################   



################################################################################################################################   
#   MAIN WINDOW
################################################################################################################################   
# action on first button clicked
def add_button_clicked():
    with open(r"C:\Users\maciej.antosz\Desktop\priv\proj\phone_book\together\data.json", 'r', encoding='utf-8') as f:
            json_data = json.loads(f.read())
            contactlist = []
            for i in range(len(json_data.keys())):
                contactlist.append([list(json_data.keys())[i], list(json_data.values())[i]])

    p, s, n = phone_entry.get(), surname_entry.get(), name_entry.get()

    if phone_validator(p) and name_validator(n, s):
        d_label.config(text="Added!")
        contactlist.append([n + " " + s, p])
        with open(r"C:\Users\maciej.antosz\Desktop\priv\proj\phone_book\together\data.json", 'w', encoding='utf-8') as f:
            for contact in contactlist:
                json_data[contact[0]] = contact[1]
            json.dump(json_data, f, ensure_ascii=False, indent=4)

        name_entry.delete(0, END)
        surname_entry.delete(0, END)
        phone_entry.delete(0, END)

    elif not name_validator(n, s):
        d_label.config(text="Insert name")
        
    elif not phone_validator(p):
        d_label.config(text="Incorrect \n phone number")


# action on close button
def close_window():
    main_window.destroy()


main_window = Tk()
main_window.title("Phone book") # window title
main_window.geometry("430x250")


main_window.grid_columnconfigure(0, minsize=10)
main_window.grid_columnconfigure(2, minsize=40)
main_window.grid_columnconfigure(4, minsize=10)
main_window.grid_rowconfigure(0, minsize=10)
main_window.grid_rowconfigure(2, minsize=30)
main_window.grid_rowconfigure(4, minsize=30)
main_window.grid_rowconfigure(6, minsize=30)


###
###     All buttons
###
add_button = Button(main_window, text = "App to phonebook" ,
             fg = "black", command=add_button_clicked)
add_button.grid(column=4, row=7)

close_button = Button(main_window, text='Close',
                      fg = "black", command=close_window)
close_button.grid(column=4,row=8)

show_book_button = Button(main_window, text='Phonebook',
                          fg="black", command=show_book)
show_book_button.grid(column=4,row=9)


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

d_label = Label(main_window, text='', fg='#FF0000')
d_label.grid(column=1 ,row=6)
################################################################################################################################   



################################################################################################################################   
# run
if __name__=="__main__":
    with open(r"C:\Users\maciej.antosz\Desktop\priv\proj\phone_book\together\data.json", 'r', encoding='utf-8') as f:
            json_data = json.loads(f.read())
            contactlist = []
            for i in range(len(json_data.keys())):
                contactlist.append([list(json_data.keys())[i], list(json_data.values())[i]])
    main_window.mainloop()

# when we put r before string it changes it to raw string