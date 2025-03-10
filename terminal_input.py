#install Inquirer
#remember to pip install InquirerPy
from InquirerPy import prompt
from InquirerPy.utils import color_print


def terminal_enquiry():

    questions = [
    {"type": "input", "message": "Project Title:", "name": "title"},
    {"type": "input", "message": "Project Description:", "name": "desc"},
    {"type": "input", "message": "Installation Instructions:", "name": "install"},
    {"type": "input", "message": "Usage Instructions:", "name": "usage"},
    {"type": "input", "message": "Author details:", "name": "author"},
    {"type": "list", "message": "Licence:","name":"licence",
    "choices": lambda result: ["MIT License",
                "Apache License 2.0",
                "GNU General Public License (GPL v3)",
                    "JGNU Lesser General Public License (LGPL v3)",
                    "Mozilla Public License 2.0 (MPL 2.0)",
                    "Creative Commons Licenses (CC0, CC BY, etc.",
                    "Unlicense"]},
    {"type": "confirm", "message": "Confirm Licence is correct y/n?", "default": True, "name":"confirm"}]
    global result
    result = prompt(questions)

    #works to here

    #create variables to hold input from

    global project_title
    project_title =result["title"]

    global project_desc
    project_desc = result["desc"]

    global install_ins
    install_ins = result["install"]

    global usage_ins
    usage_ins = result["usage"]

    global authdet
    authdet = result["author"]

    global lic_type
    lic_type = result["licence"]

    global contents
    contents = {"Project Title: " + project_title +
            "Project Description:  " + project_desc +
            "Installation Instructions: " + install_ins +
            "Usage Instructions: " + usage_ins +
            "Licence Information: " + lic_type +
            "Author Details: " + authdet}
    
        ##file handling to produce readme file
            # create text file of input responses without formatting
    global filenew
    filenew = open("README.md", "w")
    filenew.write(str(contents))
    filenew.close()

    color_print(contents)

    return contents

terminal_enquiry()
   



