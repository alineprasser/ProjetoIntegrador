#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2018 aline <aline@LAPTOP-M7UEFDMH>
#  
import LeitorNfcPython
import ifcbanco
import banco
import os

def confereop(op):
	cls = lambda: os.system('cls')
	cls()
	if(op == 1):
		LeitorNfcPython.main()
	else:
		ifcbanco.main()
	cls()
	menu()

def menu():
	print("=== MENU ===")
	op = int(input("Insira\n1 - Realizar chamada\n2 - Configurações de tag\n0 - Sair\n"))
	while not(op == 1 or op == 2 or op == 0):
			op = int(input("Operação inválida! Informe uma operação indicada.\n"))
	if(op != 0):
		confereop(op)
def main(args):
	print("Projeto Integrador\nAline Bravin Prasser e Sidney Roberts Freire")
	menu()
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
