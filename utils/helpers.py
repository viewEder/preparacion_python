"""Módulo con funciones auxiliares para el programa."""
import datetime
import json
import os
from usuario import Usuario
from pqrsf import PQRSF

# Obtener la ruta absoluta del directorio actual
DIRECTORIO_ACTUAL = "/".join(os.getcwd().split("/")[:-1])


def obtener_datos_usuario():
    """Obtiene los datos de un usuario y devuelve una instancia de Usuario."""
    print("Ingrese los datos del usuario:")
    nombre_completo = input("Nombre completo: ")
    while not nombre_completo:
        print("El nombre completo no puede estar vacío.")
        nombre_completo = input("Nombre completo: ")

    fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
    while not fecha_nacimiento or not fecha_nacimiento.strip():
        print("La fecha de nacimiento no puede estar vacía.")
        fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")

    try:
        datetime.datetime.strptime(fecha_nacimiento, "%Y-%m-%d").date()
    except ValueError:
        print("Formato de fecha incorrecto. Debe ser YYYY-MM-DD.")
        return obtener_datos_usuario()

    pais = input("País: ")
    ciudad = input("Ciudad: ")

    email = input("Email: ")
    while not email or not email.strip() or "@" not in email:
        print("El email no puede estar vacío y debe ser válido.")
        email = input("Email: ")

    telefono = input("Teléfono: ")
    while not telefono or not telefono.strip():
        print("El teléfono no puede estar vacío.")
        telefono = input("Teléfono: ")

    return Usuario(nombre_completo, fecha_nacimiento, pais, ciudad, email, telefono)


def obtener_datos_pqrsf(usuario):
    """Obtiene los datos de una PQRSF y devuelve una instancia de PQRSF."""
    print("Ingrese los datos del PQRSF:")
    motivo = input("Motivo (P, Q, R, S, F): ")
    while motivo not in {"P", "Q", "R", "S", "F"}:
        print("Motivo inválido. Debe ser P, Q, R, S o F.")
        motivo = input("Motivo (P, Q, R, S, F): ")

    descripcion = input("Descripción del problema o solicitud: ")
    while not descripcion:
        print("La descripción no puede estar vacía.")
        descripcion = input("Descripción del problema o solicitud: ")

    # Obtener fecha y hora actual
    fecha_hora_recepcion = datetime.datetime.now()

    pqrsf = PQRSF(
        motivo, descripcion, fecha_hora_recepcion.strftime("%Y-%m-%d"), usuario
    )
    return pqrsf


def cargar_pqrsf_desde_archivo():
    """Carga los PQRSF desde el archivo y devuelve una lista de instancias de PQRSF."""
    try:
        with open(f"{DIRECTORIO_ACTUAL}/files/pqrsf.json", "r") as archivo:
            pqrsf_data = json.load(archivo)
            pqrsf_list = [
                PQRSF(
                    item["motivo"],
                    item["descripcion"],
                    item["fecha_hora_recepcion"],
                    Usuario(
                        item["usuario"]["nombre_completo"],
                        item["usuario"]["fecha_nacimiento"],
                        item["usuario"]["pais"],
                        item["usuario"]["ciudad"],
                        item["usuario"]["email"],
                        item["usuario"]["telefono"],
                    ),
                )
                for item in pqrsf_data
            ]
        return pqrsf_list
    except FileNotFoundError:
        return []


# Nueva función para guardar los PQRSF en el archivo
def guardar_pqrsf_en_archivo(pqrsf_list):
    """Guarda los PQRSF en el archivo."""
    with open(f"{DIRECTORIO_ACTUAL}/files/pqrsf.json", "w") as archivo:
        pqrsf_data = [pqrsf.a_dict() for pqrsf in pqrsf_list]
        json.dump(pqrsf_data, archivo, indent=4)


# Función para agregar un nuevo PQRSF a la lista y guardarlo en el archivo
def agregar_pqrsf():
    """Agergar pqrsf a archivos"""
    usuario = obtener_datos_usuario()
    pqrsf = obtener_datos_pqrsf(usuario)
    pqrsf_list = cargar_pqrsf_desde_archivo()
    pqrsf_list.append(pqrsf)
    guardar_pqrsf_en_archivo(pqrsf_list)
    return True


def mostrar_pqrsf():
    """Mostrar pqrsf"""
    pqrsf_list = cargar_pqrsf_desde_archivo()
    for pqrsf in pqrsf_list:
        print(pqrsf)
