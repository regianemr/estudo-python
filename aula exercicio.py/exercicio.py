entrada = input ('Digite um número : ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'impar'
    if par_impar: 
        par_impar_texto = 'par'
        print (f'O numero {entrada_int} é {par_impar_texto}')
else:
    print('Voce não digitou um numero inteiro')
   
entrada = input ('Digite uma hora em numeros inteiros: ')
try:
    hora = int (entrada)
    if hora >= 0 and hora <= 11:
        print ('Bom dia')

    elif hora >=12 and hora <=17:
        print ('Boa tarde')

    elif hora >=18 and hora <= 23:
        print ('Boa noite')

    else:
        print('nao conheço essa hora')

except:
    print ('digite apenas números inteiros')
