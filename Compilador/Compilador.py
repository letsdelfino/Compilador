# Dicionário de dados: No Python, os dicionários são coleções de itens desordenados com uma diferença bem grande quando comparados às
# outras coleções (lists, sets, tuples, etc): um elemento dentro de um dicionário possui uma chave atrelada a ele, uma espécie de
# identificador. Sendo assim, é muito utilizado quando queremos armazenar dados de forma organizada e que possuem identificação
# única (como acontece em bancos de dados). Basicamente são tabelas hash.
# Fonte: https://www.treinaweb.com.br/blog/principais-estruturas-de-dados-no-python/

# Implementando o dicionário de dados

# cada linha da tabela de transição corresponde a um estado começando em q0. As colunas representam as transições.
# Visualização _|D|L|.|.....
#             q0|  |  |  |....
#             q1|  |  |  |.....

Tabela_de_Transição = [
    [1, 9, None, 10, None, 7, None, 0, 12, 0, 0, 17, 19, 13, 13, 13, 13, 14, 15, 16, 12, 21, None, None, None],  # 0
    [1, None, None, None, None, None, 2, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, 4, 4],  # 1
    [3, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None, None, None],  # 2
    [3, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None, 4, 4],  # 3
    [6, None, None, None, None, None, None, None, None, None, None, None, None, 5, 5, None, None, None, None, None,
     None, None, None, None, None],  # 4
    [6, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None, None, None],  # 5
    [6, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None, None, None],  # 6
    [7, 7, 7, 7, 7, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],  # 7
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None, None, None],  # 8
    [9, 9, 9, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None, None],  # 9
    [10, 10, 10, 10, 11, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],  # 10
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None, None, None],  # 11
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None, None, None],  # 12
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None, None, None],  # 13
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None, None, None],  # 14
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None, None, None],  # 15
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None, None, None],  # 16
    [None, None, None, None, None, None, None, None, None, None, None, None, 18, 20, None, None, None, None, None, None,
     18, None, None, None, None],  # 17
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None, None, None],  # 18
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, 18, None, None, None, None],  # 19
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None, None, None],  # 20
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None, None, None]  # 21
]

# o que se encontra entre '' na deifinição do alfabeto é o caracter lido no arquivo txt "fonte.txt." que se encontra na mesma pasta deste que este código. Já o número que se encontra
# após ':' é a coluna correspondente ao caracter lido. Os número se encontram na coluna 0 da tabela, enquanto o alfabeto se encontra na coluna 1.
# os demais caracteres como '>', '<', etc possuem cada um uma coluna para si.
# Desta forma quando lemos o caracter entre '' o programa vê o valor da coluna correspondente. Ambos serão usados mais a frente na função scanner

alfabeto = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0,
            'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 21, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1,
            'n': 1, 'o': 1, 'p': 1, 'q': 1, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1,
            'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 21, 'F': 1, 'G': 1, 'H': 1, 'I': 1, 'J': 1, 'K': 1, 'L': 1, 'M': 1,
            'N': 1, 'O': 1, 'P': 1, 'Q': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 1, 'W': 1, 'X': 1, 'Y': 1, 'Z': 1,
            '_': 2,
            '{': 3,
            '}': 4,
            '"': 5,
            '.': 6,
            ' ': 7,
            'eof': 8,
            '\t': 9,
            '\n': 10,
            '<': 11,
            '>': 12,
            '-': 13,
            '+': 14,
            '*': 15,
            '/': 16,
            '(': 17,
            ')': 18,
            ';': 19,
            '=': 20,
            }

tipos_estados_finais = {
    1:'num',
    3:'num',
    6:'num',
    8:'literal',
    9:'id',
    11:'comentario',
    12:'EOF', #ifm de arquivo
    13:'opm',
    14:'ab_p', #abre parêntese
    15:'fc_p', #fehca parêntese
    16:'pt_v', #ponto e vírgulo
    17:'opr',
    18:'opr', #operador
    19:'opr',
    20:'opr',
    21:"Erro"
    }

def scanner(conteudo):
    string = len(conteudo)
    estado = 0

    # Momentaniamente está fazendo a leitura de caracter por caracter, identificando o estado atual e o próximo estado dentro da
    # tabela de transição
    
    for i in range(string):
        a = Tabela_de_Transição[estado][alfabeto[conteudo[i]]]
        print("Posição: ", a)
        print("Caracter: ", conteudo[i])
        print("Estado: ", estado)
        if (a == None):
            estado = 0
        else:
            estado = a


def main():

    # Faz a leitura do arquivo "fonte.tct"
    file = open('fonte.txt', 'r')

    if (file):
        None
    else:
        print("Arquivo não encontrado")

    conteudo = file.read()
    scanner(conteudo)
    file.close()


main()