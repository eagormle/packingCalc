import tkinter as tk
from pyCalcTB import PackingListCalculator
from tkinter import ttk
from elePack import eleList

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Packing List Calculator")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Create a frame to contain the welcome text, description, and author name
        self.info_frame = tk.Frame(self)
        self.info_frame.pack(pady=10)

        self.welcome_label = tk.Label(self.info_frame, text="Welcome to Packing List Calculator", font=("Helvetica", 18))
        self.welcome_label.pack(pady=10)

        self.description_label = tk.Label(self.info_frame, text="This application helps you calculate packing items for a trip because my girlfriend does not know how to make a list!.", wraplength=300, justify="center")
        self.description_label.pack(pady=5)

        self.author_label = tk.Label(self.info_frame, text="Created by: Ethan :)", font=("Helvetica", 10))
        self.author_label.pack(pady=5)

        # Create a frame to contain the buttons
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(pady=10)

        self.calculate_button = tk.Button(self.button_frame, text="Calculate Packing List", command=self.run_calculator)
        self.calculate_button.pack(side="left", padx=10)

        self.quit_button = tk.Button(self.button_frame, text="Quit", command=self.master.destroy)
        self.quit_button.pack(side="left", padx=10)

        # Create a frame for the settings icon
        # self.settings_frame = tk.Frame(self)
        # self.settings_frame.pack(pady=10)

        # self.settings_icon = tk.PhotoImage(file="settings_icon.png")  # Replace with the file path of your settings icon
        # self.settings_button = ttk.Button(self.settings_frame, image=self.settings_icon)  # Add the command for the settings button
        # self.settings_button.pack()

    def run_calculator(self):
        root = tk.Tk()
        app = PackingListCalculator(root)
        root.mainloop()

    def runEle(self):
        root = tk.Tk()
        eleapp = eleList(root)
        root.mainloop()

root = tk.Tk()
app = Application(master=root)
app.mainloop()
