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
def initialq():
    questions = [
    {"type": "list",
    "message": "Would you prefer to use GUI or terminal inputs?",
    "choices": ["GUI", "Terminal"],
    "name":"input"},
    
    {"type": "confirm", "message": "Confirm?"},]

    result = prompt(questions)
    global methodinput
    methodinput =result["input"]
    
    console = Console()
    console.print(
            "[bold blue]User entered :[/bold blue]\n " +
            "[bold green]Input Choice: [/bold green] " + methodinput)
     
    return methodinput

 # when we know what choice is made, call one or other function

def recallinput(methodinput):
    if methodinput == "GUI":
        import GUI_input
        GUI_input.gui_window()
                
    elif methodinput == "Terminal":
        import terminal_input
        terminal_input.terminal_enquiry()    
   
    else:
        messagebox.showinfo(
        title="Select user input method",
        message=f"Please select either 'GUI' or 'Terminal'")

# what we now need to do is to retrieve the input data from either file.

def file_handling():
##file handling to produce readme file
    fnew_input = str(methodinput)

# create text file of input responses without formatting
    fnew = open("README2.md", "w")
    fnew.write(fnew_input)

    fnew.close()

#from this point, call the functions!
initialq()
recallinput(methodinput)
