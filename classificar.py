from random import *

#essa função imprime uma matriz qualquer, linha a linha
printmatriz = lambda n: [print(i) for i in n]

def verificar0ou1(valor_qualquer, tamanho):
    ''' Essa função verifica se a variavel valor_qualquer é composta de zeros ou uns e se tem o tamanho especificado'''
    if (valor_qualquer.isdigit() == True) and ((("2" or "3" or "4" or "5" or "6" or "7" or "8" or "9") in valor_qualquer)== False) and len(valor_qualquer) == tamanho:
        return True
    else:
        return False

def geramintermo(numero_de_bits, numero_de_mintermos):
    randBinList = lambda n: [str(randint(0,1)) for b in range(1,n+1)]
    matriz_de_mintermos = []
    for i in range(int(numero_de_mintermos)):
        b = randBinList(numero_de_bits)
        while b in matriz_de_mintermos:
            b = randBinList(numero_de_bits)
        matriz_de_mintermos.append(b)
    for i in range(len(matriz_de_mintermos)):
        matriz_de_mintermos[i] = ''.join(matriz_de_mintermos[i])
    matriz_de_mintermos = sorted(matriz_de_mintermos)
    for i in range(len(matriz_de_mintermos)):
        matriz_de_mintermos[i] = str(matriz_de_mintermos[i])
    #printmatriz(matriz_de_mintermos)
    return matriz_de_mintermos

def retornacolunas(matriz,coluna):
	y = []
	y.append(x[coluna] for x in matriz)
	return y

def classificar_grupos(matriz):
	'''essa função converte uma lista unidimensional para uma bidimensional
	na qual a segunda coluna contem os grupos

	entrada: matriz Nx1
	saída: matriz Nx2 com:
		   matriz_agrupada[i][0] = mintermo i
		   matriz_agrupada[i][1] = grupo no qual o mintermo i está contido'''

	grupos = []
	for item in matriz:
		indice = item.count('1')
		if (indice in grupos) == False:
			grupos.append(indice)
	grupos.sort()
	matriz_agrupada = []
	for i in range(len(matriz)):
		matriz_agrupada.append([matriz[i], matriz[i].count('1')])

	matriz_agrupada = sorted(matriz_agrupada, key = lambda matriz_agrupada: matriz_agrupada[1])


	return matriz_agrupada


def Xor(string, string2):
	saida = ''
	for i in range(len(string)):
		if string[i] == string2[i]:
			saida.append('-')
		else:
			saida.append('1')
	return saida


def QuineMcCluskey(matriz):
	''' essa função executa a minimização propriamente dita.

	entrada: uma matriz do tipo matriz_agrupada
	saída: a lista de implicantes primos'''
	matriz_saida = []
	grupos=[]
	for i in range(len(matriz)):
		if matriz[i][1] not in grupos:
			grupos.append(matriz[i][1])
	if grupos != []:
		for i in grupos:
			if retornacolunas(matriz,1).count(i) == 1:
				print("Hey, implicante primo {0}".format(matriz[matriz.index(i)]))
	printmatriz(grupos)
