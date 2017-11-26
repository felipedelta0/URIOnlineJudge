# -*- coding: utf-8 -*-
'''
Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano. A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).

                        |y
                    Q2  |   Q1
                        |       x
                ------------------
                        |
                    Q3  |   Q4
                        |

Se o ponto estiver na origem, escreva a mensagem “Origem”.

Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, conforme for a situação.

Entrada
A entrada contem as coordenadas de um ponto.

Saída
A saída deve apresentar o quadrante em que o ponto se encontra.

Exemplo de Entrada 	    Exemplo de Saída
4.5 -2.2                Q4
0.1 0.1                 Q1
0.0 0.0                 Origem
'''

ent = input().split(' ')
ents = [float(num) for num in ent]
x, y = ents

if x == 0.0 and y == 0.0:
    print ('Origem')
elif x == 0.0:
    print ('Eixo Y')
elif y == 0.0:
    print ('Eixo X')
else:
    if x > 0:
        isX = True
    else:
        isX = False

    if y > 0:
        isY = True
    else:
        isY = False

    if isX and isY:
        print ('Q1')
    elif isX and not isY:
        print ('Q4')
    elif not isX and isY:
        print ('Q2')
    else:
        print ('Q3')