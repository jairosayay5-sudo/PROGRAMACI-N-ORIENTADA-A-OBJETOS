# sistema_reservas.py

# Clase que representa una habitación de hotel
class Habitacion:
    def __init__(self, numero, tipo, precio):
        # Atributos de instancia
        self.numero = numero          # Número de habitación
        self.tipo = tipo              # Tipo (simple, doble, suite)
        self.precio = precio          # Precio por noche
        self.disponible = True        # Estado de disponibilidad

    def reservar(self):
        """Marca la habitación como no disponible si está libre."""
        if self.disponible:
            self.disponible = False
            print(f"Habitación {self.numero} reservada correctamente.")
        else:
            print(f"Habitación {self.numero} ya está ocupada.")

    def liberar(self):
        """Marca la habitación como disponible de nuevo."""
        if not self.disponible:
            self.disponible = True
            print(f"Habitación {self.numero} liberada correctamente.")
        else:
            print(f"Habitación {self.numero} ya estaba libre.")

    def mostrar_info(self):
        """Muestra los datos básicos de la habitación."""
        estado = "Disponible" if self.disponible else "Ocupada"
        print(f"Habitación {self.numero} | Tipo: {self.tipo} | "
              f"Precio: {self.precio} | Estado: {estado}")


# Clase que gestiona un conjunto de habitaciones (sistema de reservas)
class SistemaReservas:
    def __init__(self, nombre_hotel):
        # Atributo de instancia que guarda una lista de habitaciones
        self.nombre_hotel = nombre_hotel
        self.habitaciones = []  # Lista de objetos Habitacion

    def agregar_habitacion(self, habitacion):
        """Agrega una habitación al sistema."""
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones(self):
        """Muestra la información de todas las habitaciones."""
        print(f"=== Habitaciones del hotel {self.nombre_hotel} ===")
        for hab in self.habitaciones:
            hab.mostrar_info()

    def reservar_habitacion(self, numero):
        """Busca una habitación por número e intenta reservarla."""
        for hab in self.habitaciones:
            if hab.numero == numero:
                hab.reservar()
                return
        print(f"No se encontró la habitación {numero}.")

    def liberar_habitacion(self, numero):
        """Busca una habitación por número e intenta liberarla."""
        for hab in self.habitaciones:
            if hab.numero == numero:
                hab.liberar()
                return
        print(f"No se encontró la habitación {numero}.")


# Bloque principal para probar la interacción entre objetos
if __name__ == "__main__":
    # Crear un sistema de reservas (objeto de la clase SistemaReservas)
    sistema = SistemaReservas("Hotel Amazonía")

    # Crear algunas habitaciones (objetos de la clase Habitacion)
    hab1 = Habitacion(101, "Simple", 25.0)
    hab2 = Habitacion(102, "Doble", 40.0)
    hab3 = Habitacion(201, "Suite", 80.0)

    # Agregar las habitaciones al sistema
    sistema.agregar_habitacion(hab1)
    sistema.agregar_habitacion(hab2)
    sistema.agregar_habitacion(hab3)

    # Mostrar todas las habitaciones
    sistema.mostrar_habitaciones()

    # Reservar y liberar habitaciones para demostrar la interacción
    sistema.reservar_habitacion(101)
    sistema.reservar_habitacion(101)  # Intento de reservar de nuevo
    sistema.liberar_habitacion(101)
    sistema.mostrar_habitaciones()
