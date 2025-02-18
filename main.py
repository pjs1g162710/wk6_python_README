#install Inquirer
#remember to pip install InquirerPy
from InquirerPy import prompt
from InquirerPy.utils import color_print
from InquirerPy import inquirer

#remember to install pip install rich
from rich import print as rprint
from rich.console import Console
from rich.text import Text

import tkinter as tk
from tkinter import ttk

#First use inquirerpy to ask the user whether they want to use GUI or terminal inputs


prompt_GUI = inquirer.text(askGUI ="Would you prefer to use GUI inputs (y/n)?")

selected = prompt(prompt_GUI)
selected_output = prompt_GUI["askGUI"]



result = prompt(questions)
project_title = result["title"]
#@prompt.register_kb("alt-b")
#def _(_):
 #   color_print([("#e5c07b", "Hello"), ("#ffffff", "World")])

#name = prompt.execute()
#color_print([("class:aaa", "fooboo")], style={"aaa": "#000000"})

# the coloured print function allows creation of coloured output
#color_print(formatted_text=[("class:aa", "hello "), ("class:bb", "world")], style={"aa": "red", "bb": "blue"})
#color_print([("red", "yes"), ("", " "), ("blue", "no")])


# when we know what choice is made, call one or other function

if (prompt_GUI == 'y'):
    from GUI_input import GUI_window()

elif(prompt_GUI == 'Y'):
    from GUI_input import GUI_window()

elif(prompt_GUI == 'Yes'):
    from GUI_input import GUI_window()

elif(prompt_GUI == 'yes'):
    from GUI_input import GUI_window()

else:
        from terminal_input import terminal_questions()


# what we now need to do is to retrieve the input data from either file.



  








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
