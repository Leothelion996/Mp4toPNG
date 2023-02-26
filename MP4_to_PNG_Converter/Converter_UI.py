import tkinter as tk
from tkinter import filedialog
from Convert_logic import start_conversion

class App:
    def __init__(self, master):
        self.master = master
        master.title("Video Converter")

        # Input Folder Section
        self.input_label = tk.Label(master, text="Input Folder:")
        self.input_label.grid(row=0, column=0, sticky="w")
        self.input_path = tk.StringVar()
        self.input_entry = tk.Entry(master, textvariable=self.input_path, width=50)
        self.input_entry.grid(row=0, column=1)
        self.input_button = tk.Button(master, text="Browse", command=self.select_input_folder)
        self.input_button.grid(row=0, column=2)

        # Output Folder Section
        self.output_label = tk.Label(master, text="Output Folder:")
        self.output_label.grid(row=1, column=0, sticky="w")
        self.output_path = tk.StringVar()
        self.output_entry = tk.Entry(master, textvariable=self.output_path, width=50)
        self.output_entry.grid(row=1, column=1)
        self.output_button = tk.Button(master, text="Browse", command=self.select_output_folder)
        self.output_button.grid(row=1, column=2)

        # Resolution Section
        self.resolution_label = tk.Label(master, text="Resolution:")
        self.resolution_label.grid(row=2, column=0, sticky="w")
        self.resolution_options = ["512:512", "512:768", "1024:1024", "1024:1536", "2048:2048"]
        self.display_options = ["512x512", "512x768", "1024x1024", "1024x1536", "2048x2048"]
        self.resolution_var = tk.StringVar()
        self.resolution_var.set(self.resolution_options[0])
        self.resolution_dropdown = tk.OptionMenu(master, self.resolution_var, *self.resolution_options)
        self.resolution_dropdown.grid(row=2, column=1)


        # Frame Rate Section
        self.framerate_label = tk.Label(master, text="Choose your framerate:")
        self.framerate_label.grid(row=3, column=0, sticky="w")
        self.framerate_var = tk.StringVar()
        self.framerate_var.set("20")
        self.framerate_entry = tk.Entry(master, textvariable=self.framerate_var)
        self.framerate_entry.grid(row=3, column=1)

        # Loading Bar Section
        self.loading_label = tk.Label(master, text="Loading:")
        self.loading_label.grid(row=4, column=0, sticky="w")
        self.loading_var = tk.DoubleVar()
        self.loading_var.set(0.0)
        self.loading_bar = tk.Scale(master, from_=0, to=100, orient=tk.HORIZONTAL, length=200, showvalue=False, variable=self.loading_var)
        self.loading_bar.grid(row=4, column=1)

        # Disable manual sliding of the loading bar
        self.loading_bar.bind("<Button-1>", lambda event: "break")

        # Convert Button Section
        self.convert_button = tk.Button(master, text="Convert", command=self.convert_video)
        self.convert_button.grid(row=5, column=1)

        # Close Button Section
        self.close_button = tk.Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=6, column=1)
     

    def select_input_folder(self):
        self.input_path.set(filedialog.askdirectory())

    def select_output_folder(self):
        self.output_path.set(filedialog.askdirectory())

    def convert_video(self):
        start_conversion(self)


root = tk.Tk()
app = App(root)
root.mainloop()
