# -*- coding: utf-8 -*-

'''
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Exemplo de Entrada	    Exemplo de Saída
576.73                  NOTAS:
                        5 nota(s) de R$ 100.00
                        1 nota(s) de R$ 50.00
                        1 nota(s) de R$ 20.00
                        0 nota(s) de R$ 10.00
                        1 nota(s) de R$ 5.00
                        0 nota(s) de R$ 2.00
                        MOEDAS:
                        1 moeda(s) de R$ 1.00
                        1 moeda(s) de R$ 0.50
                        0 moeda(s) de R$ 0.25
                        2 moeda(s) de R$ 0.10
                        0 moeda(s) de R$ 0.05
                        3 moeda(s) de R$ 0.01

4.00                    NOTAS:
                        0 nota(s) de R$ 100.00
                        0 nota(s) de R$ 50.00
                        0 nota(s) de R$ 20.00
                        0 nota(s) de R$ 10.00
                        0 nota(s) de R$ 5.00
                        2 nota(s) de R$ 2.00
                        MOEDAS:
                        0 moeda(s) de R$ 1.00
                        0 moeda(s) de R$ 0.50
                        0 moeda(s) de R$ 0.25
                        0 moeda(s) de R$ 0.10
                        0 moeda(s) de R$ 0.05
                        0 moeda(s) de R$ 0.01

91.01                   NOTAS:
                        0 nota(s) de R$ 100.00
                        1 nota(s) de R$ 50.00
                        2 nota(s) de R$ 20.00
                        0 nota(s) de R$ 10.00
                        0 nota(s) de R$ 5.00
                        0 nota(s) de R$ 2.00
                        MOEDAS:
                        1 moeda(s) de R$ 1.00
                        0 moeda(s) de R$ 0.50
                        0 moeda(s) de R$ 0.25
                        0 moeda(s) de R$ 0.10
                        0 moeda(s) de R$ 0.05
                        1 moeda(s) de R$ 0.01
'''

valor = float(input())
reais = int(valor)
centavos = int((valor - reais) * 100)

n100 = reais // 100
reais = reais - (n100 * 100)
n50 = reais // 50
reais = reais - (n50 * 50)
n20 = reais // 20
reais = reais - (n20 * 20)
n10 = reais // 10
reais = reais - (n10 * 10)
n5 = reais // 5
reais = reais - (n5 * 5)
n2 = reais // 2
reais = reais - (n2 * 2)

m1 = 0
if reais:
    m1 = 1

m50 = centavos // 50
centavos = centavos - (m50 * 50)
m25 = centavos // 25
centavos = centavos - (m25 * 25)
m10 = centavos // 10
centavos = centavos - (m10 * 10)
m05 = centavos // 5
centavos = centavos - (m05 * 5)
m01 = centavos

print ("NOTAS:")
print (n100, "nota(s) de R$ 100.00")
print (n50, "nota(s) de R$ 50.00")
print (n20, "nota(s) de R$ 20.00")
print (n10, "nota(s) de R$ 10.00")
print (n5, "nota(s) de R$ 5.00")
print (n2, "nota(s) de R$ 2.00")
print ("MOEDAS:")
print (m1, "moeda(s) de R$ 1.00")
print (m50, "moeda(s) de R$ 0.50")
print (m25, "moeda(s) de R$ 0.25")
print (m10, "moeda(s) de R$ 0.10")
print (m05, "moeda(s) de R$ 0.05")
print (m01, "moeda(s) de R$ 0.01")
