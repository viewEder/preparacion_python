"""Módulo que contiene la clase PQRSF"""


class PQRSF:
    """Clase que representa una PQRSF"""

    def __init__(self, motivo, descripcion, fecha_hora_recepcion, usuario):
        self.motivo = motivo
        self.descripcion = descripcion
        self.fecha_hora_recepcion = fecha_hora_recepcion
        self.usuario = usuario

    def a_dict(self):
        """Devuelve un diccionario con los datos de la PQRSF"""
        return {
            "motivo": self.motivo,
            "descripcion": self.descripcion,
            "fecha_hora_recepcion": self.fecha_hora_recepcion,
            "usuario": self.usuario.a_dict(),
        }
