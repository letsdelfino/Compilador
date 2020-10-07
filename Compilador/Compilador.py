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
    [1, 9, None, 10, None, 7, None, 0, 0, 0, 17, 19, 13, 13, 13, 13, 14, 15, 16, 18, 9, 9, None, None],
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

# o que se encontra entre '' na deifinição do alfabeto é o caracter lido no arquivo txt "fonte.txt." que se encontra na mesma pasta deste que este código. Já o número que se encontra
# após ':' é a coluna correspondente ao caracter lido. Os número se encontram na coluna 0 da tabela, enquanto o alfabeto se encontra na coluna 1.
# os demais caracteres como '>', '<', etc possuem cada um uma coluna para si.
# Desta forma quando lemos o caracter entre '' o programa vê o valor da coluna correspondente. Ambos serão usados mais a frente na função scanner

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
estados_finais = {
    1: 'num',
    3: 'num',
    6: 'num',
    8: 'literal',
    9: 'id',
    11: 'comentario',
    12: 'EOF',  # ifm de arquivo
    13: 'opm',
    14: 'ab_p',  # abre parêntese
    15: 'fc_p',  # fecha parêntese
    16: 'pt_v',  # ponto e vírgula
    17: 'opr',
    18: 'opr',  # operador
    19: 'opr',
    20: 'opr',
    21: "Erro"
}

tipo_estados_finais = {
    1: 'inteiro',
    3: 'real',
    6: 'real',
    8: 'literal',
    9: None,
    11: None,
    12: None,  
    13: None,
    14: None,  
    15: None,  
    16: None,  
    17: None,
    18: None,  
    19: None,
    20: None,
    21: None
}

# erros léxicos
estados_erros = {

    0: 'Caminho não reconhecido',
    2: 'Numeral incorreto',
    4: 'Numeral incorreto',
    5: 'Numeral incorreto',
    7: 'Literal incorreto',
    10: 'Comentário Incorreto'

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
    'inteiro': None,
    'lit': None,
    'real': None

}

#Aqui começa qa função que faz o papel de analisador léxico
def scanner(conteudo, length):
    estadoatual = 0
    aux = 0
    ponteiro = 0
    lexema = ""
    linha = 1
    coluna = 1
    
    # Vai percorrer todo o arquivo lendo caracter por acaracter até um espaço vazio. Quando cheganoespaço vazio verifica o tipo e o token do lexema
    # e printa na tela.
    #Quando encontra uma transição não existente dentro da tabela de transição, é exibida a linha e a coluna onde o erro ocorreu, o que gerou o erro e o
    #tipo de erro especificado no dicionário 'erros léxicos'
    while(ponteiro < length):

        if (conteudo[aux] not in alfabeto):
            print("----------------------------------")
            print("Caracter inválido do alfabeto: ", conteudo[aux])
            print("Na linha: ", linha, ". Na coluna: ", coluna)
            print("----------------------------------")
            estadoatual = 0
            ponteiro += 1
            aux += 1
            lexema = ""
        
        else:
            
            a = Tabela_de_Transição[estadoatual][alfabeto[conteudo[aux]]]

            if a is None and estadoatual in estados_finais:
                
                if (estados_finais[estadoatual] != 'id'):
                    saida = "Lexema: " + lexema + "\tToken: " + estados_finais[estadoatual] + "\tTipo: " + str(tipo_estados_finais[estadoatual])
                    print(saida)
                else:
                    if (lexema in tabela_token_part1):
                       saida = "Lexema: " + lexema + "\tToken: " + estados_finais[estadoatual] + "\tTipo: " + str(tabela_token_part2[lexema])
                       print(saida)
                    else:
                       # Quando um id é lido e não está na tabela de símbolos ele é adicionado
                        saida = "Lexema: " + lexema + "\tToken: " + estados_finais[estadoatual] + "\tTipo: " + str(tipo_estados_finais[estadoatual])
                        print(saida)
                        tabela_token_part1[lexema] = estados_finais[estadoatual]
                        tabela_token_part2[lexema] = None
                estadoatual = 0
                lexema = ""
            
            elif (a is None) and (estadoatual not in estados_finais):

                print("----------------------------------")
                print(estados_erros[estadoatual])
                print("Lexema: ", lexema, " Na linha ", linha, "e coluna ", coluna)
                print("----------------------------------")
                estadoatual = 0
                ponteiro += 1
                aux += 1
                coluna += 1
                lexema = ""

            elif (estadoatual == 10 and ponteiro == (length -1)):
                
                print("----------------------------------")
                print(estados_erros[estadoatual])
                print("\nLexema: ", lexema, " \nNa linha ", linha, "e coluna ", coluna)
                print("----------------------------------")
                
                ponteiro += 1

            elif (estadoatual == 7) and ponteiro == (length -1):
                
                print("----------------------------------")
                print(estados_erros[estadoatual])
                print("\nLexema: ", lexema, " \nNa linha ", linha, "e coluna ", coluna)
                print("----------------------------------")
                
                ponteiro += 1

            else:
            
                if ((a == 0) and (conteudo[aux] == "\n" or conteudo[aux] == "\t" or conteudo[aux] == " ")):
                
                    if conteudo[aux] == "\n":

                        linha += 1
                        coluna = 1
            
                else: 
                
                    lexema = lexema + conteudo[aux]
            
                estadoatual = a
                aux += 1
                ponteiro += 1
                coluna += 1
                
            
            
        
            
    

def main():
    
    # Faz a leitura do arquivo "fonte.txt"
    file = open('fonte.txt', 'r')

    if file:
        print("Arquivo Encontrado")
    else:
        print("Arquivo não encontrado")

    conteudo = file.read()

    scanner(conteudo, len(conteudo))
    print("----------Tabela de Símbolos----------")
    print(tabela_token_part1)
    print(tabela_token_part2)
    print("--------------------------------------")
    

    file.close()


main()

