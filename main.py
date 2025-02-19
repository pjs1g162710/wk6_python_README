#install Inquirer
#pip install InquirerPy
from InquirerPy import prompt
from InquirerPy.utils import color_print
from InquirerPy import inquirer

#pip install rich
from rich import print as rprint
from rich.console import Console
from rich.text import Text

import tkinter as tk
from tkinter import ttk

#First use inquirerpy to ask the user whether they want to use GUI or terminal inputs

def choose_input():
    color_print([("class:aaa", "fooboo")], style={"aaa": "#000000"})
    questions = [
          {
        "type": "list",
        "message": "Would you prefer to use GUI or terminal inputs?",
        "choices": ["GUI", "Terminal"],
        "name":"input"
        },
        {"type": "confirm", "message": "Confirm?"},
        ]

    result = prompt(questions)
    print(result)
    return result
   



input_type = questions.choices[1]
print(input_type)
confirm = result[2]
print(confirm)   

# when we know what choice is made, call one or other function

if (input_type == 'GUI'):
    from GUI_input import GUI_window

elif(input_type == 'Terminal'):
    from GUI_input import GUI_window
else:
    from GUI_input import GUI_window


# what we now need to do is to retrieve the input data from either file.



  
##file handling to produce readme file
fnew_input = str(result)

# create text file of input responses without formatting
fnew = open("README.md", "w")
fnew.write(fnew_input)

fnew.close()





#**Use `Rich`** to enhance the user experience with **colored text and structured output**.
#experimenting with Rich syntax
console = Console()
text = Text("Hello, World!")
text.stylize("bold magenta", 0, 6)
console.print(text)

text = Text.assemble(("Hello", "bold magenta"), " World!")
console.print(text)

#justify (left, center, right or full)
#overflow (fold. crop, ellipsis)
#no_wrap ()
#tab size (sets number of char in tab)
