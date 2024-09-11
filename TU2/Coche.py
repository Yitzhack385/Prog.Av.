class coche:
    marca = ""
    modelo = ""
    año = 0

    # Constructor


    def _init_(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    # Metodo MOSTRAR INFORMACION

    def mostrar_informacion(self):
        print("Marca: " + str(self.marca))
        print("Modelo: " + str(self.modelo))
        print("Año: " + str(self.año))




    
    

