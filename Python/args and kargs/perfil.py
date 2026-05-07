def mostrar_perfil(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
mostrar_perfil(nombre="Juan", edad=30, profesion="Desarrollador")
# Output:
# nombre: Juan
# edad: 30
# profesion: Desarrollador
mostrar_perfil(usuario="Admin", nivel=5)