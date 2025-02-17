#install Inquirer
#remember to pip install InquirerPy
from InquirerPy import prompt

#prompt for Project Title


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

    if result[2] == n:
          {"type": "list",
        "message": "Licence:",
        "choices": ["MIT License", "Apache License 2.0", "GNU General Public License (GPL v3)", "JGNU Lesser General Public License (LGPL v3),""Mozilla Public License 2.0 (MPL 2.0)","Creative Commons Licenses (CC0, CC BY, etc.","Unlicense"]
        },
        {"type": "confirm", "message": "Confirm Licence is correct? (y/n)"},
        else
         { "message": "Details are complete"},

]

#create variables to hold input from
result = prompt(questions)
project_title = result["title"]
project_desc = result["desc"]
install_ins = result["install"]
usage_ins = result["usage"]

lic_type = result[1]
confirm = result[2]

#**Use `Rich`** to enhance the user experience with **colored text and structured output**.

