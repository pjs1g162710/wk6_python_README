import tkinter

#def GUI_window():
def print_text_text():
    project_title = input_text_title.get(1.0)
    project_desc = input_text_desc.get(1.0)
    inst = input_text_inst.get(1.0)
    usage_ins = input_text_usage.get(1.0)

    label = tkinter.Label(root, text="")
    label.pack(pady=10)
    label.config(text="User entered : " + project_title + " " + project_desc + " " + inst + " " + usage_ins)

#This collects the inputs from the GUI window and designates them as variables
def submit_callback():#
    project_title = input_text_title.get(1.0, 100.0)
    project_desc = input_text_desc.get(1.0, 100.0)
    inst = input_text_inst.get(1.0, 500.0)
    usage_ins = input_text_usage.get(1.0, 500.0)


# This prints the inputs given to the console to check they are correct, and saves to file
    print(
        "User entered :\n " +
        "Project Title: " + project_title +
        "\nProject Description:  " + project_desc +
        "\nInstallation Instructions: " + inst +
        "\nUsage Instructions: " + usage_ins)

    contents = {"Project Title: " + project_title +
        "Project Description:  " + project_desc +
        "Installation Instructions: " + inst +
        "Usage Instructions: " + usage_ins}

    ##file handling to produce readme file
        # create text file of input responses without formatting
    filenew = open("README.md", "w")
    filenew.write(str(contents))

    filenew.close()


    return project_title + project_desc + inst + usage_ins


    # Creating tkinter window
root = tkinter.Tk()
root.title("Build a README File for Github")
root.geometry('500x550')
    #This is the label for the first field
input_label_title = tkinter.Label(root, text="Project Title" ,font = ("Arial", 12)).grid(column = 0,row = 1, padx = 5, pady = 5)

# try doing this as a text box rather than an entry
input_text_title = tkinter.Text(root, width=55, height=2)
input_text_title.grid(column=0, row=2, padx = 8, pady = 5)

    #this is the input label for the second field
input_label_desc = tkinter.Label(root,text="Project Description" ,font = ("Arial", 12)).grid(column = 0,row = 3, padx = 2, pady = 5)

    #this is the text box for the second field
input_text_desc = tkinter.Text(root, width=55, height=2)
input_text_desc.grid(column=0, row=4, padx = 8, pady = 5)

    #this is the input label for the third field
input_label_inst = tkinter.Label(root,text="Installation Instructions" ,font = ("Arial", 12)).grid(column = 0,row = 5, padx = 2, pady = 5)

    #this is the text box for the third field
input_text_inst = tkinter.Text(root, width=55, height=6 )
input_text_inst.grid(column = 0,row = 6, padx = 2, pady = 5)

    #this is the input label for the fourth field
input_label_usage = tkinter.Label(root,text="Usage Instructions" ,font = ("Arial", 12)).grid(column = 0,row = 7, padx = 2, pady = 5)

# this is the text box for the fourth field
input_text_usage = tkinter.Text(root, width=55, height=6)
input_text_usage.grid(column = 0,row = 8, padx = 5, pady = 5)

#submit button
submit_button = tkinter.Button(root, text = "Submit" , activebackground= 'blue', command =submit_callback)
submit_button.grid(column=0, row=9, padx = 10, pady = 5)

root.mainloop()


