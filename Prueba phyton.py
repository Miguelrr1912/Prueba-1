class Agenda:
    def __init__(self):
        self.contactos = {}

    def agregar_contacto(self, nombre, telefono, email):
        self.contactos[nombre] = {"telefono": telefono, "email": email}
        print(f"Contacto {nombre} agregado correctamente.")

    def buscar_contacto(self, nombre):
        if nombre in self.contactos:
            print(f"Nombre: {nombre}\nTeléfono: {self.contactos[nombre]['telefono']}\nEmail: {self.contactos[nombre]['email']}")
        else:
            print("Contacto no encontrado.")

    def eliminar_contacto(self, nombre):
        if nombre in self.contactos:
            del self.contactos[nombre]
            print(f"Contacto {nombre} eliminado correctamente.")
        else:
            print("Contacto no encontrado.")

    def mostrar_contactos(self):
        if self.contactos:
            print("Lista de contactos:")
            for nombre, info in self.contactos.items():
                print(f"- {nombre}: {info['telefono']}, {info['email']}")
        else:
            print("No hay contactos en la agenda.")


def menu():
    agenda = Agenda()
    while True:
        print("\n--- Agenda de Contactos ---")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Eliminar contacto")
        print("4. Mostrar todos los contactos")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            agenda.agregar_contacto(nombre, telefono, email)
        elif opcion == "2":
            nombre = input("Ingrese el nombre a buscar: ")
            agenda.buscar_contacto(nombre)
        elif opcion == "3":
            nombre = input("Ingrese el nombre a eliminar: ")
            agenda.eliminar_contacto(nombre)
        elif opcion == "4":
            agenda.mostrar_contactos()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
