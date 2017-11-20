# -*- coding: utf-8 -*-

'''
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:

MaiorAB = (a+b+abs(a-b)) / 2

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

Exemplos de Entrada	    Exemplos de Saída
7 14 106                106 eh o maior
217 14 6                217 eh o maior
'''

entrada = input()
strnums = entrada.split(" ")
nums = [int(num) for num in strnums]
a, b, c = nums

ab = (a + b + abs(a-b)) / 2
maiorabc = (ab + c + abs(ab-c)) / 2

print (int(maiorabc), "eh o maior")