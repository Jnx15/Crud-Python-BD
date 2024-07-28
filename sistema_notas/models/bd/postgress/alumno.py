import psycopg
from .connect import con

import tkinter as tk

class AlumnoModel:
    def __init__(self) -> None:        
        self.codigo=tk.StringVar()
        self.nombres=tk.StringVar()
        self.apellidos=tk.StringVar()
        self.correo=tk.StringVar()
    
    def add(self):
        with psycopg.connect(con) as conn:
            with conn.cursor() as cur:
                sql ="insert into Alumno (codigo,nombres,apellidos,correo) values (%s,%s,%s,%s)"
                data = (self.codigo.get(),self.nombres.get(),self.apellidos.get(),self.correo.get())
                cur.execute(sql,data)
                conn.commit()
    def getAll(self)->list:
        with psycopg.connect(con) as conn:
            with conn.cursor() as cur:
                sql ="select * from Alumno order by codigo"
                cur.execute(sql)
                list = []
                for res in cur:
                    item = AlumnoModel()
                    item.codigo.set(res[1])
                    item.nombres.set(res[2])
                    item.apellidos.set(res[3])
                    item.correo.set(res[4])
                    list.append(item)
                    del item
                return list
            
    def update(self):
        with psycopg.connect(con) as conn:
            with conn.cursor() as cur:
                sql ="update Alumno set nombres=%s, apellidos=%s, correo=%s where codigo =%s"
                data = (self.nombres.get(), self.apellidos.get(), self.correo.get(), self.codigo.get())
                cur.execute(sql,data)
                conn.commit()
    
    def delete(self):
        with psycopg.connect(con) as conn:
            with conn.cursor() as cur:
                sql="delete from Alumno where codigo=%s"
                data=(self.codigo.get(),)
                cur.execute(sql,data)
                conn.commit()

    def find(self):
        with psycopg.connect(con) as conn:
            with conn.cursor() as cur:
                data=(self.codigo.get(),self.nombres.get(),self.apellidos.get(), self.correo.get())
                sql=f"select * from Alumno where  codigoilike %{data[0]}% and nombres ilike %{data[1]}% and  apellidos ilike %{data[2]}% and correo ilike %{data[3]}%"
                cur.execute(sql)
                list = []
                for res in cur:
                    item = AlumnoModel()
                    item.codigo.set(res[1])
                    item.nombres.set(res[2])
                    item.apellidos.set(res[3])
                    item.correo.set(res[4])
                    list.append(item)
                    del item
                return list

                