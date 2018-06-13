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
		presenca,nomeprof,nomedisc = LeitorNfcPython.main()
		
		arquivo = open('chamada%d.txt'%(i),'w')
		arquivo.write("=== RELATÓRIO DE PRESENÇA ===\n\nProfessor responsável: %s\nDisciplina: %s\n"%(nomeprof,nomedisc))
		arquivo.write("Relatório gerado no dia "+datetime.datetime.now().strftime("%d/%m/%y às %H:%M:%S\n\n"))
		if(len(presenca) == 0):
			print("Não houve presenças nesse dia.")
			arquivo.write("Não houve presenças nesse dia!")
		else:
			for j in range(len(presenca)):
				arquivo.write('%d - %s\n'%(j+1,presenca[j]))
		arquivo.close()
		
		op = int(input("\nInsira para continuar:\n1 - Realizar chamada novamente\n0 - Voltar para o menu inicial\n"))
		while not(op == 1 or op == 0):
			op = int(input("Operação inválida! Informe uma operação indicada.\n"))
		while(op == 1):
			cls()
			presenca,nomeprof,nomedisc = LeitorNfcPython.main()
			
			i += 1
			arquivo = open('chamada%d.txt'%(i),'w')
			arquivo.write("=== RELATÓRIO DE PRESENÇA ===\n\nProfessor responsável: %s\nDisciplina: %s\n"%(nomeprof,nomedisc))
			arquivo.write("Relatório gerado no dia "+datetime.datetime.now().strftime("%d/%m/%y às %H:%M:%S\n\n"))
			if(len(presenca) == 0):
				print("Não houve presenças nesse dia.")
				arquivo.write("Não houve presenças nesse dia!")
			else:
				for j in range(len(presenca)):
					arquivo.write('%d - %s\n'%(j+1,presenca[j]))
			arquivo.close()
			
			op = int(input("\nInsira para continuar:\n1 - Realizar chamada novamente\n0 - Voltar para o menu inicial\n"))
			while not(op == 1 or op == 0):
				op = int(input("Operação inválida! Informe uma operação indicada.\n"))
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
