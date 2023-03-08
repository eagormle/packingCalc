import tkinter as tk


class PackingListCalculator:

    #main method for the list object
    def __init__(self, master):
        self.master = master
        self.master.title("Packing List Calculator")
        self.items_to_pack = []

        self.label1 = tk.Label(master, text="Duration of trip (in days):")
        self.label1.grid(row=3, column=0, sticky="w")
        self.duration = tk.Entry(master)
        self.duration.grid(row=3, column=1)

        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate_items)
        self.calculate_button.grid(row=4, column=0)

        self.add_button = tk.Button(master, text="Add Items to Pack", command=self.open_input_window)
        self.add_button.grid(row=4, column=1)

        self.label2 = tk.Label(master, text="Pants to pack:")
        self.label2.grid(row=6, column=0, sticky="w")
        self.pants_to_pack = tk.Label(master, text="")
        self.pants_to_pack.grid(row=6, column=1)

        self.label3 = tk.Label(master, text="Shirts to pack:")
        self.label3.grid(row=7, column=0, sticky="w")
        self.shirts_to_pack = tk.Label(master, text="")
        self.shirts_to_pack.grid(row=7, column=1)

        self.label4 = tk.Label(master, text="Socks to pack:")
        self.label4.grid(row=8, column=0, sticky="w")
        self.socks_to_pack = tk.Label(master, text="")
        self.socks_to_pack.grid(row=8, column=1)

        self.label5 = tk.Label(master, text="Undergarmets to pack:")
        self.label5.grid(row=9, column=0, sticky="w")
        self.under_to_pack = tk.Label(master, text="")
        self.under_to_pack.grid(row=9, column=1)


        self.label6 = tk.Label(master, text="Items to pack:")
        self.label6.grid(row=10, column=0, sticky="w")
        self.items_to_pack_label = tk.Label(master, text="")
        self.items_to_pack_label.grid(row=10, column=1, sticky="w")

    # method to open new window for user input
    def open_input_window(self):
        input_window = tk.Toplevel(self.master)
        input_window.title("Add Items to Pack")

        input_label = tk.Label(input_window, text="Enter the items you need to pack, separated by commas:")
        input_label.pack()

        input_entry = tk.Entry(input_window)
        input_entry.pack()

        # function to process user input
        def process_input():
            items = input_entry.get().split(",")
            # store the items entered by the user
            self.items_to_pack.extend(items)

            # update the items label with the current list of items
            self.items_to_pack_label.configure(text=", ".join(self.items_to_pack))

            # close the input window
            input_window.destroy()

        add_button = tk.Button(input_window, text="Add Items", command=process_input)
        add_button.pack()

    #preform the calucaltion for the tems abd semd tghem tio tghte gui
    def calculate_items(self):
        try:
            pants_to_pack = 1
            shirts_to_pack = 1
            socks_to_pack = 1
            under_to_pack = 1
            duration = int(self.duration.get())
            self.pants_to_pack.configure(text=str(round((pants_to_pack * duration) * 1.5)))
            self.shirts_to_pack.configure(text=str(round((shirts_to_pack * duration) * 1.2)))
            self.socks_to_pack.configure(text=str(round((socks_to_pack * duration) * 1.5)))
            self.under_to_pack.configure(text=str(round((under_to_pack * duration) * 1.7)))

            # update the items label with the current list of items
            self.items_to_pack_label.configure(text=", ".join(self.items_to_pack))

            self.write_to_file(self.pants_to_pack['text'], self.shirts_to_pack['text'], self.socks_to_pack['text'], self.under_to_pack['text'], self.items_to_pack)
        except ValueError:
            self.total_items.configure(text="Invalid input")

    #write to txt file for future use
    def write_to_file(self, pants_to_pack, shirts_to_pack, socks_to_pack, under_to_pack, items_to_pack):
        with open("packing_list.txt", "w") as f:
            f.write("Pants to pack: {}\n".format(pants_to_pack))
            f.write("Shirts to pack: {}\n".format(shirts_to_pack))
            f.write("Pairs of socks to pack: {}\n".format(socks_to_pack))
            f.write("Underwear to pack: {}\n".format(under_to_pack))
            f.write("Items to pack: {}\n".format(", ".join(items_to_pack)))

#bruh yk what this if for on fortnite
if __name__ == "__main__":
    root = tk.Tk()
    app = PackingListCalculator(root)
    root.mainloop()
