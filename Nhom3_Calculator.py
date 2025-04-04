#B23DCDT249 - Nguyen ba tho
from tkinter import *
from math import *
class App:
    def __init__(self, master):
        self.master = master
        self.master.geometry("342x600")
        self.master.title("Calculator")
        self.master.grid_rowconfigure(0, weight=0)
        self.master.grid_columnconfigure(0, weight=0)
        self.master.config(bg="black")
        button_texts = [
            ["DEL", "AC", "%", "/"],
            ["7", "8", "9", "x"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["+/-", "0", ",", "="],
        ]
        
        # Create the display area
        self.display = Entry(master, font=("Arial", 20), bd=10, relief=FLAT, justify=RIGHT, bg= "black",fg = "white")
        self.display.grid(row=0, column=0, columnspan=4, ipadx=5, ipady=50)

        # Create the buttons
        for i in range(5):  # Rows
            for j in range(4):  # Columns
                num = button_texts[i][j]
                if num: 
                    if num == "=":
                        btn = Button(master, text=num, font=("Arial", 12), width=8, height=4,
                            command=lambda n=num: self.on_button_click(n), bg="orange", fg="white")
                    elif num in ["AC","%","DEL"]:
                        btn = Button(master, text=num, font=("Arial", 12), width=8, height=4,
                            command=lambda n=num: self.on_button_click(n), bg="#5C5C5F", fg="white")
                    elif num in ["+", "-", "x", "/"]:
                        btn = Button(master, text=num, font=("Arial", 12), width=8, height=4,
                            command=lambda n=num: self.on_button_click(n), bg="#FF9F0A", fg="white")
                    elif num == "":
                        btn = Button(master, text="", state=DISABLED, font=("Arial", 12), width=8, height=4,
                        bg="black", relief=FLAT)
                    else:
                        btn = Button(master, text=num, font=("Arial", 12), width=8, height=4,
                            command=lambda n=num: self.on_button_click(n), bg="#2A2A2C", fg="white")
                    btn.grid(row=i + 1, column=j, padx=1, pady=1)

    def on_button_click(self, char):
        if char == "=":  
            try:
                expression = self.display.get().replace("x", "*") 
                result = eval(expression)
                self.display.delete(0, END)
                self.display.insert(END, str(result))
            except:
                self.display.delete(0, END)
                self.display.insert(END, "Lỗi")
        elif char == "AC":  
            self.display.delete(0, END)
        elif char == "+/-":
            try:
                current = float(self.display.get())
                self.display.delete(0, END)
                self.display.insert(END, str(-current))
            except:
                pass  
        elif char == "DEL":
            current = self.display.get()
            if current:
                self.display.delete(len(current)-1, END)
        elif char == "%":  
            try:
                current = float(self.display.get()) / 100  # Tính phần trăm
                current = self.math.ceil(current)  # Làm tròn lên
                self.display.delete(0, END)
                self.display.insert(END, str(current))
            except:
                pass
        else:  
            self.display.insert(END, char)

root = Tk()
app = App(root)
root.mainloop()
