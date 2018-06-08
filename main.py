#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2018 aline <aline@LAPTOP-M7UEFDMH>
#  
import LeitorNfcPython
import ifcbanco
import os
import datetime

def confereop(op):
	cls = lambda: os.system('cls')
	cls()
	if(op == 1):
		i = 1
		presenca = LeitorNfcPython.main()
		arquivo = open('chamada%d.txt'%(i),'w')
		i += 2
		arquivo.write("Relatório de presença:\n")
		arquivo.write(datetime.datetime.now().strftime("%d/%m/%y às %H:%M:%S\n"))
		for i in range(len(presenca)):
			arquivo.write("%d - %s\n"%(i+1,presenca[i]))
		arquivo.close()
		#print(presenca)
		op = int(input("\nInsira para continuar:\n1 - Realizar chamada novamente\n0 - Voltar para o menu inicial\n"))
		while not(op == 1 or op == 0):
			op = int(input("Operação inválida! Informe uma operação indicada.\n"))
		while(op == 1):
			cls()
			presenca = LeitorNfcPython.main()
			#print(presenca)
			op = int(input("\nInsira para continuar:\n1 - Realizar chamada novamente\n0 - Voltar para o menu inicial\n"))
	else:
		ifcbanco.main()
	cls()
	menu()

def menu():
	print("=== MENU ===")
	op = int(input("Insira para iniciar:\n1 - Realizar chamada\n2 - Configurações de tag\n0 - Sair\n"))
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
