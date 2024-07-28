from tkinter import ttk

class Text(ttk.Frame):
    def __init__(self,parent=None,label="",value="",min=0,max=3,width = 8):
        super().__init__(parent)        
        self.pack(fill="both")
        self.min=min
        self.max=max


        self.lbl=ttk.Label(self,text=label+":",width=8)
        self.lbl.pack(side="left", padx=5,pady=5)
        self.entry = ttk.Entry(self,textvariable=value,width=12)
        
        self.validateLenght = self.register(self.on_change)
        self.entry.config(validate="key", validatecommand=(self.validateLenght,"%P"),width=width)
        
        self.entry.pack(side="left",padx=5, pady=5)
        

    def on_change(self,text):        
        longitud_minima = self.min
        longitud_maxima = self.max

        if longitud_minima <= len(text) <= longitud_maxima:
            return True  # Permite la entrada
        else:
            return False  # Rechaza la entrada