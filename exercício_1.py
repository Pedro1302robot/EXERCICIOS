# -*- coding: utf-8 -*-
"""EXERCÍCIO 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1voY2K5sxK8PDrkGbCXmxaIMhm1_Xvcbo
"""

print("""Escreva um programa que peça 2 números e um número real. Calcule e mostre:
O produto do dobro do primeiro com a metade do segundo;
A soma do triplo do primeiro com o terceiro;
O terceiro elevado ao cubo.""")

numero1inteiro = int(input("Digite o primeiro número inteiro:"))
numero2inteiro = int(input("Digite o segundo número inteiro:"))
numero3real = float(input("Digite o terceiro número real:"))

print("O produto do dobre do primeiro com a metade do segundo",(numero1inteiro*2)*(numero2inteiro/2))
print("A soma do triplo do primeiro com o terceiro",(numero1inteiro*3)+numero3real)
print("O terceiro elevado ao cubo",numero3real**3)