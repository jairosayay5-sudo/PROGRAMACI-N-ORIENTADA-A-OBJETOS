"""
Sistema de Gestión de Biblioteca
Demuestra conceptos de POO: Herencia, Encapsulación y Polimorfismo
Autor: Jairo Estiven Sayay Alvarez
Fecha: 18 de enero 2026
"""

# ================== CLASE BASE ==================
class Publicacion:
    """
    Clase base que representa una publicación general en la biblioteca.
    Demuestra ENCAPSULACIÓN mediante atributos privados.
    """
    
    def __init__(self, titulo, autor, año_publicacion):
        # Atributos privados (encapsulación) - se acceden mediante métodos
        self.__titulo = titulo
        self.__autor = autor
        self.__año_publicacion = año_publicacion
        self.__disponible = True
    
    # Métodos getter (para acceder a atributos privados)
    def get_titulo(self):
        """Retorna el título de la publicación"""
        return self.__titulo
    
    def get_autor(self):
        """Retorna el autor de la publicación"""
        return self.__autor
    
    def get_año(self):
        """Retorna el año de publicación"""
        return self.__año_publicacion
    
    def esta_disponible(self):
        """Retorna si la publicación está disponible"""
        return self.__disponible
    
    # Métodos setter (para modificar atributos privados de forma controlada)
    def prestar(self):
        """Marca la publicación como prestada"""
        if self.__disponible:
            self.__disponible = False
            print(f"'{self.__titulo}' ha sido prestado.")
        else:
            print(f"'{self.__titulo}' no está disponible.")
    
    def devolver(self):
        """Marca la publicación como devuelta"""
        self.__disponible = True
        print(f"'{self.__titulo}' ha sido devuelto.")
    
    # Método que será sobrescrito (POLIMORFISMO)
    def mostrar_info(self):
        """Muestra información básica de la publicación"""
        estado = "Disponible" if self.__disponible else "Prestado"
        return f"Título: {self.__titulo}\nAutor: {self.__autor}\nAño: {self.__año_publicacion}\nEstado: {estado}"


# ================== CLASES DERIVADAS (HERENCIA) ==================
class Libro(Publicacion):
    """
    Clase derivada que representa un libro.
    Hereda de Publicacion y añade atributos específicos.
    """
    
    def __init__(self, titulo, autor, año_publicacion, isbn, num_paginas):
        # Llamar al constructor de la clase padre
        super().__init__(titulo, autor, año_publicacion)
        # Atributos específicos de Libro
        self.__isbn = isbn
        self.__num_paginas = num_paginas
    
    def get_isbn(self):
        """Retorna el ISBN del libro"""
        return self.__isbn
    
    def get_paginas(self):
        """Retorna el número de páginas"""
        return self.__num_paginas
    
    # POLIMORFISMO: Sobrescritura del método mostrar_info
    def mostrar_info(self):
        """Muestra información completa del libro"""
        info_base = super().mostrar_info()
        return f"{info_base}\nISBN: {self.__isbn}\nPáginas: {self.__num_paginas}\nTipo: Libro"


class Revista(Publicacion):
    """
    Clase derivada que representa una revista.
    Hereda de Publicacion y añade atributos específicos.
    """
    
    def __init__(self, titulo, autor, año_publicacion, numero_edicion, mes):
        # Llamar al constructor de la clase padre
        super().__init__(titulo, autor, año_publicacion)
        # Atributos específicos de Revista
        self.__numero_edicion = numero_edicion
        self.__mes = mes
    
    def get_edicion(self):
        """Retorna el número de edición"""
        return self.__numero_edicion
    
    def get_mes(self):
        """Retorna el mes de publicación"""
        return self.__mes
    
    # POLIMORFISMO: Sobrescritura del método mostrar_info
    def mostrar_info(self):
        """Muestra información completa de la revista"""
        info_base = super().mostrar_info()
        return f"{info_base}\nEdición: {self.__numero_edicion}\nMes: {self.__mes}\nTipo: Revista"


# ================== CLASE PARA GESTIÓN ==================
class Biblioteca:
    """
    Clase que gestiona la colección de publicaciones.
    Demuestra POLIMORFISMO al trabajar con diferentes tipos de publicaciones.
    """
    
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__catalogo = []  # Lista para almacenar publicaciones
    
    def agregar_publicacion(self, publicacion):
        """Agrega una publicación al catálogo"""
        self.__catalogo.append(publicacion)
        print(f"\n✓ '{publicacion.get_titulo()}' agregado al catálogo.")
    
    def mostrar_catalogo(self):
        """
        Muestra todo el catálogo.
        POLIMORFISMO: cada publicación usa su propio método mostrar_info()
        """
        print(f"\n{'='*50}")
        print(f"CATÁLOGO DE {self.__nombre.upper()}")
        print(f"{'='*50}")
        
        if not self.__catalogo:
            print("El catálogo está vacío.")
        else:
            for i, pub in enumerate(self.__catalogo, 1):
                print(f"\n[{i}] {pub.mostrar_info()}")
                print("-" * 50)
    
    def buscar_por_titulo(self, titulo):
        """Busca una publicación por título"""
        for pub in self.__catalogo:
            if titulo.lower() in pub.get_titulo().lower():
                return pub
        return None


# ================== FUNCIÓN PRINCIPAL ==================
def main():
    """
    Función principal que demuestra el uso del sistema.
    """
    print("=" * 60)
    print("SISTEMA DE GESTIÓN DE BIBLIOTECA")
    print("Demostrando Herencia, Encapsulación y Polimorfismo")
    print("=" * 60)
    
    # Crear instancia de Biblioteca
    mi_biblioteca = Biblioteca("Biblioteca Central")
    
    # Crear instancias de Libro (clase derivada)
    libro1 = Libro(
        titulo="Cien Años de Soledad",
        autor="Gabriel García Márquez",
        año_publicacion=1967,
        isbn="978-0307474728",
        num_paginas=417
    )
    
    libro2 = Libro(
        titulo="Don Quijote de la Mancha",
        autor="Miguel de Cervantes",
        año_publicacion=1605,
        isbn="978-8420412146",
        num_paginas=863
    )
    
    # Crear instancias de Revista (clase derivada)
    revista1 = Revista(
        titulo="National Geographic",
        autor="Varios autores",
        año_publicacion=2026,
        numero_edicion=156,
        mes="Enero"
    )
    
    revista2 = Revista(
        titulo="Scientific American",
        autor="Varios autores",
        año_publicacion=2025,
        numero_edicion=328,
        mes="Diciembre"
    )
    
    # Agregar publicaciones al catálogo
    mi_biblioteca.agregar_publicacion(libro1)
    mi_biblioteca.agregar_publicacion(libro2)
    mi_biblioteca.agregar_publicacion(revista1)
    mi_biblioteca.agregar_publicacion(revista2)
    
    # Mostrar catálogo completo (POLIMORFISMO en acción)
    mi_biblioteca.mostrar_catalogo()
    
    # Demostrar operaciones de préstamo (ENCAPSULACIÓN)
    print("\n" + "=" * 60)
    print("DEMOSTRANDO OPERACIONES DE PRÉSTAMO")
    print("=" * 60)
    
    print("\n--- Intentando prestar un libro ---")
    libro1.prestar()
    
    print("\n--- Intentando prestar el mismo libro nuevamente ---")
    libro1.prestar()
    
    print("\n--- Devolviendo el libro ---")
    libro1.devolver()
    
    print("\n--- Prestando el libro nuevamente ---")
    libro1.prestar()
    
    # Demostrar búsqueda
    print("\n" + "=" * 60)
    print("DEMOSTRANDO BÚSQUEDA")
    print("=" * 60)
    
    titulo_buscar = "Quijote"
    print(f"\nBuscando: '{titulo_buscar}'")
    resultado = mi_biblioteca.buscar_por_titulo(titulo_buscar)
    
    if resultado:
        print("\n¡Encontrado!")
        print(resultado.mostrar_info())
    else:
        print("\nNo se encontró la publicación.")
    
    print("\n" + "=" * 60)
    print("FIN DE LA DEMOSTRACIÓN")
    print("=" * 60)


# ================== EJECUCIÓN DEL PROGRAMA ==================
if __name__ == "__main__":
    main()