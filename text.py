from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('Texteditor')
root.geometry('1200x600')

# ** Create main frame
my_frame = Frame(root)
my_frame.pack(pady=6)

# * Create scrool bar
text_scrool = Scrollbar(my_frame)
text_scrool.pack(side=RIGHT, fill=Y )


# ** Create Text Box
my_text = Text(my_frame, width=98 , height=25, font=('Helvetica', 16), selectbackground='yellow', selectforeground='black', undo=True)
my_text.pack()

# * Configure scrool Bar
text_scrool.config(command=my_text.yview)
my_text.config(yscrollcommand=text_scrool.set)

# * Creat Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# ! Creat file menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New')
file_menu.add_command(label='Open')
file_menu.add_command(label='Save')
file_menu.add_command(label='Save as')
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)


# ! Creat Edit menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Create')
edit_menu.add_command(label='Copy')
edit_menu.add_command(label='Paste')
edit_menu.add_command(label='Cut')

# ! Status Bar
status_bar = Label(root, text='This', anchor=E)
status_bar.pack(side=BOTTOM, fill=X, ipady=5)


root.mainloop()

