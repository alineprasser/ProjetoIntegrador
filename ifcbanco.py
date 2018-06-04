#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ifcbanco.py
#  
#  Copyright 2018 aline <aline@LAPTOP-M7UEFDMH>
#  

import banco
import LeitorNfcPython

def leitura(conSerial):
	ler = conSerial.readline() #tag
	x = ler.decode('utf-8')
	uid = x[:20]
	x = uid.split(" ")
	return x,uid

def confereop(op):
	conSerial = LeitorNfcPython.conSer()
	conSerial.readline() #found pn532
	conSerial.readline() #firmware version
	conSerial.readline()
	cnx = banco.con()
	p = banco.selectUidProf(cnx)
	d = banco.selectDisc(cnx)
	a = banco.selectUidAluno(cnx)
	x,uid = leitura(conSerial)
	while(x[0] == ''):
		x,uid = leitura(conSerial)
	if(op == 1):
		if x in p:
			print("Tag já está cadastrada no banco de dados!")
		else:
			nome = input("Informe o nome do professor: ")
			cod = input("Informe o código do professor: ")
			banco.insertProf(cnx,cod,nome,uid)
			disc = input("Informe o nome da disciplina que este professor leciona: ")
			ch = input("Informe a carga horária da disciplina: ")
			p = banco.selectProf(cnx)
			for i in p:
				if(i[3] == x):
					idp = i[0]
			banco.insertDisc(cnx,nome,ch,idp)
	else:
		if x in a:
			print("Tag já está cadastrada no banco de dados!")
		else:
			nome = input("Informe o nome do aluno: ")
			mat = input("Informe a matrícula: ")
			banco.insertAluno(cnx,nome,mat,uid)

def main(args):
	print("Informe a operação desejada!\n1 - Registrar professor no banco de dados\n2 - Registrar aluno no banco de dados")
	op = int(input())
	while(op != 1 and op != 2):
		op = int(input("Operação inválida. Informe 1 ou 2!\n"))
	confereop(op)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
