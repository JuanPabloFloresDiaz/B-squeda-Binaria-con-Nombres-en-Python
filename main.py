# Importar las clases necesarias para validaciones y entrada de datos
from Teclado import Teclado
from Validaciones import Validaciones

def busqueda_binaria(lista, nombre):
    """
    Realiza búsqueda binaria en una lista ordenada de nombres.
    
    Args:
        lista (list): Lista ordenada de nombres
        nombre (str): Nombre a buscar
    
    Returns:
        int: Posición del nombre si se encuentra, -1 si no se encuentra
    """
    inicio = 0
    fin = len(lista) - 1
    
    while inicio <= fin:
        medio = (inicio + fin) // 2
        
        # Comparación insensible a mayúsculas y minúsculas
        if lista[medio].lower() == nombre.lower():
            return medio  # posición encontrada
        elif nombre.lower() < lista[medio].lower():
            fin = medio - 1
        else:
            inicio = medio + 1
    
    return -1  # no encontrado

def mostrar_menu():
    """Muestra el menú principal del programa"""
    print("\n" + "="*50)
    print("    BÚSQUEDA BINARIA DE NOMBRES")
    print("="*50)
    print("1. Buscar un nombre")
    print("2. Mostrar lista de nombres")
    print("3. Salir del programa")
    print("="*50)

def mostrar_lista_nombres(nombres):
    """Muestra la lista de nombres con sus posiciones"""
    print("\nLISTA DE NOMBRES DISPONIBLES:")
    print("-" * 40)
    for i, nombre in enumerate(nombres):
        print(f"{i:2d}. {nombre}")
    print("-" * 40)
    print(f"Total de nombres: {len(nombres)}")

def buscar_nombre(nombres):
    """Función para buscar un nombre en la lista"""
    print("\nBÚSQUEDA DE NOMBRES")
    print("-" * 30)
    
    # 3. Pedir al usuario que ingrese un nombre con validaciones
    nombre_buscado = Teclado.read_text(
        "Ingrese el nombre a buscar:",
        min_length=2,
        max_length=50
    )
    
    # Realizar la búsqueda binaria
    posicion = busqueda_binaria(nombres, nombre_buscado)
    
    print(f"\nRESULTADO DE LA BÚSQUEDA:")
    print("-" * 35)
    
    # 4. Mostrar si existe y la posición
    if posicion != -1:
        print(f"¡Nombre encontrado!")
        print(f"Nombre: {nombres[posicion]}")
        print(f"Posición: {posicion}")
        print(f"(Posición {posicion + 1} si contamos desde 1)")
    else:
        # 5. Mostrar mensaje claro si no existe
        print(f"El nombre '{nombre_buscado}' no se encontró en la lista.")
        print("Verifique la ortografía o consulte la lista de nombres disponibles.")

def main():
    """Función principal del programa"""
    # 1. Declarar lista con 10 nombres desordenados
    nombres = [
        "Carlos", "Ana", "Pedro", "Lucía", "María", 
        "Jorge", "Sofía", "Luis", "Elena", "Miguel",
        "Valeria", "Andrés", "Camila", "Diego", "Isabella"
    ]
    
    print("Lista original (desordenada):")
    print(nombres)
    
    # 2. Ordenar la lista
    nombres.sort()
    print("\nLista ordenada alfabéticamente:")
    print(nombres)
    
    # 6. Permitir realizar varias búsquedas sin reiniciar el programa
    while True:
        try:
            # 9. Mostrar el menú en cada iteración
            mostrar_menu()
            
            # 7. Utilizar validaciones para asegurar entrada correcta
            opcion = Teclado.read_integer(
                "Seleccione una opción:",
                min_value=1,
                max_value=3
            )
            
            if opcion == 1:
                buscar_nombre(nombres)
                
            elif opcion == 2:
                mostrar_lista_nombres(nombres)
                
            elif opcion == 3:
                # 10. Permitir salir del programa
                print("\n¡Gracias por usar el programa de búsqueda binaria!")
                print("Programa finalizado correctamente.")
                break
                
        except KeyboardInterrupt:
            # 8. Manejar errores y casos especiales
            print("\n\nPrograma interrumpido por el usuario.")
            print("¡Hasta luego!")
            break
        except Exception as e:
            # 8. Manejar errores inesperados
            print(f"\nError inesperado: {e}")
            print("El programa continuará ejecutándose...")

# Punto de entrada del programa
if __name__ == "__main__":
    main()