import tkinter as tk

class PackingListCalculator:

    #main method for the list object
    def __init__(self, master):
        self.master = master
        self.master.title("Packing List Calculator")

        self.label1 = tk.Label(master, text="Number of pants:")
        self.label1.grid(row=0, column=0, sticky="w")
        self.pants = tk.Entry(master)
        self.pants.grid(row=0, column=1)

        self.label2 = tk.Label(master, text="Number of shirts:")
        self.label2.grid(row=1, column=0, sticky="w")
        self.shirts = tk.Entry(master)
        self.shirts.grid(row=1, column=1)

        self.label3 = tk.Label(master, text="Socks to pack:")
        self.label3.grid(row=2, column=0, sticky="w")
        self.socks = tk.Entry(master)
        self.socks.grid(row=2, column=1)

        self.label4 = tk.Label(master, text="Duration of trip (in days):")
        self.label4.grid(row=3, column=0, sticky="w")
        self.duration = tk.Entry(master)
        self.duration.grid(row=3, column=1)

        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate_items)
        self.calculate_button.grid(row=4, column=0)

        # self.label5 = tk.Label(master, text="Total items to pack:")
        # self.label5.grid(row=5, column=0, sticky="w")
        # self.total_items = tk.Label(master, text="")
        # self.total_items.grid(row=5, column=1)

        self.label6 = tk.Label(master, text="Pants to pack:")
        self.label6.grid(row=6, column=0, sticky="w")
        self.pants_to_pack = tk.Label(master, text="")
        self.pants_to_pack.grid(row=6, column=1)

        self.label7 = tk.Label(master, text="Shirts to pack:")
        self.label7.grid(row=7, column=0, sticky="w")
        self.shirts_to_pack = tk.Label(master, text="")
        self.shirts_to_pack.grid(row=7, column=1)

        self.label8 = tk.Label(master, text="Socks to pack:")
        self.label8.grid(row=8, column=0, sticky="w")
        self.socks_to_pack = tk.Label(master, text="")
        self.socks_to_pack.grid(row=8, column=1)



    
    #preform the calucaltion for the tems abd semd tghem tio tghte gui
    def calculate_items(self):
        try:
            pants = int(self.pants.get()) 
            shirts = int(self.shirts.get())
            socks = int(self.socks.get())
            duration = int(self.duration.get())
            #otal_items = (pants + shirts + socks(2 * duration)) #i broke this lol, prob not even nessicary
            #self.total_items.configure(text=str(total_items))
            pants_to_pack = pants if duration < 7 else pants + 1
            shirts_to_pack = shirts if duration < 14 else shirts + 2
            socks_to_pack = socks if duration < 14 else socks + 2
            self.pants_to_pack.configure(text=str(pants_to_pack * duration))
            self.shirts_to_pack.configure(text=str(shirts_to_pack * duration))
            self.socks_to_pack.configure(text=str(socks_to_pack * duration))
            self.write_to_file(pants_to_pack, shirts_to_pack)
        except ValueError:
            self.total_items.configure(text="Invalid input")

    #write to csv file for future use
    def write_to_file(self, pants_to_pack, shirts_to_pack, socks_to_pack):
        with open("packing_list.txt", "w") as f:
            f.write("Pants to pack: {}\n".format(pants_to_pack))
            f.write("Shirts to pack: {}\n".format(shirts_to_pack))
            f.write("Socks to pack: {}\n".format(socks_to_pack))

#bruh yk what this if for on fortnite
if __name__ == "__main__":
    root = tk.Tk()
    app = PackingListCalculator(root)
    root.mainloop()
