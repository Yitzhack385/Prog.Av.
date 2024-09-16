class Hospital:
    pacientes = []
    medicos = []
    consultas = []

    def registrar_consulta(self, id_paciente, id_medico):
        if not self.validar_cantidad_usuarios():
            return
        
        if self.validar_existencia_paciente(id_paciente) == False or self.validar_existencia_medico(id_medico) == False:
            print("No se puede registrar la consulta, no existe el médico o el paciente")
            return
        
        print("Continuamos con el registro")

    def registrar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def registrar_medico(self, medico):
        self.medicos.append(medico)

    def mostrar_pacientes(self):
        print("*** Pacientes en el Sistema ***")
        for paciente in self.pacientes:
            paciente.mostrar_informacion()

# TAREA ---------------------------

    def mostrar_medicos(self):
        print("*** Médicos en el Sistema ***")
        for medico in self.medicos:
            medico.mostrar_informacion()

    def mostrar_pacientes_menores(self):
        print("*** Pacientes Menores de Edad ***")
        for paciente in self.pacientes:
            if paciente.edad < 18:
                paciente.mostrar_informacion()

    def mostrar_pacientes_mayores(self):
        print("*** Pacientes Mayores de Edad ***")
        for paciente in self.pacientes:
            if paciente.edad >= 18:
                paciente.mostrar_informacion()

    def eliminar_paciente(self, id_paciente):
        self.pacientes = [paciente for paciente in self.pacientes if paciente.id != id_paciente]

    def eliminar_medico(self, id_medico):
        self.medicos = [medico for medico in self.medicos if medico.id != id_medico]

#-------------------------

    def validar_existencia_paciente(self, id_paciente):
        for paciente in self.pacientes:
            if paciente.id == id_paciente:
                return True
  
        return False
    
    def validar_existencia_medico(self, id_medico):
        for medico in self.medicos:
            if medico.id == id_medico:
                return True
            
        return False
        
    def validar_cantidad_usuarios(self):
        if len(self.pacientes) == 0:
            print("No puedes registra una consulta, no existen pacientes")
            return False
        
        if len(self.medicos) == 0:
            print("No puedes registra una consulta, no existen médicos")
            return False
        
        return True


    
