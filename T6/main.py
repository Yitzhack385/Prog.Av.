from Estudiante import Estudiante
from Curso import Curso



# Cursos
curso1 = Curso("Matemáticas", "MATH101", "Dr. Smith")
curso2 = Curso("Física", "PHYS101", "Dr. Johnson")
curso3 = Curso("Programación", "CS101", "Prof. Lee")

# Estudiantes
estudiante1 = Estudiante("Juan Pérez", 20, "S001")
estudiante2 = Estudiante("María López", 22, "S002")

# Asignar cursos a estudiantes
estudiante1.agregar_curso(curso1)
estudiante1.agregar_curso(curso3)

estudiante2.agregar_curso(curso2)
estudiante2.agregar_curso(curso3)

# Mostrar información de los estudiantes
estudiante1.mostrar_informacion()
print("----------------------------")
estudiante2.mostrar_informacion()