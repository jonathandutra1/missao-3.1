dicionario = {
    1: {'nome': 'Maria', 'idade': 26, 'nacionalidade': 'brasileira'}
}

print(dicionario)

novos_elementos = {
    2: {'nome': 'João', 'idade': 30, 'nacionalidade': 'brasileiro'},
    3: {'nome': 'Ana', 'idade': 22, 'nacionalidade': 'portuguesa'}
}

dicionario.update(novos_elementos)

print(dicionario)

novo_dicionario = dicionario.copy()

print("Dicionário original:", dicionario)
print("Novo dicionário (cópia):", novo_dicionario)

elemento_removido = dicionario.pop(1)
print("Elemento removido:", elemento_removido)

print("Dicionário após a remoção:", dicionario)

chave, valor = dicionario.popitem()
print("Elemento removido (chave, valor):", chave, valor)

print("Dicionário após a remoção:", dicionario)

dicionario.clear()
print("Primeiro dicionário após a remoção:", dicionario)

novo_dicionario.clear()
print("Segundo dicionário após a remoção:", novo_dicionario)

chaves = ['nome', 'idade', 'cidade']

novo_dicionario = dict.fromkeys(chaves)

print("Itens do dicionário:", novo_dicionario.items())

print("Chaves do dicionário:", novo_dicionario.keys())

print("Valores do dicionário:", novo_dicionario.values())