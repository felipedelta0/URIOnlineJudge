# -*- coding: utf-8 -*-
import math
'''
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

Distancia = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

Entrada
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.

Exemplo de Entrada	    Exemplo de Saída
1.0 7.0                 4.4721
5.0 9.0

-2.5 0.4                16.1484
12.1 7.3

2.5 -0.4                16.4575
-12.2 7.0
'''

ent1 = input()
ent2 = input()
strn1 = ent1.split(" ")
strn2 = ent2.split(" ")
num1 = [float(num) for num in strn1]
num2 = [float(num) for num in strn2]
x1, y1 = num1
x2, y2 = num2

res = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

print ("{:.4f}".format(res))