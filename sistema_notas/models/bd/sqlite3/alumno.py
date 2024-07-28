import sqlite3
from .connect import con
import tkinter as tk


class AlumnoModel:
    def __init__(self) -> None:        
        self.codigo=tk.StringVar()
        self.nombres=tk.StringVar()
        self.apellidos=tk.StringVar()
        self.correo=tk.StringVar()
        if not  self.exits():
            self.create() 

    def exits(self):
        exit=False
        try:         
            cur = con.cursor()
            sql = "SELECT * FROM alumno"
            cur.execute(sql)
            exit = True
            return exit
        except:
            return exit

    def create(self):
            cur = con.cursor()
            sql = "CREATE TABLE alumno(codigo, nombres, apellidos, correo)"
            cur.execute(sql)
            con.commit()

    def add(self):
        cur = con.cursor()
        sql = "INSERT INTO alumno values(%s, %s, %s, %s)"
        data = (self.codigo.get(),self.nombres.get(),self.apellidos.get(),self.correo.get())
        cur.execute(sql, data)
        con.commit()

    def getAll(self)->list:
        cur = con.cursor()
        sql = "SELECT * FROM alumno"
        cur.execute(sql)
        list=[]
        
            
    def update(self):
        pass
    
    def delete(self):
       pass

    def find(self):
        pass
                