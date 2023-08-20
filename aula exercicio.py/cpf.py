#calculo cpf 
#gerador de cpf 159.671.370-41
#Colete a soma dos 9 primeiros digitos do cpf
"""
Calculo do primeiro dígito do CPF
CPF: 159.671.370-41
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  159.671.370-41 (159671370
   10  9  8  7  6  5  4  3  2
*  1   5  9  6  7  1  3  7  0
   10  45 72 42 42 5 12 21 0
Somar todos os resultados: 
10+45+72+42+42+5+12+21+0= 249
Multiplicar o resultado anterior por 10
249 * 10 = 2490
Obter o resto da divisão da conta anterior por 11
2490 % 11 = 4
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 4
"""
#calculo do segundo dígito do CPF
#"CPF: 159.671.370-41
#Colete a soma dos 9 primeiros dígitos do CPF,
#MAIS O PRIMEIRO DIGITO,
#multiplicando cada um dos valores por uma
#contagem regressiva começando de 11

import random

for _ in range (100):
    nove_digitos = ''
    for i in range (9):
        nove_digitos += str (random.randint(0, 9))


    contador_regressivo_1 = 10

    resultado_digito_1 = 0

    for digito in nove_digitos:
      resultado_digito_1 += int(digito) * contador_regressivo_1
      contador_regressivo_1 -= 1 
    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0 
  

    dez_digitos = nove_digitos + str (digito_1)
    contador_regressivo_2 = 11

    resultado_digito_2 = 0

    for digito in dez_digitos:
      resultado_digito_2 += int(digito) * contador_regressivo_2
      contador_regressivo_2 -= 1
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

print (cpf_gerado_pelo_calculo)