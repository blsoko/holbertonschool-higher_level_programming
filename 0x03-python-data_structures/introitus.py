#!/usr/bin/python3
import math

lista = [[0] * 9 for i in range(1, 10)]


for i in range(1, 10):
	for j in range(1, 10):
		lista[i - 1][j - 1] = i * j
for i in range(0, 9):
	print(lista[i])