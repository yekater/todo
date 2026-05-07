def unir_palabras(**valores):
    print(valores)
    print(type(valores))

    print(kwvalores)
    print(type(kwvalores))

    total = a + b
    for n in valores:
        if type(n) in (int, float):
            total += n
    
    claves_str = " "
    texto_str = " "
    for k, v in valores.items():
        if type(k) == str:
            claves_str += k + ", "
        else:
            pass
        if type(v) == str:
            texto_str += v + ", "
        else:
            pass
    return claves_str, texto_str

print(unir_palabras())
exit()