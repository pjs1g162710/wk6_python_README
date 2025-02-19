import tkinter as tk
from tkinter import ttk

def GUI_window():

    # Creating tkinter window
    window = tk.Tk()
    window.title('Build a README File for Github')
    window.geometry('500x550')
  

    #This is the label for the first field
    input_label_title = tk.Label(window, text="Project Title" ,font = ("Arial", 14)).grid(column = 0,row = 1, padx = 2, pady = 5)
    #input_label.place(column = 1, row = 30)

    #this is the text box for the first field
    input_entry_title = tk.Entry(window, text="titleTK" ,font = ("Arial", 14))
    input_entry_title.grid(column = 0,row = 2, padx = 20, pady = 10)

    #this is the input label for the second field
    input_label_desc = tk.Label(window, text="Project Description" ,font = ("Arial", 14)).grid(column = 0,row = 3, padx = 2, pady = 5)
    #input_label.place(column = 1, row = 30)

    input_entry_desc = tk.Entry(window, text="descTK" ,font = ("Arial", 14))
    input_entry_desc.grid(column = 0,row = 4, padx = 20, pady = 10)

    #this is the input label for the third field
    input_label_inst = tk.Label(window, text="Installation Instructions" ,font = ("Arial", 14)).grid(column = 0,row = 5, padx = 2, pady = 5)
    #input_label.place(column = 1, row = 30)

    input_entry_inst = tk.Entry(window, text="instTK" ,font = ("Arial", 14))
    input_entry_inst.grid(column = 0,row = 6, padx = 20, pady = 10)

    #this is the input label for the fourth field
    input_label_usage = tk.Label(window, text="Usage Instructions" ,font = ("Arial", 14)).grid(column = 0,row = 7, padx = 2, pady = 5)
    #input_label.place(column = 1, row = 30)

    input_entry_usage = tk.Entry(window, text="useTK" ,font = ("Arial", 14))
    input_entry_usage.grid(column = 0,row = 8, padx = 20, pady = 10)



    submit_button = tk.Button(window, text = "Submit" , command = lambda: submit_callback(submit_button))

    submit_button.grid(column=5, row=11)

    def submit_callback(submit_button):
    #print("User entered : " + input_entry.get())
    #return None

        project_title = input_entry_title.get()
        project_desc = input_entry_desc.get()
        inst = input_entry_inst.get()
        usage_ins = input_entry_usage.get()

    window.mainloop()

