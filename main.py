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





gui_choice (

)




  









questions = [
    {"type": "input", "message": "Project Title:", "name": "title"},
    {"type": "input", "message": "Project Description:", "name": "desc"},
    {"type": "input", "message": "Installation Instructions:", "name": "install"},
      {"type": "input", "message": "Usage Instructions:", "name": "usage"},



    {
        "type": "list",
        "message": "Licence:",
        "choices": ["MIT License", "Apache License 2.0", "GNU General Public License (GPL v3)", "JGNU Lesser General Public License (LGPL v3),""Mozilla Public License 2.0 (MPL 2.0)","Creative Commons Licenses (CC0, CC BY, etc.","Unlicense"]
    },
    {"type": "confirm", "message": "Confirm Licence is correct? (y/n)"},

       # if "n" in result[2]:
       # {"type": "list",
       # "message": "Licence:",
       # "choices": ["MIT License", "Apache License 2.0", "GNU General Public License (GPL v3)", "JGNU Lesser General Public License (LGPL v3),""Mozilla Public License 2.0 (MPL 2.0)","Creative Commons Licenses (CC0, CC BY, etc.","Unlicense"]
       # },
       # {"type": "confirm", "message": "Confirm Licence is correct? (y/n)"},
       # else
       # { "message": "Details are complete"},

]



#create variables to hold input from
result = prompt(questions)
project_title = result["title"]
project_desc = result["desc"]
install_ins = result["install"]
usage_ins = result["usage"]

lic_type = result[4]
confirm = result[5]

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
