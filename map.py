def dobrar(x):
    return x * 2

lista = [1, 2, 3, 4, 5]
resultado = map(dobrar, lista)

# Converter o resultado em uma lista
lista_dobrada = list(resultado)

print(lista_dobrada)