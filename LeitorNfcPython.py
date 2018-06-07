#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  LeitorNfcPython.py
#  
#  Copyright 2018 aline <aline@LAPTOP-M7UEFDMH>
#  

import serial
import sys
import time
import datetime
import os
import banco

def conSer():
	#==== Conexão com Arduino ====
	porta = "COM3"
	baudrate = 9600
	
	conSerial = serial.Serial(porta,baudrate,timeout=1)
	
	return conSerial

def confereUid(l,x):
	p = False
	if(x in l):
		p = True
	
	return p

def leitura(conSerial):
	ler = conSerial.readline() #tag
	x = ler.decode('utf-8')
	uid = x[:20].split(" ") #lista com uid
	
	return uid

def authProf(conSerial,cnx):
	uid = leitura(conSerial)
	l = banco.selectUidProf(cnx) #acessa lista de prof no banco
	
	p = confereUid(l,uid)
	
	while not(p):
		print("Aguardando autenticação!")
		uid = leitura(conSerial)
		p = confereUid(l,uid)
	
	return p,uid

def authAluno(conSerial,cnx):
	uid = leitura(conSerial)
	l = banco.selectUidAluno(cnx) #acessa lista de aluno no banco
	
	p = confereUid(l,uid)
	
	return p,uid

def imprimeLista(lst):
	for i in range(len(lst)):
		print(lst[i])

def main():
	#==== banco ====
	cnx = banco.con()
	
	#==== serial ====
	conSerial = conSer()
	
	#==== inicializando ====
	print("=== CHAMADA ===")
	print("Aproxime a tag!")
	conSerial.readline() #found pn532
	conSerial.readline() #firmware version
	
	#==== autenticação ====
	p,prof = authProf(conSerial,cnx)
	print("Acesso permitido!")
	time.sleep(1)
	
	m = banco.selectProf(cnx)
	d = banco.selectDisc(cnx)
	for i in range(len(m)):
		if(prof == m[i][3]):
			nomeprof = m[i][2]
			if(m[i][0] == d[i][3]):
				nomedisc = d[i][1]
	
	cls = lambda: os.system('cls')
	cls()
	print("Olá",nomeprof)
	print(nomedisc)
	print("Chamada iniciada no dia",datetime.datetime.now().strftime("%d/%m/%y às %H:%M:%S"))
	
	
	#==== leitura dos alunos ====
	l = banco.selectAluno(cnx)
	n = []
	presenca = []
	while(p):
		f,aluno = authAluno(conSerial,cnx)
		if(aluno[0] != ''):
			if(f):
				for i in range(len(l)):
					if(aluno == l[i][3]):
						if aluno not in n:
							n.append(aluno)
							presenca.append(l[i][1])
							print(datetime.datetime.now().strftime("(%H:%M:%S)"),"Aluno presente: %s"%(l[i][1]))
						else:
							print("Aluno já registrado!")
			else:
				if(aluno != prof):
					print("Aluno não cadastrado no banco!")
		
		if(aluno == prof):
			p = False
			if(len(n) == 0):
				print("Não houve presenças nesse dia.")
			print("Chamada encerrada",datetime.datetime.now().strftime("às %H:%M:%S"),"por",nomeprof)
			print()
			print("Lista de alunos presentes: ")
			imprimeLista(presenca)
			time.sleep(5)
	
	conSerial.close()
	cnx.close()
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main())
