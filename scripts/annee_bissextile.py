#!/usr/bin/python3
# -*-coding:Utf-8 -*

# Ce script a pour but de vérifier si une année, saisie par l'utilisateur, est bissextile ou non.

annee = input("Veuillez saisir une année : ")
annee = int(annee)

def annee_bissextile(annee):
	if annee % 4 != 0:
		print("Année non bissextile")
	else:
		if annee % 100 != 0:
			print("Année non bissextile")
		else:
			if annee % 400 != 0:
				print("Année non bissextile")        
			else:
				print("Année bissextile")
	return annee
	
annee_bissextile(annee)