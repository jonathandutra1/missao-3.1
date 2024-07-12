set_inicial = {11, 12, 13, 14}

print(set_inicial)

set_inicial.add(15)

print(set_inicial)

set_inicial.update([1, 2, 3, 4, 5]) 

print(set_inicial)

set_inicial.discard(13)

print(set_inicial)

novo_set = set([20, 21, 23, 1, 2])

print(novo_set)

uniao = set_inicial | novo_set
print("União:", uniao)

intersecao = set_inicial & novo_set
print("Interseção:", intersecao)

diferenca = set_inicial - novo_set
print("Diferença:", diferenca)

diferenca_simetrica = set_inicial ^ novo_set
print("Diferença simétrica:", diferenca_simetrica)