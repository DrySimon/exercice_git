#!/usr/bin/python3
# -*-coding:Utf-8 -*

# Affiche la table de multiplication d'un nombre choisi.

def table_multiplication(nb):
	i = 0
	while i < 10:
		print(int(i) + 1, "*", int(nb), "=", (int(i) + 1) * int(nb))
		i += 1

nombre = input("Table de multiplication de quel nombre ? : ")

table_multiplication(nombre)