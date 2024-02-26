import Persona
class cliente(Persona):
    def __init__(self):
        super()
        self.nit

    def crear_cliente(self, nombre, apellido, direccion, telefono, fecha_nacimiento):
        print("Se crea una persona")

    def leer_cliente(self):
        print("Se lee el listado de personas")

    def actualizar_cliente(self, nombre, apellido, direccion, telefono, fecha_nacimiento):
        print("Se actualiza una persona")

    def borra_cliente(self):
        print("Se borra una persona")