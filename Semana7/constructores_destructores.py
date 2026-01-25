"""
Tarea: Constructores y Destructores en Python
Estudiante: Jairo Estiven Sayay Alvarez 
Fecha: 24 Enero 2026

Este programa demuestra cómo funcionan los constructores y destructores en Python
"""


class Libro:
    """
    Clase que representa un libro.
    Muestra el uso básico de constructor y destructor.
    """
    
    def __init__(self, titulo, autor, paginas):
        """
        Constructor: Se ejecuta cuando creamos un nuevo libro.
        Aquí inicializamos los datos del libro.
        """
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        
        # Mensaje que confirma que el objeto fue creado
        print(f"Libro creado: '{self.titulo}' de {self.autor}")
    
    def mostrar_info(self):
        """Muestra la información del libro"""
        print(f"\nTítulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Páginas: {self.paginas}")
    
    def __del__(self):
        """
        Destructor: Se ejecuta cuando el objeto va a ser eliminado.
        Python lo llama automáticamente.
        """
        print(f"Libro eliminado: '{self.titulo}'")


class Estudiante:
    """
    Clase que representa un estudiante.
    """
    
    def __init__(self, nombre, edad, carrera):
        """
        Constructor: Inicializa los datos del estudiante.
        """
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.materias = []
        
        print(f"\nEstudiante registrado: {self.nombre}")
    
    def agregar_materia(self, materia):
        """Agrega una materia a la lista del estudiante"""
        self.materias.append(materia)
        print(f"Materia '{materia}' agregada para {self.nombre}")
    
    def mostrar_datos(self):
        """Muestra todos los datos del estudiante"""
        print(f"\n--- Datos del Estudiante ---")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Carrera: {self.carrera}")
        print(f"Materias: {self.materias}")
    
    def __del__(self):
        """
        Destructor: Se ejecuta al eliminar el estudiante.
        """
        print(f"Estudiante {self.nombre} eliminado del sistema")


class CuentaBancaria:
    """
    Clase que representa una cuenta bancaria simple.
    """
    
    def __init__(self, titular, saldo_inicial):
        """
        Constructor: Crea una nueva cuenta bancaria.
        """
        self.titular = titular
        self.saldo = saldo_inicial
        
        print(f"\nCuenta bancaria creada para: {self.titular}")
        print(f"Saldo inicial: ${self.saldo}")
    
    def depositar(self, cantidad):
        """Deposita dinero en la cuenta"""
        self.saldo += cantidad
        print(f"Depósito de ${cantidad}. Nuevo saldo: ${self.saldo}")
    
    def retirar(self, cantidad):
        """Retira dinero de la cuenta"""
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro de ${cantidad}. Nuevo saldo: ${self.saldo}")
        else:
            print("Saldo insuficiente")
    
    def __del__(self):
        """
        Destructor: Se ejecuta al cerrar la cuenta.
        """
        print(f"\nCuenta de {self.titular} cerrada. Saldo final: ${self.saldo}")


# PROGRAMA PRINCIPAL
print("=" * 50)
print("DEMOSTRACIÓN DE CONSTRUCTORES Y DESTRUCTORES")
print("=" * 50)

# Ejemplo 1: Usando la clase Libro
print("\n--- EJEMPLO 1: LIBROS ---")
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 417)
libro2 = Libro("Don Quijote", "Miguel de Cervantes", 863)

libro1.mostrar_info()
libro2.mostrar_info()

# Eliminar un libro manualmente (esto llama al destructor)
print("\nEliminando libro1...")
del libro1

# Ejemplo 2: Usando la clase Estudiante
print("\n--- EJEMPLO 2: ESTUDIANTES ---")
estudiante1 = Estudiante("Juan Pérez", 20, "Ingeniería en Sistemas")
estudiante1.agregar_materia("Programación")
estudiante1.agregar_materia("Matemáticas")
estudiante1.mostrar_datos()

estudiante2 = Estudiante("Ana García", 19, "Diseño Gráfico")
estudiante2.agregar_materia("Photoshop")
estudiante2.mostrar_datos()

# Ejemplo 3: Usando la clase CuentaBancaria
print("\n--- EJEMPLO 3: CUENTA BANCARIA ---")
cuenta = CuentaBancaria("Carlos Rodríguez", 1000)
cuenta.depositar(500)
cuenta.retirar(300)
cuenta.depositar(200)

print("\n" + "=" * 50)
print("FIN DEL PROGRAMA")
print("Los destructores de los objetos restantes")
print("se ejecutarán automáticamente ahora...")
print("=" * 50)

# Cuando el programa termina, Python llama automáticamente
# a los destructores de todos los objetos que aún existen