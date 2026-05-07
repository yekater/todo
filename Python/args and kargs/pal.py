def suma(a=0, b=0, *valores, **kwvalores):
    # Печатаем входные данные для наглядности
    print(f"--- Вызов функции: a={a}, b={b}, valores={valores}, kwargs={kwvalores} ---")

    # 1. Считаем сумму чисел
    total = a + b
    for n in valores:
        if isinstance(n, (int, float)):
            total += n

    # 2. Собираем ключи и строковые значения из kwargs
    claves_list = []
    texto_list = []
    
    for k, v in kwvalores.items():
        # В kwargs ключи всегда строки
        claves_list.append(str(k))
        
        # Добавляем в текст только если значение — строка
        if isinstance(v, str):
            texto_list.append(v)
            
    # Соединяем списки в строки через запятую
    claves_str = ", ".join(claves_list)
    texto_str = ", ".join(texto_list)
            
    return total, claves_str, texto_str

# Проверки:
print("Результат 1:", suma()) 
# Вернет: (0, '', '')

print("Результат 2:", suma(10, 30)) 
# Вернет: (40, '', '')

print("Результат 3:", suma(10, 30, 5, 15, 20)) 
# Вернет: (80, '', '')

print("Результат 4 (с текстом):", suma(1, 2, 3, x="Hola", y="Mundo")) 
# Вернет: (6, 'x, y', 'Hola, Mundo')