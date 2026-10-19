# =============================================================
# Portada
# =============================================================
# Nombre: Carlos Armando Muñoz Bustamante
# Matrícula: 2630017
# Grupo: IM-1-3

# =============================================================
# Resúmen Ejecutivo
# =============================================================
# Tuplas (Tuple) y listas (List) son dos de los cuatro tipos de datos incorporados 
# que puedes usar en Python para almacenar colecciones de datos. Los diccionarios en Python 
# son una estructura de datos que permite almacenar su contenido en forma de llave y valor.
# Las listas son mutables, o sea que puedes agregar, eliminar o modificar elementos después de
# su creación, mientra que las tuplas son inmutables, eso quiere decir que no se pueden 
# modificar después de su creación. Los diccionarios en Python asocian claves con valores, así
# permitiendo guardar y buscar información mediante una clave única.
# descripción de cada problema, diseño de entradas y salidas, validaciones aplicadas 
# y uso de listas, tuplas y diccionarios en contextos prácticos 
# (por ejemplo, catálogos, registros, estadísticas).

# =============================================================
# Principios y buenas prácticas
# =============================================================
# - Usar listas cuando necesites agregar o eliminar elementos con frecuencia.
# - Usar tuplas para datos que no deben cambiar (por ejemplo, coordenadas, fechas, configuraciones fijas).
# - Usar diccionarios cuando necesites buscar información por una clave (por ejemplo, por nombre, id, código).
# - Evitar modificar una lista mientras la recorres con un for, a menos que sepas exactamente lo que haces.
# - Usar nombres de claves descriptivos en los diccionarios (por ejemplo, "name", "age", "price").
# - Escribir código legible y mensajes claros para el usuario.

# =============================================================
# Problema 1: Shopping list basics (list operations)
# =============================================================
# Description: 
# El programa permite crear y administrar una lista de compras, agregando productos, 
# consultando los artículos guardados y eliminando productos cuando sea necesario.
# Inputs:
# - Nombre del producto que se desea agregar.
# - Opción del menú: agregar, consultar, eliminar o salir.
# - Nombre del producto que se desea eliminar.
# Outputs:
# - Confirmación de que un producto fue agregado o eliminado.
# - Lista de productos guardados.
# - Mensajes de error si el producto no existe o la opción no es válida.
# - Mensaje de despedida al salir.
# Validations: 
# Verificar que el nombre del producto no esté vacío.
# Comprobar que la opción del menú sea válida.
# Verificar que el producto exista antes de eliminarlo.
# Evitar errores al intentar eliminar productos de una lista vacía.
# Test cases: 
# 1. Normal: Input: "apple,banana,orange", New item: "grapes", Search: "banana"
#    Expected Output: Items list: ['apple', 'banana', 'orange', 'grapes']
#    Total items: 4
#    Found item: true

# 2. Border: Input: "apple", New item: "banana", Search: "banana"
#    Expected Output: Items list: ['apple', 'banana']
#    Total items: 2
#    Found item: true

# 3. Error: Input: "   ", New item: "banana", Search: "apple"
#    Expected Output: Error: invalid input

print("Problem 1: Shopping list basics")
initial_items_text = input("Enter initial products separated by commas: ").strip()

if not initial_items_text:
    print("Error: initials list cannot be empty")
else:
    items_list = [item.strip() for item in initial_items_text.split(",") if item.strip()]
    new_item = input("Enter a new product: ").strip()

    if not new_item:
        print("Error: new product cannot be empty")
    else: 
        items_list.append(new_item)
        len_list = len(items_list)
        search_time = input("Enter a product to search: ").strip()

        if not search_time:
            print("Error: search product cannot be empty")
        else:
            is_in_list = search_time in items_list

            print(f"Items list: {items_list}")
            print(f"Total items: {len_list}")
            print(f"Found item: {str(is_in_list).lower()}")

# =============================================================
# Problema 2: Points and distances with tuples
# =============================================================
# Descripción:
# El programa guarda dos puntos mediante tuplas, calcula la distancia
# entre ellos y muestra las coordenadas y el resultado.
# Inputs:
# x1: coordenada X del primer punto (float).
# y1: coordenada Y del primer punto (float).
# x2: coordenada X del segundo punto (float).
# y2: coordenada Y del segundo punto (float).
# Outputs:
# Point 1: coordenadas del primer punto.
# Point 2: coordenadas del segundo punto.
# Distance: distancia entre ambos puntos.
# Validations:
# Verificar que las coordenadas sean números válidos.
# Usar try-except para manejar entradas no numéricas.
# Guardar las coordenadas de cada punto en una tupla.
# Calcular correctamente la distancia entre los dos puntos.
# Test cases:
# 1. Punto (0, 0) y punto (3, 4): distancia esperada = 5.0.
# 2. Punto (2, 2) y punto (2, 2): distancia esperada = 0.0.
# 3. Punto (-1, -1) y punto (2, 3): distancia esperada = 5.0.

print("Problem 2: Points and distances whit tuples")

try: 
    x1 = float(input("Enter x coordinate of point 1: "))
    y1 = float(input("Enter y coordinate of point 1: "))

    x2 = float(input("Enter x coordinate of point 2: "))
    y2 = float(input("Enter y coordinate of point 2: "))

    point1 = (x1, y1)
    point2 = (x2, y2)
    
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    print(f"Point 1: {point1}")
    print(f"Point 2: {point2}")
    print(f"Distance: {distance}")

except ValueError:
    print("Error: invalid input")

# =============================================================
# Conclusión
# =============================================================
# En conclusion las listas nos convienen cuando necesitamos almacenar colecciones 
# de datos que pueden cambiar en un futuro. Permiten agregar elementos con 
# append() y eliminarlos con remove(). También facilitan recorrer y modificar 
# los elementos de una colección.
# Las tuplas son útiles para guardar datos que no deben modificarse, como las coordenadas.
# Una vez creadas, las tuplas no se puede cambiar sus datos.
# Las listas son más flexibles, mientras que las tuplas mantienen los datos constantes.
# El patrón es que ambas nos permiten organizar, almacenar y organizar información de 
# una forma sencilla.

# =============================================================
# Referencias
# =============================================================
# freeCodeCamp - Tuple vs List en Python: ¿Cuál es la diferencia?
# https://www.freecodecamp.org/espanol/news/tuple-vs-list-en-python-cual-es-la-diferencia/
#
# El Libro de Python - Diccionarios en Python.
# https://ellibrodepython.com/diccionarios-en-python
#
# Stack Overflow en español - ¿Cuál es la diferencia entre una tupla y una lista en Python?
# https://es.stackoverflow.com/questions/415447/cu%C3%A1l-es-la-diferencia-entre-una-tupla-y-una-lista-en-python
#
# Python Software Foundation - Tutorial de Python 3.11: Estructuras de datos.
# https://docs.python.org/es/3.11/tutorial/datastructures.html
#
# Python Software Foundation - Python Tutorial: Data Structures.
# https://docs.python.org/3/tutorial/datastructures.html