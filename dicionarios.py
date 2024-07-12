meu_dicionario = {
    1: "Python",
    2: "Java",
    3: "PHP"
}

print(type(meu_dicionario))

valor = meu_dicionario.get(1)
print(valor)

tamanho = len(meu_dicionario)
print(tamanho)

dicionario_frutas = {
    1: {"nome": "limão", "tipo": "ácida"},
    2: {"nome": "laranja", "tipo": "ácida"},
    3: {"nome": "manga", "tipo": "semiácida"},
    4: {"nome": "maça", "tipo": "semiácida"},
    5: {"nome": "banana", "tipo": "doce"},
    6: {"nome": "mamão", "tipo": "doce"}
}

print(dicionario_frutas)

nome_fruta = dicionario_frutas[1]["nome"]
tipo_fruta = dicionario_frutas[1]["tipo"]

print("Nome:", nome_fruta)
print("Tipo:", tipo_fruta)

nome_fruta = dicionario_frutas[2]["nome"]
tipo_fruta = dicionario_frutas[2]["tipo"]

print("Nome:", nome_fruta)
print("Tipo:", tipo_fruta)

for chave, valor in dicionario_frutas.items():
    nome_fruta = valor["nome"]
    tipo_fruta = valor["tipo"]
    print("Fruta:", nome_fruta, "- Tipo:", tipo_fruta)