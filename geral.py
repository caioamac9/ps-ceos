#Ressalva: sou do segundo semestre e ainda estou aprendendo sobre complexidade de algoritmos na cadeira, perdoem algum erro :)
#QUESTÃO 1
def lerarquivo(nomearquivo): #LENDO O ARQUIVO E TRANSFORMANDO EM MATRIZ
    matriz = []
    with open(nomearquivo, 'r') as arquivo:
        for linha in arquivo:
            linhamatriz = [int(x) for x in linha.strip().split()]
            if len(linhamatriz) != 0:
                matriz.append(linhamatriz)
            else:
                continue
    arquivo.close()
    return matriz

#QUESTÃO 2
#a complexidade desse algoritmo depende do numero n de linhas e m de elementos, podendo ser representado por O(n*m)
def EncontraeZera(matriz): 
    elementos = []
    rep = []
    for linha in matriz:
        for elemento in linha:
            if elemento not in elementos: #SE É A PRIMEIRA OCORRENCIA DE UM VALOR, ELE PARA LISTA REFERENCIA
                elementos.append(elemento)
            else:
                rep.append(elemento) # AQUI, UM VALOR JÁ FOI CONTABILIZADO EM ELEMENTOS, LOGO, ELE É REPETIDO.

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] in rep: # AQUI, SE UM X DA MATRIZ FOR UM NUMERO REPETIDO, ELE SERÁ ZERADO
                matriz[i][j] = 0          
    return matriz

#QUESTÃO 3
def ImprimirMatriz(matriz):
    for linha in matriz:
        print(linha)

#ÚTIL
def preencherLista():
    lista = []
    print('Quando desejar finalizar a lista, digite uma letra.')
    while True:
        elemento = input('digite um valor: ')
        if elemento.isalpha()== True:
            break
        else:
            lista.append(int(elemento))
    return lista

#QUESTÃO 5
#aqui temos o insertion sort, que, no pior dos casos, possui complexidade O(n*n)
def ordenarlista(lista):
    for i in range(1, len(lista)): #AQUI ORGANIZAMOS ATRAVES DO METODO INSERTION SORT, REALIZANDO UMA ESPECIE DE ORDENAÇÃO DE 'SUB-LISTAS'
        valor = lista[i]
        j = i - 1
        while j >= 0 and valor < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = valor
    return lista

#QUESTÃO 6
#aqui, a complexidade segue a do metodo de ordenar, visto que preencher lista e comparar elementos tem complexidades mais baixas, O(n) e O(1)
def MenoreseMaiores():
    while True:
        lista1 = preencherLista()
        lista2 = preencherLista()
        if len(lista1) != len(lista2): #AQUI FAZEMOS DO CONTROLE DO TAMANHO DAS LISTAS
            print('!!!Por favor, faça listas de mesmo tamanho n!!!')
            continue
        else:
            listacontrole = lista1 + lista2
            ordenarlista(listacontrole)
            listamenor = listacontrole[:len(lista1)]
            listamaior = listacontrole [len(lista1):len(listacontrole)]
            if listamenor[-1] == listamaior[0]:
                print('\nNessa configuração, os elementos de L2 não podem ser estritamente maiores, tente uma nova! ')
                continue
            else:
                break
    return listamenor, listamaior

#QUESTÃO 7:
#aqui, a complexidade segue a do metodo de ordenar, visto que preencher lista e comparar elementos tem complexidades mais baixas, O(n) e O(1)
#o tempo do algoritmo é um reflexo da complexidade.
def verificarpermutação():
    while True:
        lista1 = preencherLista()
        lista2 = preencherLista()
        lista1a = lista1[:] #AQUI FAZEMOS UMA COPIA DAS LISTAS PARA QUE POSSAMOS MANIPULÁ-LAS
        lista2a = lista2[:]
        erro = 0
        if len(lista1) != len(lista2): #AQUI FAZEMOS DO CONTROLE DO TAMANHO DAS LISTAS
            print('!!!Por favor, faça listas de mesmo tamanho n!!!')
            continue
            
        else:
            lista1ord = ordenarlista(lista1a)
            lista2ord = ordenarlista(lista2a)
            for x in range(len(lista1)):
                if lista1ord[x] != lista2ord[x]: #EM LISTAS ORDENADAS, PODEMOS COMPARAR LINEARMENTE SE CADA FATOR NA POSICAO X É IGUAL
                    erro+=1                      #CASO NÃO SEJA, RODA-SE A VARIAVEL DE ERRO, APONTANDO QUE NÃO SAO LISTAS PERMUTADAS
                elif lista1 == lista2:           #AQUI ANALISAMOS SE POSSUI ORDEM DIFERENTE
                    erro+=1

        if erro == 0:
            resposta = print('L2 é permutação')
        else:     
            resposta = print('L2 NÃO é permutação')
        return resposta

    
#PROGRAMA MATRIZ

nomearquivo = 'testematriz.txt'  # NOME DO ARQUIVO DE TEXTO
matriz = lerarquivo(nomearquivo)
matriz = EncontraeZera(matriz)
ImprimirMatriz(matriz) 

#PROGRAMA LISTAS

print('\nVamos receber uma lista e, em seguida, fornecer o terceiro maior elemento.')
while True:
    listaX = preencherLista()
    if len(listaX) <3:
        continue
    else:
        ordenarlista(listaX)
        print('O terceiro maior elemento é', listaX[-3])
        break

print('\nAgora faremos uma lista ter seus elementos menores que a outra.')
print('\nL1 e L2, respectivamente: ', MenoreseMaiores())

print('\nAgora, verificaremos a PERMUTAÇÃO de duas listas.')
verificarpermutação()

