def LeituraArquivo(NomeArqui):
  try:
      with open(NomeArqui, 'r') as arquivo:
          linhas = arquivo.readlines()
          num = int(linhas[0])
          operacoes = []
          for i in range(1, len(linhas), 3):
              tipo = linhas[i].strip()
              conj1 = set(linhas[i+1].strip().split(','))
              conj2 = set(linhas[i+2].strip().split(','))

              conj1 = {elemento.strip() for elemento in conj1}
              conj2 = {elemento.strip() for elemento in conj2}

              operacoes.append((tipo, conj1, conj2))
          return operacoes
  except FileNotFoundError:
      print(f"Arquivo '{NomeArqui}' não encontrado.")
      return []

def Operacoes(operacoes):
  resultados = []
  for tipo, conj1, conj2 in operacoes:
      if tipo == 'U':
          resultado = Uniao(conj1, conj2)
      elif tipo == 'I':
          resultado = Intersec(conj1, conj2)
      elif tipo == 'C':
          resultado = ProdutoCarte(conj1, conj2)
      elif tipo == 'D':
          resultado = Diferen(conj1, conj2)
      else:
          print(f"Operação inválida: {tipo}")
          continue
      resultados.append((tipo, conj1, conj2, resultado))
  return resultados

def Uniao(conjunto1, conjunto2):
  return conjunto1.union(conjunto2)

def Intersec(conjunto1, conjunto2):
  return conjunto1.intersection(conjunto2)

def ProdutoCarte(conjunto1, conjunto2):
  resultado = [(x, y) for x in conjunto1 for y in conjunto2]
  return resultado

def Diferen(conjunto1, conjunto2):
  return conjunto1.difference(conjunto2)

def Saida(resultados):
  for tipo, conj1, conj2, resultado in resultados:
      if tipo == 'C':
          resultado_str = "[" + ", ".join([f"({x}, {y})" for x, y in resultado]) + "]"
      else:
          resultado_str = "{" + ", ".join(map(str, sorted(resultado))) + "}"
      print(f"{tipo}: Conjunto 1 {{{', '.join(conj1)}}}, Conjunto 2 {{{', '.join(conj2)}}}, Resultado {resultado_str}")
  print("----------------------------------------------")

NomeArqui = input("Digite o nome do arquivo: (Exemplo: ExerciBase.txt) ")
operacoes = LeituraArquivo(NomeArqui)
if operacoes:
  resultados = Operacoes(operacoes)
  Saida(resultados)
