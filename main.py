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

def show_points(x,y):
	for k in x:
		print(f"Point {k} : ({x[k]}; {y[k]})")
	return None

def PInterpol(x, L):
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

def Lagrange(L, y):
	"""Fonction servant à finaliser l'interpolation,
    à multiplier les Polynomes intermédiaires
    par leur y"""
	PF=0
	for k in L:
		PF+=y[k]*L[k]
	return PF

askpoints(x,y)
show_points(x,y)
PInterpol(x, L)
print(Lagrange(L, y))

def main():
	pass


if __name__ == '__main__':
	main()

