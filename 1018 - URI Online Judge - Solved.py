# -*- coding: utf-8 -*-

'''
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.

Exemplo de Entrada	    Exemplo de Saída
576                     576
                        5 nota(s) de R$ 100,00
                        1 nota(s) de R$ 50,00
                        1 nota(s) de R$ 20,00
                        0 nota(s) de R$ 10,00
                        1 nota(s) de R$ 5,00
                        0 nota(s) de R$ 2,00
                        1 nota(s) de R$ 1,00

11257                   11257
                        112 nota(s) de R$ 100,00
                        1 nota(s) de R$ 50,00
                        0 nota(s) de R$ 20,00
                        0 nota(s) de R$ 10,00
                        1 nota(s) de R$ 5,00
                        1 nota(s) de R$ 2,00
                        0 nota(s) de R$ 1,00
                        
503                     503
                        5 nota(s) de R$ 100,00
                        0 nota(s) de R$ 50,00
                        0 nota(s) de R$ 20,00
                        0 nota(s) de R$ 10,00
                        0 nota(s) de R$ 5,00
                        1 nota(s) de R$ 2,00
                        1 nota(s) de R$ 1,00
'''

ent = int(input())
print (ent)

n100 = int(ent / 100)
n50 = int((ent - n100 * 100) / 50)
n20 = int((ent - n100 * 100 - n50 * 50) / 20)
n10 = int((ent - n100 * 100 - n50 * 50 - n20 * 20) / 10)
n5 = int((ent - n100 * 100 - n50 * 50 - n20 * 20 - n10 * 10) / 5)
n2 = int((ent - n100 * 100 - n50 * 50 - n20 * 20 - n10 * 10 - n5 * 5) / 2)
n1 = int(ent - n100 * 100 - n50 * 50 - n20 * 20 - n10 * 10 - n5 * 5 - n2 * 2)

print (int(n100), "nota(s) de R$ 100,00")
print (int(n50), "nota(s) de R$ 50,00")
print (int(n20), "nota(s) de R$ 20,00")
print (int(n10), "nota(s) de R$ 10,00")
print (int(n5), "nota(s) de R$ 5,00")
print (int(n2), "nota(s) de R$ 2,00")
print (int(n1), "nota(s) de R$ 1,00")
