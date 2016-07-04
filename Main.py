# -*- coding: latin1 -*-
'''
Essa função gerará um numero de mintermos
correspondente à variável numero_de_mintermos
E cada mintermo terá um numero de bits corre-
pondente à variável numero_de_bits.

A metodologia de geração será gerar n numero
de bits, com o numero de mintermos especifi-
cado, e coloca-los em uma matriz. Depois os
mintermos serão verificados para identificar
mintermos coincidentes, se houver algum ele
será apagado e substituido por outro, e o
processo continuará até o fim da matriz.
O processo será repetido ate que todos os
mintermos sejam diferentes uns dos outros.
'''
from random import *
import os
randBinList = lambda n: [str(randint(0,1)) for b in range(1,n+1)]
printmatriz = lambda n: [print(i) for i in n]


def geramintermo(numero_de_bits, numero_de_mintermos):
    matriz_de_mintermos = []
    for i in range(int(numero_de_mintermos)):
        b = randBinList(numero_de_bits)
        while b in matriz_de_mintermos:
            b = randBinList(numero_de_bits)
        matriz_de_mintermos.append(b)
    for i in range(len(matriz_de_mintermos)):
        matriz_de_mintermos[i] = ''.join(matriz_de_mintermos[i])
    matriz_de_mintermos = sorted(matriz_de_mintermos)
    printmatriz(matriz_de_mintermos)

while True:
    os.system('cls')
    a = input("deseja gerar mintermos aleatorios (1) ou inserir mintermos? (2)")    
    os.system('cls')
    if a == "2":
        while True:
            try:
                os.system('cls')
                numero_de_bits = int(input("Digite o numero de bits de cada min termo\n"))
                numero_de_mintermos = int(input("Digite o numero de mintermos!\n"))
                os.system('cls')
                if (numero_de_mintermos) >= (2**numero_de_bits):
                    raise ValueError
                matriz = [[] for i in range(numero_de_mintermos)]
                for i in range(numero_de_mintermos):
                    while True:
                        os.system('cls')
                        valor_mintermo = input("digite o mintermo %d!\n"%(i+1))
                        os.system('cls')
                        if (valor_mintermo.isdigit() == True) and (("2" or "3" or "4" or"5" or"6"or "7"or"8" or "9") in valor_mintermo) == False:
                            matriz[i] = valor_mintermo
                            break
                printmatriz(matriz)
                break
            except ValueError:
                print("ERRO. Tente novamente! \n")
                os.system('cls')
        break
    elif a == "1":
        while True:
            try:
                numero_de_bits = int(input("Digite o numero de bits de cada min termo\n"))
                numero_de_mintermos = int(input("Digite o numero de mintermos!\n"))
                os.system('cls')
                if (numero_de_mintermos) >= (2**numero_de_bits):
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Seu jumento digita direito!\n")
                os.system('cls')
        geramintermo(numero_de_bits,numero_de_mintermos)
        break
