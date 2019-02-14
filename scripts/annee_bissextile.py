#!/usr/bin/python3
# -*-coding:Utf-8 -*


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