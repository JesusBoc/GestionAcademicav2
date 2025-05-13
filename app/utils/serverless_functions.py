from app import create_app, db
from app.models.connections import *
from os import system
from datetime import date

def get_estudiantes(clase: Clase):
    estudiantes: list[Estudiante] = Estudiante.query.filter_by(salon_id=clase.salon_id).order_by(Estudiante.apellido,Estudiante.nombre)
    return estudiantes

def enumerate_estudiantes(estudiantes: list[Estudiante],msg:str):
    print(f"---------------------- {msg} ----------------------")
    for i, estudiante in enumerate(estudiantes):
        print(f"{i+1}) {estudiante.nombre_completo}")
    print("")

def agregar_estudiante(clase: Clase):
    system('cls')
    nombre = input("Ingrese el nombre del estudiante a agregar")
    apellido = input("Ingrese el apellido del estudiante a agregar")
    estudiante = Estudiante(nombre=nombre,apellido=apellido,salon_id=clase.salon_id)
    db.session.add(estudiante)
    db.session.commit()

def editar_estudiante(clase: Clase):
    estudiantes = get_estudiantes(clase)
    enumerate_estudiantes(estudiantes, "Estudiante a editar")
    # TODO: investigar cómo editar en la BD

def eliminar_estudiante(clase: Clase):
    estudiantes = get_estudiantes(clase)
    enumerate_estudiantes(estudiantes, "Estudiante a eliminar")
    seleccion = int(input("Estudiante a eliminar: "))
    if seleccion < 1 or seleccion > len(estudiantes):
        print("La opcion que escogiste no está en la lista")


def tomar_asistencia(clase: Clase):
    estudiantes = get_estudiantes(clase)
    for estudiante in estudiantes:
        system('cls')
        print("----------------------CHEAT SHEET----------------------")
        print("\t1) Presente")
        print("\t2) Tarde")
        print("\t3) Ausente")
        print("\t4) Excusa\n")
        while True:
            seleccion = int(input(f"Asistencia para {estudiante.nombre_completo}: "))
            if seleccion == 1:
                estado = EstadoAsistencia.PRESENTE
                break
            if seleccion == 2:
                estado = EstadoAsistencia.TARDE
                break
            if seleccion == 3:
                estado = EstadoAsistencia.AUSENTE
                break
            if seleccion == 4:
                estado = EstadoAsistencia.EXCUSA
                break
            print("Esa no es una opción!!!")
        asistencia = Asistencia(
            estudiante_id = estudiante.id,
            clase_id = clase.id,
            estado = estado,
            fecha = date.today()
        )
        db.session.add(asistencia)
    db.session.commit()

def menu_clase(salon: Salon):
    system('cls')
    opc = 0
    print(f"----------------------Selección de clase: {salon.nombre}----------------------")
    print("Selecciona la clase: ")
    for i, clase in enumerate(salon.clases):
        print(f"\t{i+1}) {clase.nombre_generado}")
    print(f"\t-1) Salir")
    opc = int(input("Opción: "))
    if(opc > i+1):
        print("La opción escogida no existe!")
        menu_clase(salon)
    if(opc < 0):
        return
    tomar_asistencia(salon.clases[opc-1])

def menu():
    system('cls')
    salones: list[Salon] = Salon.query.all()
    opc = 0
    print("----------------------Gestión de clases----------------------")
    print("Selecciona el salón en donde tendrás la clase: ")
    for i, salon in enumerate(salones):
        print(f"\t{i+1}) {salon.nombre}")
    print(f"\t-1) Salir")
    opc = int(input("Opción: "))
    if(opc > i+1):
        print("La opción escogida no existe!")
        menu()
    if(opc < 0):
        return
    menu_clase(salones[opc-1])
