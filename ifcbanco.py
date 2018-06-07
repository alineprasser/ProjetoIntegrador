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

def confereop(op,conSerial,cnx):
	adm = ['04', 'B3', '61', '2A', 'E7', '4C', '80']
	p = banco.selectProf(cnx)
	a = banco.selectAluno(cnx)
	d = banco.selectDisc(cnx)
	todas = banco.selectTodasUid(cnx)
	
	print("Aproxime a tag ao leitor.\n")
	
	listaUid,uid = leitura(conSerial)
	while(listaUid[0] == ''):
		listaUid,uid = leitura(conSerial)
	
	if(op == 1):
		if listaUid in todas:
			print("Tag já está cadastrada no banco de dados!\n")
		else:
			nome = input("Informe o nome do professor: ")
			cod = input("Informe o código do professor: ")
			banco.insertProf(cnx,cod,nome,uid)
			disc = input("Informe o nome da disciplina que este professor leciona: ")
			ch = input("Informe a carga horária da disciplina: ")
			p = banco.selectProf(cnx)
			for i in p:
				if(i[3] == listaUid):
					idp = i[0]
			banco.insertDisc(cnx,disc,ch,idp)
			print("Professor cadastrado com sucesso!\n")
	elif(op == 2):
		if listaUid in todas:
			print("Tag já está cadastrada no banco de dados!\n")
		else:
			nome = input("Informe o nome do aluno: ")
			mat = input("Informe a matrícula: ")
			banco.insertAluno(cnx,nome,mat,uid)
			print("Aluno cadastrado com sucesso!\n")
	else:
		if listaUid in todas:
			print("Dados que serão apagados: ")
			for i in a:
				if(i[3] == listaUid):
					print(i)
			for i in p:
				if(i[3] == listaUid):
					print(i)
			print("Esta ação apagará os dados do banco de dados permanentemente. Aproxime a tag ADMIN para confirmar ou outra qualquer para cancelar.\n")
			confirma,uid = leitura(conSerial)
			while(confirma[0] == ''):
				confirma,uid = leitura(conSerial)
			if(confirma == adm):
				banco.deleteTag(cnx,listaUid)
				print("Dados apagados.\n")
			else:
				print("Tag inválida. Por razões de segurança, será redirecionado ao menu.\n")
		else:
			print("Tag não cadastrada.")
	menu(conSerial,cnx)

def menu(conSerial,cnx):
	while(conSerial.isOpen()):
		print("=== CONFIGURAÇÃO DE TAG ===")
		op = int(input("Informe a operação desejada!\n1 - Registrar professor no banco de dados\n2 - Registrar aluno no banco de dados\n3 - Deletar tag\n0 - Voltar para o menu inicial\n"))
		while not(op == 1 or op == 2 or op == 3 or op == 0):
			op = int(input("Operação inválida! Informe uma operação indicada.\n"))
		if(op != 0):
			confereop(op,conSerial,cnx)
		else:
			conSerial.close()
			cnx.close()

def main():
	conSerial = LeitorNfcPython.conSer()
	conSerial.readline() #found pn532
	conSerial.readline() #firmware version
	conSerial.readline()
	cnx = banco.con()
	
	menu(conSerial,cnx)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())
