"""Modulo que contiene la clase Usuario"""


class Usuario:
    """Clase que representa a un usuario de la aplicación"""

    def __init__(
        self, nombre_completo, fecha_nacimiento, pais, ciudad, email, telefono
    ):
        self.nombre_completo = nombre_completo
        self.fecha_nacimiento = fecha_nacimiento
        self.pais = pais
        self.ciudad = ciudad
        self.email = email
        self.telefono = telefono

    def a_dict(self):
        """Devuelve un diccionario con los datos del usuario"""
        return {
            "nombre_completo": self.nombre_completo,
            "fecha_nacimiento": self.fecha_nacimiento,
            "pais": self.pais,
            "ciudad": self.ciudad,
            "email": self.email,
            "telefono": self.telefono,
        }

    def __str__(self) -> str:
        return f"""
        Nombre completo: {self.nombre_completo}
        Fecha de nacimiento: {self.fecha_nacimiento}
        País: {self.pais}
        Ciudad: {self.ciudad}
        Email: {self.email}
        Teléfono: {self.telefono}
        """
