def sumar_todos(*args):
    resultado = 0
    for numero in args:
        resultado += numero
    return resultado
print(sumar_todos(1, 2, 3, 4, 5))  # Output: 15