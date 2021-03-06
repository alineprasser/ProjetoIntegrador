import mysql.connector

def insertAluno(cnx, nome, matricula, uid):
	cursor = cnx.cursor()
	query = ("INSERT INTO Aluno (nomeAluno, matAluno,UIDaluno) VALUES ('{}','{}','{}')".format(str(nome), str(matricula),str(uid)))
	cursor.execute(query)
	cnx.commit()
	cursor.close()

def insertProf(cnx,cod,nome,uid):
	cursor = cnx.cursor()
	query = ("INSERT INTO Professor (codProf,nomeProf,UIDprof) VALUES ('{}','{}','{}')".format(str(cod),str(nome),str(uid)))
	cursor.execute(query)
	cnx.commit()
	cursor.close()

def insertDisc(cnx,nome,ch,prof):
	cursor = cnx.cursor()
	query = ("INSERT INTO Disciplina (nomeDisc,cargaHoraria,idProfessor) VALUES ('{}','{}','{}')".format(str(nome),str(ch),str(prof)))
	cursor.execute(query)
	cnx.commit()
	cursor.close()

def selectAluno(cnx):
	l = []
	m = []
	cursor = cnx.cursor()
	query = "SELECT * FROM Aluno"
	cursor.execute(query)
	for row in cursor:
		l.append(row[0]) #id
		l.append(row[1]) #nome
		l.append(row[2]) #matricula
		l.append(row[3].split(" ")) #uid
		m.append(l)
		l = []
	cursor.close()
	return m

def selectProf(cnx):
	l = []
	m = []
	cursor = cnx.cursor()
	query = "SELECT * FROM Professor"
	cursor.execute(query)
	for row in cursor:
		l.append(row[0]) #id
		l.append(row[1]) #cod
		l.append(row[2]) #nome
		l.append(row[3].split(" ")) #uid
		m.append(l)
		l = []
	cursor.close()
	return m

def selectDisc(cnx):
	l = []
	m = []
	cursor = cnx.cursor()
	query = "SELECT * FROM Disciplina"
	cursor.execute(query)
	for row in cursor:
		l.append(row[0]) #id
		l.append(row[1]) #nome
		l.append(row[2]) #carga horaria
		l.append(row[3]) #id prof
		m.append(l)
		l = []
	cursor.close()
	return m

def updateAluno(cnx, matricula, nome):
	cursor = cnx.cursor()
	query = "UPDATE Aluno SET nomeAluno = '{}' WHERE matAluno = '{}'".format(nome, matricula)
	cursor.execute(query)
	cnx.commit()
	cursor.close()

def deleteAluno(cnx, matricula):
	cursor = cnx.cursor()
	query = "DELETE FROM Professor WHERE idProfessor = '{}'".format(matricula)
	cursor.execute(query)
	cnx.commit()
	cursor.close

def selectUidProf(cnx):
	l = []
	cursor = cnx.cursor()
	query = "SELECT UIDprof FROM Professor"
	cursor.execute(query)
	for row in cursor:
		l.append(row[0].split(" "))
	cursor.close
	return l

def selectUidAluno(cnx):
	l = []
	cursor = cnx.cursor()
	query = "SELECT UIDaluno FROM Aluno"
	cursor.execute(query)
	for row in cursor:
		l.append(row[0].split(" "))
	cursor.close
	return l

def selectTodasUid(cnx):
	l = []
	adm = ['04', 'B3', '61', '2A', 'E7', '4C', '80']
	
	cursor = cnx.cursor()
	query = "SELECT UIDaluno FROM Aluno"
	cursor.execute(query)
	for row in cursor:
		l.append(row[0].split(" "))
	
	query = "SELECT UIDprof FROM Professor"
	cursor.execute(query)
	for row in cursor:
		l.append(row[0].split(" "))
	cursor.close()
	
	l.append(adm)
	
	return l

def con():
	config = {
		'user': 'root',
		'password': '1234',
		'host': '127.0.0.1',
		'database': 'modelo'
	}
	cnx = mysql.connector.connect(**config)
	
	return cnx

def deleteTag(cnx,x):
	cursor = cnx.cursor()
	l = selectUidProf(cnx)
	if x in l:
		m = selectProf(cnx)
		d = selectDisc(cnx)
		for i in range(len(m)):
			if(x == m[i][3]):
				query = "DELETE FROM Disciplina WHERE idProfessor = '{}'".format(m[i][0])
				cursor.execute(query)
				cnx.commit()
				query = "DELETE FROM Professor WHERE idProfessor = '{}'".format(m[i][0])
	else:
		l = selectUidAluno(cnx)
		if x in l:
			m = selectAluno(cnx)
			for i in range(len(m)):
				if(x == m[i][3]):
					query = "DELETE FROM Aluno WHERE idAluno = '{}'".format(m[i][0])
	cursor.execute(query)
	cnx.commit()
	cursor.close()

def main():
	cnx = con()
	
	l = selectDisc(cnx)
	for i in range(len(l)):
		print(l[i])
	print()
	
	l = selectAluno(cnx)
	for i in range(len(l)):
		print(l[i])
	print()
	
	l = selectProf(cnx)
	for i in range(len(l)):
		print(l[i])
	print()
	
	cnx.close()

if __name__ == "__main__":
	main()
