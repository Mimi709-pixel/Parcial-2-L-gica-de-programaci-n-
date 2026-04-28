# --- ESTRUCTURAS DE DATOS ---

# Tupla con horarios disponibles (no cambian)
HORARIOS = ("15:00", "18:00", "21:00")

# Lista de diccionarios con películas y sus datos (precio y sala)
cartelera = [
    {"id": 1, "titulo": "Avatar: El Camino del Agua", "precio": 10.0, "sala": 1},
    {"id": 2, "titulo": "Spider-Man: Across the Spider-Verse", "precio": 8.5, "sala": 2},
    {"id": 3, "titulo": "Oppenheimer", "precio": 12.0, "sala": 3},
]

# --- FUNCIONES ---

def mostrar_cartelera():
    """Muestra las películas disponibles con sus precios."""
    print("\n--- 🎬 CARTELERA CINE 🎬 ---")
    for pelicula in cartelera:
        print(f"[{pelicula['id']}] {pelicula['titulo']} - ${pelicula['precio']} (Sala {pelicula['sala']})")
    print("----------------------------")

def comprar_boletas():
    """Gestiona el proceso de compra de boletas."""
    mostrar_cartelera()
    
    try:
        # Selección de película
        id_pelicula = int(input("\nSeleccione el número de la película que desea ver: "))
        pelicula_seleccionada = None
        for p in cartelera:
            if p['id'] == id_pelicula:
                pelicula_seleccionada = p
                break
        
        if not pelicula_seleccionada:
            raise ValueError("Película no disponible.")

        # Selección de cantidad
        cantidad = int(input(f"¿Cuántas boletas para '{pelicula_seleccionada['titulo']}' desea? "))
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero.")

        # Procesar compra
        total = pelicula_seleccionada['precio'] * cantidad
        print(f"\n✅ Compra exitosa: {cantidad} boleta(s) para {pelicula_seleccionada['titulo']}.")
        print(f"💰 Total a pagar: ${total:.2f}")

    except ValueError as e:
        print(f"\n❌ Error: {e}. Por favor intente de nuevo con números válidos.")
    except Exception as e:
        print(f"\n❌ Ocurrió un error inesperado: {e}")

# --- PROGRAMA PRINCIPAL ---

def main():
    while True:
        print("\n=== BIENVENIDO AL SISTEMA DE CINE ===")
        print("1. Ver Cartelera y Comprar")
        print("2. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            comprar_boletas()
        elif opcion == "2":
            print("¡Gracias por usar nuestro sistema!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()