import tkinter as tk
from pyCalcTB import PackingListCalculator

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.quit_button = tk.Button(self, text="Quit", command=self.master.destroy)
        self.quit_button.pack(side="bottom")

        self.calculate_button = tk.Button(self, text="Calculate Packing List", command=self.run_calculator)
        self.calculate_button.pack(side="top")

    def run_calculator(self):
        root = tk.Tk()
        app = PackingListCalculator(root)
        root.mainloop()

root = tk.Tk()
app = Application(master=root)
app.mainloop()