
'''
Essa função gerará um numero de mintermos correspondente à variável
numero_de_mintermos E cada mintermo terá um numero de bits corre-
pondente à variável numero_de_bits.

A metodologia de geração será gerar n numero de bits, com o numero de
mintermos especificado, e coloca-los em uma matriz. Depois os
mintermos serão verificados para identificar mintermos coincidentes, se
houver algum ele será apagado e substituido por outro, e o processo
continuará até o fim da matriz. O processo será repetido ate que todos
os mintermos sejam diferentes uns dos outros.
'''

import classificar
import os


while True:
    while True:
        '''os.system('clear')'''
        a = input(".:::Deseja gerar mintermos aleatorios (1) ou inserir mintermos? (2)")
        '''os.system('clear')'''
        if a == "1":
            while True:
                try:
                    numero_de_bits = int(input(".:::Digite o numero de bits de cada min termo\n"))
                    numero_de_mintermos = int(input(".:::Digite o numero de mintermos!\n"))
                    '''os.system('clear')'''
                    if (numero_de_mintermos) >= (2**numero_de_bits):
                        raise ValueError
                    else:
                        break
                except ValueError:
                    print(".:::Erro de digitação. Tente novamente!\n")
                    '''os.system('clear')'''
            matriz_primaria = []
            matriz_primaria = classificar.geramintermo(numero_de_bits,numero_de_mintermos)
            classificar.printmatriz(matriz_primaria)
            break
        elif a == "2":
            while True:
                try:
                    #A parte de inserir a matriz está ok
                    '''os.system('clear')'''
                    numero_de_bits = int(input(".:::Digite o numero de bits de cada min termo\n"))
                    numero_de_mintermos = int(input(".:::Digite o numero de mintermos!\n"))
                    '''os.system('clear')'''
                    if (numero_de_mintermos) >= (2**numero_de_bits):
                        raise ValueError
                    matriz_primaria = []
                    sentinel = '' # ends when this string is seen
                    for line in iter(input, sentinel):
                        matriz_primaria.append(line)
                    #Até aqui tudo rodando
                    #os valores são inseridos e a matriz sai perfeitamente.
                    matriz_agrupada = classificar.classificar_grupos(matriz_primaria)
                    classificar.QuineMcCluskey(matriz_agrupada)
                    break
                except ValueError:
                    print("ERRO. Tente novamente! \n")
                    '''os.system('clear')'''
            break


    a = input(".:::Digite 0 e pressione Enter para sair ou digite qualquer coisa e pressione Enter e para continuar")
    if a == "0":
        break
