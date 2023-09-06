from tkinter import *
from tkinter import messagebox
import phonenumbers

# phone validator
def phone_validator(phone):
    try:
        phonenumbers.parse(phone)
        return True
    except phonenumbers.phonenumberutil.NumberParseException:
        return False


# initializing window
root = Tk()
root.title("Phone book") # window title
root.geometry("700x550")
root.config(bg = '#d3f3f5')
root.resizable(0,0)

# basic list of contacts
contactlist = [['Alicja Antosz', '123456789'], ['Maciej Antosz', '234567890'], ['Lena Antosz', '901234567']]


Name = StringVar()
Number = StringVar()

# create frame
frame = Frame(root)
frame.pack(side = RIGHT)

# adding scroll
scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set,font=('Times new roman',16),bg="#f0fffc",width=20,height=20,borderwidth=3,relief="groove")
scroll.config (command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT,  fill=BOTH, expand=1)


# function to get select value, on click in book
def Selected():
	if len(select.curselection()) == 0:
		messagebox.showerror("Error", "Please Select the Name")
	else:
		return int(select.curselection()[0])


# function to add new contact
def AddContact():
    if (Name.get()!="" and Number.get()!=""):
        if phone_validator(Number.get()):
            contactlist.append([Name.get() ,Number.get()])
            print(contactlist)
            Select_set()
            EntryReset()
            messagebox.showinfo("Confirmation", "Successfully Add New Contact")
        else:
            messagebox.showerror("Error","Enter correct phone number")
    else:
        messagebox.showerror("Error","Please fill the information")


# editing existing contact
def UpdateDetail():
	if Name.get() and Number.get():
		contactlist[Selected()] = [Name.get(), Number.get()]
                
		messagebox.showinfo("Confirmation", "Successfully Update Contact")
		EntryReset()
		Select_set()

	elif not(Name.get()) and not(Number.get()) and not(len(select.curselection())==0):
		messagebox.showerror("Error", "Please fill the information")

	else:
		if len(select.curselection())==0:
			messagebox.showerror("Error", "Please Select the Name and \n press Load button")
		else:
			message1 = """To Load the all information of \n 
						  selected row press Load button\n.
						  """   
			messagebox.showerror("Error", message1)


# function to clear entries in window
def EntryReset():
	Name.set('')
	Number.set('')


# deleteing selected contact
def Delete_Entry():
    if len(select.curselection())!=0:
        result=messagebox.askyesno('Confirmation','You Want to Delete Contact\n Which you selected')
        if result==True:
            del contactlist[Selected()]
            EntryReset()
            Select_set()
    else:
        messagebox.showerror("Error", 'Please select the Contact')

   
# view selected contact
def VIEW():
    NAME, PHONE = contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)
        

# exiting window  
def EXIT():
    root.destroy()


def Select_set() :
    contactlist.sort()
    select.delete(0,END)
    for name,phone in contactlist :
        select.insert (END, name)
Select_set()


# Name label and entry
Label(root, text = 'Name', font=("Times new roman",25,"bold"), bg = 'SlateGray3').place(x= 30, y=20)
Entry(root, textvariable = Name, width=30).place(x= 200, y=30)

#Phone number lables and entry
Label(root, text = 'Phone nr', font=("Times new roman",22,"bold"),bg = 'SlateGray3').place(x= 30, y=70)
Entry(root, textvariable = Number, width=30).place(x= 200, y=80)

###
###     All buttons
###
Button(root,text=" ADD", font='Helvetica 18 bold',bg='#e8c1c7', command = AddContact, padx=20). place(x= 50, y=140)
Button(root,text="EDIT", font='Helvetica 18 bold',bg='#e8c1c7',command = UpdateDetail, padx=20).place(x= 50, y=200)
Button(root,text="DELETE", font='Helvetica 18 bold',bg='#e8c1c7',command = Delete_Entry, padx=20).place(x= 50, y=260)
Button(root,text="VIEW", font='Helvetica 18 bold',bg='#e8c1c7', command = VIEW).place(x= 50, y=325)
Button(root,text="RESET", font='Helvetica 18 bold',bg='#e8c1c7', command = EntryReset).place(x= 50, y=390)
Button(root,text="EXIT", font='Helvetica 24 bold',bg='tomato', command = EXIT).place(x= 250, y=470)


# run
if __name__=="__main__":
    root.mainloop()
  

