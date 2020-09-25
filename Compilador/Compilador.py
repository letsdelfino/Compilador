
Tabela_de_Transição = [
    [1, 9, None, 10, None, 7, None, 0, 0, 0, 17, 19, 13, 13, 13, 13, 14, 15, 16, 18, 9, 9, None],
    [1, None, None, None, None, None, 2, None, None, None, None, None, None, None, None, None, None, None, None, None,
     4, 4, None],
    [3, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None],
    [3, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, 4, 4, None],
    [6, None, None, None, None, None, None, None, None, None, None, None, 5, 5, None, None, None, None, None, None,
     None, None, None],
    [6, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None],
    [6, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None],
    [7, 7, 7, 7, 7, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None],
    [9, 9, 9, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 9,
     9, None],
    [10, 10, 10, 10, 11, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, 18, 20, None, None, None, None, None, None, 18,
     None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     18, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None]

]

alfabeto = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0,
            'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 21, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1,
            'n': 1, 'o': 1, 'p': 1, 'q': 1, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1,
            'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 20, 'F': 1, 'G': 1, 'H': 1, 'I': 1, 'J': 1, 'K': 1, 'L': 1, 'M': 1,
            'N': 1, 'O': 1, 'P': 1, 'Q': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 1, 'W': 1, 'X': 1, 'Y': 1, 'Z': 1,
            '_': 2,
            '{': 3,
            '}': 4,
            '"': 5,
            '.': 6,
            ' ': 7,
            '\t': 8,
            '\n': 9,
            '<': 10,
            '>': 11,
            '-': 12,
            '+': 13,
            '*': 14,
            '/': 15,
            '(': 16, 
            ')': 17,
            ';': 18,
            '=': 19,
            ':': 22,
            '\\': 23
            }

# Aqui é especificado os estados finais to autômato e o tipo de lexema que é gerado nesse estado final
tipos_estados_finais = {
    1: 'num',
    3: 'num',
    6: 'num',
    8: 'literal',
    9: 'id',
    11: 'comentario',
    12: 'EOF',  # ifm de arquivo
    13: 'opm',
    14: 'ab_p',  # abre parêntese
    15: 'fc_p',  # fehca parêntese
    16: 'pt_v',  # ponto e vírgulo
    17: 'opr',
    18: 'opr',  # operador
    19: 'opr',
    20: 'opr',
    21: "Erro"
}

# aqui é listado o token e como ele é visto no arquivo. Ex: inicio no arquivo pode ser lido como inicio
tabela_token_part1 = {
    'inicio': 'inicio',
    'varinicio': 'varinicio',
    'varfim': 'varfim',
    'escreva': 'escreva',
    'leia': 'leia',
    'se': 'se',
    'entao': 'entao',
    'fimse': 'fimse',
    'fim': 'fim',
    'inteiro': 'inteiro',
    'lit': 'lit',
    'real': 'real'
}

# aqui é listado o tipo de cada token, completando o dicionário tabela_token_part1
tabela_token_part2 = {
    'inicio': None,
    'varinicio': None,
    'varfim': None,
    'escreva': None,
    'leia': None,
    'se': None,
    'entao': None,
    'fimse': None,
    'fim': None,
    'inteiro': 'inteiro',
    'lit': 'literal',
    'real': 'double'
}


def scanner(conteudo, length):
    estadoatual = 0
    aux = 0
    ponteiro = 0
    lexema = ""

    while(ponteiro != length):

        a = Tabela_de_Transição[estadoatual][alfabeto[conteudo[aux]]]
        
        if a is None:
            
            estadoatual = 0
            print("Token --> ", lexema)
            lexema = ""
            
        else:
            
            if ((a == 0) and (conteudo[aux] == "\n" or conteudo[aux] == "\t" or conteudo[aux] == " ")):
                
                None
            
            else: 
                
                lexema = lexema + conteudo[aux]
            
            if(ponteiro == (length - 1)):

                print("Token --> ", lexema)
                lexema = ""

            estadoatual = a
            aux += 1
            ponteiro += 1
            
            
        
            
    

def main():
    
    # Faz a leitura do arquivo "fonte.tct"
    file = open('c:/Users/humbe/Desktop/fonte.txt', 'r')

    if file:
        print("Arquivo Encontrado")
    else:
        print("Arquivo não encontrado")

    conteudo = file.read()
    length = len(conteudo)

    scanner(conteudo, length)

    file.close()


main()
