import tkinter as tk
from tkinter import ttk,PhotoImage
from ..widgets.text import Text
from models.bd.postgress.alumno import AlumnoModel 
from controllers.alumno import AlumnoController
from ..icons.icon import Icon

class AlumnoView(ttk.Frame):
    def __init__(self,parent,typedb):
        super().__init__(parent)
        self.controller=AlumnoController(typedb)
        self.entity=self.controller.select_db()     
        self.parent=parent
        self.pack(fill="both",expand=1)
        self.frmClose =ttk.Frame(self)
        self.frmClose.pack(fill="both")

        self.iconClose =PhotoImage(file=Icon.close)
        self.iconAdd = PhotoImage(file=Icon.add)
        self.iconUpdate = PhotoImage(file=Icon.tool)
        self.iconClean = PhotoImage(file=Icon.broom)
        self.iconDelete = PhotoImage(file=Icon.trash)
        self.iconFind = PhotoImage(file=Icon.search)

        self.btnClose = ttk.Button(self.frmClose,image=self.iconClose,command=self.on_close)
        self.btnClose.pack(side="right")

        self.frmAdd = ttk.LabelFrame(self,text="Agregar")
        self.frmAdd.pack(fill="both")

        self.txtCodigo = Text(self.frmAdd,label="Codigo",value=self.entity.codigo,min=0,max=5,width=10)
        self.txtNombres = Text(self.frmAdd,label="Nombres",value=self.entity.nombres,min=0,max=20,width=25)
        self.txtApellidos =Text(self.frmAdd,label="Apellidos",value=self.entity.apellidos,min=0,max=20,width=25)
        self.txtCorreo = Text(self.frmAdd,label="Correo",value=self.entity.correo,min=0,max=20,width=25)

        self.frmButtons =ttk.Frame(self)
        self.frmButtons.pack(fill="both")
        
        self.btnAdd=ttk.Button(self.frmButtons,image=self.iconAdd, text="Agregar",compound="left", command=self.on_add)
        self.btnAdd.pack(side="left")       

        self.btnUpdate=ttk.Button(self.frmButtons,image=self.iconUpdate, text="Actualizar",compound="left",command=self.on_update)
        self.btnUpdate.pack(side="left")

        self.btnClean =ttk.Button(self.frmButtons,image=self.iconClean, text="Limpiar",compound="left",command=self.on_clean)
        self.btnClean.pack(side="left") 

        self.btnDelete = ttk.Button(self.frmButtons,image=self.iconDelete,text="Borrar",compound="left",command=self.on_delete)
        self.btnDelete.pack(side="left")

        self.btnFind = ttk.Button(self.frmButtons,image=self.iconFind,text="Buscar",compound="left",command=self.on_find)
        self.btnFind.pack(side="left")


        self.columns=("nombres","apellidos","correo")
        self.gv=ttk.Treeview(self,columns=self.columns)
        self.gv.pack(fill="both",expand=1)
        self.gv.heading("#0",text="Código",anchor="center")
        self.gv.heading("nombres",text="Nombres",anchor="center")
        self.gv.heading("apellidos",text="Apellidos",anchor="center")
        self.gv.heading("correo",text="Correo",anchor="center")
        self.gv.column("#0",anchor="center")
        self.gv.column("nombres",anchor="center")
        self.gv.column("apellidos",anchor="center")
        self.gv.column("correo",anchor="center")
        
        self.on_load()
    
    def on_close(self):
        self.parent.notebook.pack(fill="both",expand=1)
        self.destroy()

    def on_add(self):
        self.entity.add()
        self.entity.codigo.set("")
        self.entity.nombres.set("")
        self.entity.apellidos.set("")
        self.entity.correo.set("")
        self.on_load()
    
    def on_load(self):
        self.gv.delete(*self.gv.get_children())
        for item in self.entity.getAll():
            data = (item.nombres.get(),item.apellidos.get(),item.correo.get())
            self.gv.insert("","end",text=item.codigo.get(),values=data,tags="Select")
            self.gv.tag_bind("Select","<<TreeviewSelect>>",self.on_select)
        
    def on_select(self,event):
        index =self.gv.focus()
        row=self.gv.item(index)
        self.entity.codigo.set(row["text"])
        self.entity.nombres.set(row["values"][0])
        self.entity.apellidos.set(row["values"][1])
        self.entity.correo.set(row["values"][2])
        self.txtCodigo.entry.config(state="readonly")

    def on_update(self):
        self.entity.update()
        self.on_load()

    def on_clean(self):
        self.entity.codigo.set("")
        self.entity.nombres.set("")
        self.entity.apellidos.set("")
        self.entity.correo.set("")
        self.txtCodigo.entry.config(state="normal")
        self.on_load()
    
    def on_delete(self):
        self.entity.delete()
        self.on_clean()

    def on_find(self):
        self.gv.delete(*self.gv.get_children())
        for item in self.entity.find():
            data = (item.nombres.get(),item.apellidos.get(),item.correo.get())
            self.gv.insert("","end",text=item.codigo.get(),values=data,tags="Select")
            self.gv.tag_bind("Select","<<TreeviewSelect>>",self.on_select)        
        