def suma_cuadrados_digitos(n: int) -> int:
    """
    Calcula la suma de los cuadrados de los dígitos de un número.

    Args:
    n (int): El número entero positivo.

    Returns:
    int: La suma de los cuadrados de los dígitos.
    """
    return sum(int(digit) ** 2 for digit in str(n))

def es_numero_feliz(n: int) -> bool:
    """
    Determina si un número es un "número feliz".
    Un número es feliz si al reemplazarlo repetidamente por la suma de los cuadrados
    de sus dígitos se llega al número 1, de lo contrario, es un número infeliz.

    Args:
    n (int): El número entero positivo a verificar.

    Returns:
    bool: True si el número es feliz, False si no lo es.
    """
    visitados = set()  # Usamos un conjunto para detectar ciclos

    while n != 1 and n not in visitados:
        visitados.add(n)
        n = suma_cuadrados_digitos(n)

    return n == 1

def main():
    """
    Función principal que obtiene una entrada del usuario, verifica si es un número feliz
    y muestra el resultado.
    """
    try:
        n = int(input("Introduce un número entero positivo: "))
        if n > 0:
            if es_numero_feliz(n):
                print(f"{n} es un número feliz.")
            else:
                print(f"{n} no es un número feliz.")
        else:
            print("Por favor, ingresa un número entero positivo.")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")

if __name__ == "__main__":
    main()
