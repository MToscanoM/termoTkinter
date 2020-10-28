from tkinter import *
from tkinter import ttk

class mainApp(Tk):
    entrada = None
    tipoUnidad = None
    
    def __init__(self):
        Tk.__init__(self)
        
        self.geometry("200x150")
        self.title("Termómetro")
        self.configure(bg="#DED7B9")
        
        self.temperatura = StringVar(value="")
        self.tipoUnidad = StringVar(value="C")
        
        self.createLayout()
        
    def createLayout(self):
        self.entrada = ttk.Entry(self, textvariable=self.temperatura).place(x=10, y=10)
        
    def start(self):
        self.mainloop()


if __name__ == '__main__':
    app = mainApp()
    app.start()
