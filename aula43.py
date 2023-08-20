# # Operadores in e not in
# nome = input ('Digite seu nome: ')
# encontrar = input ('Digite o que quer encontrar: ')
# if encontrar in nome:
#     print (f'{encontrar} está em {nome}')
# else: 
#     print(f'{encontrar} não está em {nome}')



# """
# Fatiamento de strings
#  012345678
#  Olá mundo
# -987654321
# Fatiamento [i:f:p] [::]
# Obs.: a função len retorna a qtd 
# de caracteres da str
# """
# variavel = 'Olá mundo'
# print(variavel[0:5])

#print([1, 2, 3][::-1])
#print('amor'[::-1] == 'roma')

#def isPalindrome(word1, word2):
 #   return word1[::-1] == word2

#print(isPalindrome('papel', 'cabeça'))
#print(isPalindrome('asa', 'asa'))

"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
