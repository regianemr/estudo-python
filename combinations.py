# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import combinations, permutations, product
def print_inter (iterator):
    print (*list(iterator), sep='\n')
    print() #só para quebrar a linha


pessoas = [
    'João', 'Luiz', 'Joana', 'Maria',
]

camisetas = [                                  
    ['Preta', 'Branca'],
    ['p', 'm','g'],
    ['masculino', 'feminino'],
    ['algodão', 'poliester']
]

# print_inter (combinations(pessoas, 2))
# print_inter (permutations(pessoas, 2))
print_inter (product(*camisetas))