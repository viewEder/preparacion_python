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

    def __str__(self) -> str:
        return f"""
        --- PQRSF ---
        Motivo: {self.motivo}
        Descripción: {self.descripcion}
        Fecha y hora de recepción: {self.fecha_hora_recepcion}
        --- Usuario --- {self.usuario}
        """
