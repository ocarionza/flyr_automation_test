def foo_bar(n: int) -> None:
    """
    Imprime 'Foo', 'Bar', 'FooBar', o el número dado según las reglas:
    - 'Foo' si el número es divisible por 3.
    - 'Bar' si el número es divisible por 5.
    - 'FooBar' si el número es divisible por ambos 3 y 5.
    - El número mismo si no cumple ninguna de las condiciones anteriores.

    Args:
    n (int): Número entero positivo a evaluar.
    """
    if n % 3 == 0 and n % 5 == 0:
        print("FooBar")
    elif n % 3 == 0:
        print("Foo")
    elif n % 5 == 0:
        print("Bar")
    else:
        print(n)

def main():
    """
    Función principal que obtiene una entrada del usuario y llama a foo_bar().
    Valida que la entrada sea un número entero positivo.
    """
    try:
        n = int(input("Introduce un número entero positivo: "))
        if n > 0:
            foo_bar(n)
        else:
            print("Por favor, ingresa un número entero positivo.")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")

if __name__ == "__main__":
    main()
