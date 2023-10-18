# valor_1 = input('Digite um valor: ')
# valor_2 = input('Digite outro valor: ')

# if valor_1 > valor_2:

#     print (f'{valor_1} é maior do que {valor_2}')

# else:
#     print (f'{valor_2} é maior do que {valor_1}')


# primeiro_valor = input('Digite um valor: ')
# segundo_valor = input('Digite outro valor: ')


# if primeiro_valor >= segundo_valor:
#     print(
#         f'{primeiro_valor=} é maior ou igual '
#         f'ao que {segundo_valor=}'
#     )
# else:
#     print(
#         f'{segundo_valor=} é maior '
#         f'do que {primeiro_valor=}'
#     )

#nome = input('Digite seu nomen: ')
#idade = input('Digite sua idade: ')

#if nome and idade: 
#    print(f'O seu nome é {nome}')
#   print(f'O seu nome invertido é {nome[::-1]}')
#if ' ' in nome:
 #   print('Seu nome contém espaços')
#else:
 #   print(f'Seu nome não contém espaços')

#print(f'Seu nome tem {len(nome)} letras')
#print(f'A primeira letra do seu nome é {nome[0]}')
#print(f'A ultima letra do seu nome é {nome[-1]}')

velocidade = 50
local_carro= 100

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

if velocidade > RADAR_1:
    print('Velocidade ultrapassou a velocidade permitida')
if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and \
    velocidade > RADAR_1:
    print ('Carro multado')
if velocidade < RADAR_1:
    print('Passagem ok')




    