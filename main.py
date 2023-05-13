#!/usr/bin/env python
#-*- Coding : UTF-8-*-
"""
main.py

Created by Adahy on 2023-05-13.
Copyright (c) 2023 Adahy de Plas. All rights reserved.
"""

import sys
import os
import numpy as np

x={} #dictionnaire contenant toutes les abscisses
y={} #dictionnaire contenant toutes les ordonnées
L={} #dictionnaire contenant tous les polynomes interpolateurs
def banner():
	print("Lagrange's Interpolation")

def info():
	print("Usage : lagrange [options] [file]")
	print("--cli      : Démarre le programme dans le terminal, pas besoin de fichier")
	print("--file, -f : Démarre le programme dans le terminal en prenant le fichier en entrée")
	print("--help, -h : Affiche cette aide")

#---Fonctions de base---

def is_text(v:str):
	"""Fonction servant à vérfier si l'entrée
    peut être convertie en nombre"""
	try:
		float(v)
		return False
	except:
		return True

def askpoints(x:dict, y:dict):
	"""Fonction servant à récupérer les points
    pour l'interpolation"""
	N=input("Nombre de points : ")
	while is_text(N)==True:
		print("Veuillez entrer un nombre entier !")
		N=input("Nombre de points : ")
	c=1
	while c <= int(N):
		x[c]=input(f"x{c} : ")
		while is_text(x[c])==True:
			print("Veuillez entrer un nombre !")
			x[c]=input(f"x{c} : ")
		x[c]=float(x[c])
		y[c]=input(f"y{c} : ")
		while is_text(y[c]):
			print("Veuillez entrer un nombre !")
			y[c]=input(f"y{c} : ")
		y[c]=float(y[c])
		c+=1
	return None

def show_points(x:dict,y:dict):
	for k in x:
		print(f"Point {k} : ({x[k]}; {y[k]})")
	return None

def PInterpol(x:dict, L:dict):
	"""Fonction servant à générer
    les polynomes interpolateurs
    de Lagrange"""
	for i in x:
		L[i]=1
		for j in x:
			if i==j:
				L[i]*=1
			else:
				PIN=np.poly1d([1, -x[j]])
				PID=np.poly1d([x[i]-x[j]])
				div=np.polydiv(PIN, PID)
				PI=div[0]
				L[i]*=PI
	return None

def Lagrange(L:dict, y:dict):
	"""Fonction servant à finaliser l'interpolation,
    à multiplier les Polynomes intermédiaires
    par leur y"""
	PF=0
	for k in L:
		PF+=y[k]*L[k]
	return PF

#--- Fonctions complémentaires ---

def read_file(file):
	"""Fonction servant à convertir un fichier
    texte en deux dictionnaires séparés
    Format du fichier : '{x},{y}\n'"""
	try:
		with open(file, 'r') as f:
			data=f.readlines()
			c=1
			for k in data:
				d=k.split(",")
				x[c]=float(d[0])
				y[c]=float(d[1].strip("\n"))
				c+=1
	except FileNotFoundError:
		print("Veuillez vérifier votre fichier !")
		sys.exit(0)

def main():
	global x, y, L
	banner()
	try:
		if sys.argv[1]=="--help" or sys.argv[1]=="-h":
			info()
		elif sys.argv[1]=="--file" or sys.argv[1]=="-f":
			read_file(sys.argv[2])
			show_points(x, y)
			PInterpol(x, L)
			print(Lagrange(L, y))
		elif sys.argv[1]=="--cli":
			askpoints(x, y)
			show_points(x,y)
			PInterpol(x, L)
			print(Lagrange(L, y))
		else:
			print(f"l'option {sys.argv[1]} n'existe pas !")
			info()
	except(KeyboardInterrupt, EOFError):
		print("Vous avez quitté le programme ! À bientôt ! :)")
		sys.exit(0)
	except ValueError:
		print("Une erreur a eu lieu avec les données, veuillez redémarrer...")
		sys.exit(0)
	except IndexError:
		info()
		
if __name__ == '__main__':
	main()
	sys.exit(0)

