nomes_alunos =(["maria", "ana", "joão", "Félix", "agatha","joaquim"])
matriculas_alunos =([26, 101, 13, 5,37, 72])


notas = [None] * len(nomes_alunos)  

notas[0] = [8,7,5,9]  # Notas da Maria
notas[1] = [9, 9, 8, 9]  # Notas da Ana
notas[2] = [6, 5, 5, 5]  # Notas do João
notas[3] = [10, 8, 8, 8]  # Notas do Félix
notas[4] = [8, 6, 7.5, 9]  # Notas da agatha
notas[5] = [6, 5.5, 5, 7]  # Notas do joaquim


def calcular_media(notas_aluno):

  return sum(notas_aluno) / len(notas_aluno) 

def verificar_reprovado(notas_aluno):

  return calcular_media(notas_aluno) < 6

def identificar_reprovados(nomes_alunos, notas):

  reprovados = []
  for i in range(len(nomes_alunos)):
    if verificar_reprovado(notas[i]):
      reprovados.append((nomes_alunos[i], notas[i]))
  return reprovados



medias = [calcular_media(notas_aluno) for notas_aluno in notas] 
print("Médias dos alunos:")
for nome, media in zip(nomes_alunos, medias):
  print(f"{nome}: {media:.2f}")


reprovados = identificar_reprovados(nomes_alunos, notas)


if reprovados:
  print("\nAlunos reprovados:")
  for nome, notas_aluno in reprovados:
    print(f"Nome: {nome}, Notas: {notas_aluno}, Média: {calcular_media(notas_aluno):.2f}")
else:
  print("\nNenhum aluno foi reprovado.")