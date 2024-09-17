from tkinter import Frame,Label,Entry
class FieldFrame(Frame):
    def __init__(self, frame,tituloCriterios, criterios, tituloValores, valores, habilitado,ancho_entry=20):
        super().__init__(frame,bg="white")

        self.valores=[]

        #Etiquetas para los títulos de las columnas
        Label(self, text=tituloCriterios,bg="white",font=("Helvetica", 12, "bold")).grid(row=0, column=0)
        Label(self, text=tituloValores,bg="white",font=("Helvetica", 12, "bold")).grid(row=0, column=1)

        # Etiquetas y campos de entrada para cada criterio
        for i, criterio in enumerate(criterios, start=1):
            Label(self, text=criterio,bg="white", font=("Helvetica", 10, "bold")).grid(row=i, column=0, padx=20, pady=5, sticky="w")
            entry = Entry(self,width=ancho_entry)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky="w")
            # Se inserta los valores por defecto que queramos
            if valores is not None:
                #el número 0 indica que se inserta desde el inicio del string
                entry.insert(0, valores[i - 1])
            #Para deshabilitar el entry
            if habilitado is not None and not habilitado[i - 1]:
                entry.config(state='readonly')

            #Se guarda la referencia de ese entry
            self.valores.append(entry)

    def habilitarEntry(self, indice, habilitar):
        if habilitar:
            return self.valores[indice - 1].config(state="normal")
        else:
            return self.valores[indice - 1].config(state="readonly")

    def getValue(self, criterio):
        if criterio - 1 < len(self.valores):
            return self.valores[criterio-1].get()
        else:
            raise ValueError("Invalid criterio value")


    