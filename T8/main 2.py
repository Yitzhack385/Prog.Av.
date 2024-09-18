"""
- Pacientes
- Médicos
- Consultas
- Medicamentos
"""

from Paciente.paciente import Paciente
from Medico.medico import Medico
from Hospital.hospital import Hospital

hospital = Hospital()

while True:
    print("*** Menú del Hospital ***")
    print("1. Registrar paciente")
    print("2. Registrar médico")
    print("3. Mostrar pacientes")
    print("4. Mostrar medicos")
    print("5. Eliminar pacientes")
    print("6. Eliminar medicos")
    print("7. Mostrar pacientes menores de edad")
    print("8. Mostrar pacientes mayores de edad")
    print("9. Salir")

    opcion_usuario = int(input("Ingrese una opción: "))

    if opcion_usuario == 1:
        print("Seleccionaste la opcion para registrar un paciente")

        nombre = input("Ingrese el nombre del paciente: ")
        ano_nacimiento = int(input("Ingrese el ano_nacimiento del paciente: "))
        peso = float(input("Ingrese el peso del paciente: "))
        estatura = float(input("Ingrese la estatura del paciente: "))
        direccion = input("Ingrese la dirección del paciente: ")

        paciente = Paciente(nombre=nombre, ano_nacimiento=ano_nacimiento, peso=peso, estatura=estatura, direccion=direccion)
        hospital.registrar_paciente(paciente)

        print("Paciente registrado correctamente.")

    elif opcion_usuario == 2:
        print("Seleccionaste la opcion para registrar un médico")

        nombre = input("Ingrese el nombre del médico: ")
        ano_nacimiento = int(input("Ingrese el ano_nacimiento del médico: "))
        rfc = input("Ingrese el RFC del médico: ")
        direccion = input("Ingrese la dirección del médico: ")

        medico = Medico(nombre=nombre, ano_nacimiento=ano_nacimiento, rfc=rfc, direccion=direccion)
        hospital.registrar_medico(medico)

        print("Médico registrado correctamente.")

    elif opcion_usuario == 3:
        hospital.mostrar_pacientes()

    elif opcion_usuario == 4:
        hospital.mostrar_medicos()

    elif opcion_usuario == 5:
        hospital.eliminar_paciente()

    elif opcion_usuario == 6:
        hospital.eliminar_medico()

    elif opcion_usuario == 7:
        hospital.mostrar_pacientes_menores()
    
    elif opcion_usuario == 8:
        hospital.mostrar_pacientes_mayores()

    elif opcion_usuario == 9:
        print("Hasta la vista baby...")
        break


    


