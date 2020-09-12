#Dicionário de dados: No Python, os dicionários são coleções de itens desordenados com uma diferença bem grande quando comparados às 
#outras coleções (lists, sets, tuples, etc): um elemento dentro de um dicionário possui uma chave atrelada a ele, uma espécie de 
#identificador. Sendo assim, é muito utilizado quando queremos armazenar dados de forma organizada e que possuem identificação 
#única (como acontece em bancos de dados). Basicamente são tabelas hash. 
#Fonte: https://www.treinaweb.com.br/blog/principais-estruturas-de-dados-no-python/

#Implementando o dicionário de dados

#cada linha da tabela de transição corresponde a um estado começando em q0. As colunas também representam estados e começam pelo estado q0.
#Visualização _|q0|q1|q2|.....
#             q0|  |  |  |....
#             q1|  |  |  |.....

Ttabela_transicao = [
   #|q0|q1|q2|q3|q4|q5....|21|
  [1, None, None, None, None, None, None, 7, None, 9, 10, None, 12, 13, 14, 15, 16, None, None, 19, None, 21], #0
  [None, 1, 2, None, 4, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], #1
  [None, None, None, 3, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], #2
  [None, None, None, 3, 4, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], #3
  [None, None, None, None, None, 5, 6, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], #4
  [None, None, None, None, None, None, 6, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], #5
  [None, None, None, None, None, None, 6, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], #6
  [None, None, None, None, None, None, None, 7, 8, None, None, None, None, None, None, None, None, None, None, None, None, None], #7
  [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], #8
  [None, None, None, None, None, None, None, None, None, 9, None, None, None, None, None, None, None, None, None, None, None, None], #9
  [None, None, None, None, None, None, None, None, None, None, 10, 11, None, None, None, None, None, None, None, None, None, None], #10
  [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], #11
  [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], #12
  [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], #13
  [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], #14
  [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], #15 
  [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],#16
  [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 18, None, 20, None], #17
  [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], #18
  [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 18, None, None, None], #19
  [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], #20
  [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], #21
]

def main():
  file = open('fonte.txt', 'r')

  if (file):
      None
  else:
    print("Arquivo não encontrado")

  conteudo = file.read()
  print(conteudo)

  file.close()
 
main()