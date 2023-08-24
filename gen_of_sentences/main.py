from wonderwords import RandomWord, Defaults
from tkinter import *

# configuration of generator
persons = ["I", "You", "He", "She", "It", "We", "You", "They"]
generator = RandomWord(
    who=persons,
    verb=Defaults.VERBS,
    noun=Defaults.NOUNS
)


# 'root' window is top level window that contains everything alse and does not have a parent
root = Tk()
root.title("Sentence generator") # window title
root.geometry('500x250') # windows size


# configure grid sizes and arounds
root.grid_columnconfigure(0, minsize=10)
root.grid_columnconfigure(2, minsize=40)
root.grid_columnconfigure(4, minsize=40)
root.grid_rowconfigure(0, minsize=10)
root.grid_rowconfigure(2, minsize=40)
root.grid_rowconfigure(4, minsize=40)


# action on generate button clicked
def generate_clicked():
    person = generator.word(include_categories=["who"])
    verb = generator.word(include_categories=["verb"])
    noun = generator.word(include_categories=["noun"])
    name = name_entry.get()
    name_entry["state"] = DISABLED
    if len(name) <= 0:
        try:
            if ["He", "She", "It"].index(person) > 0:
                if verb.endswith("s"):
                    verb = verb + "es"
                else:
                    verb = verb + "s"
        except ValueError:
            pass
    else:
        person = name

    sentence = person + " " + verb + " " + noun + "."
    lable_sentence.configure(text=sentence)


# action on clicking Clear, so we clear our entry
def clear_name_clicked():
    name_entry["state"] = NORMAL
    name_entry.delete(0, END)
    name_entry["state"] = DISABLED


# actions on Name clicked, so we let user enter name
def name_clicked():
    name_entry["state"] = NORMAL


# action on close button
def close_window():
    root.destroy()


###
###     All buttons
###
generate_button = Button(root, text = "Generate" ,
             fg = "black", command=generate_clicked)
generate_button.grid(column=1, row=3)

name_button = Button(root, text = "Name" ,
             fg = "black", command=name_clicked)
name_button.grid(column=1, row=1)

clear_name_button = Button(root, text = "Clear Name" ,
             fg = "black", command=clear_name_clicked)
clear_name_button.grid(column=1, row=2)

close_button = Button(root, text='Close',
                      fg = "black", command=close_window)
close_button.grid(column=1,row=5)


# Name entry
name_entry = Entry(root, width=10, state=DISABLED)
name_entry.grid(column=3, row=1)


# lable to show generated sentence
lable_sentence = Label(root, text='')
lable_sentence.grid(column=5 ,row=1)


# run
if __name__=="__main__":
    root.mainloop()