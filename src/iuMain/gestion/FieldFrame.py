from tkinter import Frame,Label,Entry

class FieldFrame(Frame):
    def __init__(self, parent, tituloCriterios, criterios, tituloValores, valores=None, habilitado=None):
        super().__init__(parent, bg="white")
        self.tituloCriterios = tituloCriterios
        self.criterios = criterios
        self.tituloValores = tituloValores
        self.valores = valores if valores is not None else ["" for _ in criterios]
        self.habilitado = habilitado if habilitado is not None else [True for _ in criterios]

        # Crear los títulos de las columnas
        Label(self, text=self.tituloCriterios, font=("Arial", 10), bg="white").grid(row=0, column=0, padx=10,
                                                                                    pady=5, sticky="w")
        Label(self, text=self.tituloValores, font=("Arial", 10), bg="white").grid(row=0, column=1, padx=10, pady=5,
                                                                                    sticky="e")

        # Crear etiquetas y campos de entrada para cada criterio
        self.entries = {}  # Diccionario para almacenar las entradas
        for i, criterio in enumerate(self.criterios):
            # Etiqueta del criterio
            label = Label(self, text=criterio, font=("Arial", 10), bg="white")
            label.grid(row=i + 1, column=0, padx=10, pady=5, sticky="w")

            # Campo de entrada para el valor
            entry = Entry(self, width=30)
            entry.grid(row=i + 1, column=1, padx=10, pady=5)

            # Si tiene valor predeterminado, lo coloca
            if self.valores[i]:
                entry.insert(0, self.valores[i])

            # Si el campo no está habilitado, lo desactiva
            if not self.habilitado[i]:
                entry.config(state="disabled")

            # Guardar la referencia del campo de entrada
            self.entries[criterio] = entry