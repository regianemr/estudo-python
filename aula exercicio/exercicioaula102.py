# def multiplicar (*args):
#     total = 1
#     for numero in args:
#         total *= numero
#     return total
    
# multiplicacao= multiplicar (1,2,3,4,5,6)
# print (multiplicacao)


# def par_impar (numero):
#     divisivel_por_dois = numero % 2 == 0 

#     if divisivel_por_dois:
#         return f'{numero} é par'
    
#     return f'{numero} é ímpar'
    
# print (par_impar(2))
# print (par_impar(15))

# Pessoa = {}

# chave = 'nome'
# Pessoa [chave] = 'Regiane'
 
# print (Pessoa [chave])


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
qtn_acertos = 0

for pergunta in perguntas:
    print ('Pergunta:', pergunta ['Pergunta'])

    print ()

    opcoes = pergunta ['Opções']
    for i, opcao in enumerate(opcoes):
        print (f'{i})', opcao)

    print ()

escolha = input('Escolha uma opção: ')

acertou = False
escolha_int = None
qtd_opcoes = len (opcoes)

if escolha.isdigit():
    escolha_int = int(escolha)

if escolha_int is not None:
    if escolha_int >= 0 and escolha_int < qtd_opcoes:
        if opcoes [escolha_int] == pergunta ['Resposta']:
            acertou = True
if acertou: 
    qtn_acertos +=1
    print ('Acertou')    
else: 
    print ('Errou')  

print ()
   
print ('Você acertou', qtn_acertos)
print ('de', len(perguntas), 'perguntas.')