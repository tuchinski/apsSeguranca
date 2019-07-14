# -*- coding: utf-8 -*-
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import random
import crypt
import string
from random import choice

def recuperarSenha(email):
	alfabeto = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	newPassword = "".join(random.sample(alfabeto,8))

	msg = MIMEMultipart() # Cria instância do objeto de mensagem
	message = " Olá! Sua nova senha para o PasswdNG é: " + newPassword + ".\n Recomendamos que após o login você altere a senha."
	 
	# Parâmetros da mensagem
	password = "seguranca"
	msg['From'] = "pwdng2019@gmail.com"
	msg['To'] = email
	msg['Subject'] = "Sua nova senha do PasswdNG"
	 
	# Adiciona mensagem ao corpo do e-mail
	msg.attach(MIMEText(message, 'plain'))

	# Cria o server e conecta
	server = smtplib.SMTP('smtp.gmail.com: 587')
	server.starttls()
	 
	# Credenciais de Login
	server.login(msg['From'], password)
	 
	# Envia mensagem ao servidor
	server.sendmail(msg['From'], msg['To'], msg.as_string())
	 
	# Fecha conexão com o servidor
	server.quit()

	print "successfully sent email to %s:" % (msg['To'])

def encontrarUsuario(email):
	file = open('/etc/passwd')
	for i in file.readlines():
		if email in i:
			line = i
	usuario = line.split(':')
	usuario = usuario[0]
	return usuario

def alterarSenha(usuario, senha):
	salt = '$6$'
	possibleSalt = string.ascii_letters + string.digits

	for a in range(8):
		salt = salt + choice(possibleSalt)

	salt = salt + '$'
	encriptedPassword = crypt.crypt(senha,salt)

	c = -1

	file = open('teste.txt', 'rw')
	for i in file.readlines():
		c = c + 1
		if usuario in i:
			line = i
			print(line)
			c_line = c

	aux = line.split(':')[0] + ":" + line.split(':')[1]
	newKey = line.split(':')[0] + ":" + encriptedPassword

	file = open('teste.txt', 'rw')
	for i in file.readlines():
		if aux in i:
			print(aux)

def alterar_linha(path,index_linha,nova_linha):
    with open(path,'r') as f:
        texto=f.readlines()
    with open(path,'w') as f:
        for i in texto:
            if texto.index(i)==index_linha:
                f.write(nova_linha+'\n')
            else:
                f.write(i)

#recuperarSenha("allisonsampaiox@gmail.com")
alterarSenha("allisonsampaiox", "123mudar")
#alterar_linha("teste.txt", 0, "oi")