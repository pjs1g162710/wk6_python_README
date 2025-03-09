#install Inquirer
#pip install InquirerPy
from InquirerPy import prompt
from InquirerPy.utils import color_print
from InquirerPy import inquirer

#pip install rich
from rich import print as rprint
from rich.console import Console
from rich.text import Text

import tkinter
from tkinter import ttk, messagebox

#First use inquirerpy to ask the user whether they want to use GUI or terminal inputs

#def choose_input():
    #color_print([("class:aaa", "fooboo")], style={"aaa": "#000000"})
questions = [
{"type": "list",
"message": "Would you prefer to use GUI or terminal inputs?",
"choices": ["GUI", "Terminal"],
"name":"input"},
    
{"type": "confirm", "message": "Confirm?"},]
    
result = prompt(questions)
global firstq
firstq = result["input"]

#console = Console()
#text = Text.str(firstq)
#text.stylize("bold magenta", 0, 6)
#console.print(firstq)


 # when we know what choice is made, call one or other function

def recallinput():
    if firstq["input"] == 'GUI':
        import GUI_input
        GUI_input.gui_window()
                
    elif firstq["input"] == 'Terminal':
        import terminal_input
        terminal_input.terminal_enquiry()    
   
    else:
        messagebox.showinfo(
        title="Select user input method",
        message=f"Please select either 'GUI' or 'Terminal'")

# what we now need to do is to retrieve the input data from either file.

def file_handling():
##file handling to produce readme file
    fnew_input = str(firstq)

# create text file of input responses without formatting
    fnew = open("README2.md", "w")
    fnew.write(fnew_input)

    fnew.close()





#**Use `Rich`** to enhance the user experience with **colored text and structured output**.
#experimenting with Rich syntax
   


#justify (left, center, right or full)
#overflow (fold. crop, ellipsis)
#no_wrap ()
#tab size (sets number of char in tab)
