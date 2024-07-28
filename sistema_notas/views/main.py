import tkinter as tk
from tkinter import ttk
from typing import Literal
from .maestros.alumno import AlumnoView
from .icons.icon import Icon
class Main(tk.Tk):
    def __init__(self,title ="",typedb:Literal["postgres","sqlite3"]="postgres"):
        super().__init__()
        self.__typedb = typedb
        self.title(title)
        self.geometry("1200x800")
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)


        self.menuFile =tk.Menu(self.menu, tearoff=0)
        self.menuFile.add_command(label="New File",command="")
        self.menuFile.add_separator()      
        self.menuFile.add_command(label="Salir", command=self.destroy)
        
        self.menuMaster = tk.Menu(self.menu, tearoff=0)
        self.menuMaster.add_command(label="Alumno",command=self.load_alumno)


        self.menu.add_cascade(label="Archivo",menu=self.menuFile)
        
        self.menu.add_cascade(label="Maestros",menu=self.menuMaster)

        self.notebook = ttk.Notebook(self)
        self.notebook.pack()
        

    def load_alumno(self):
        self.alumno = AlumnoView(self,self.__typedb)        
        self.notebook.add(text="Alumno",child=self.alumno)
        self.notebook.pack(fill="both",expand=1)

    
    