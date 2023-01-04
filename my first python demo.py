from tkinter import Tk
from tkinter import ttk

class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("My First GUI program")
        self.geometry("400x300")

        self.mainloop()
        
    
if __name__=="__main__":
    win=MainWindow()