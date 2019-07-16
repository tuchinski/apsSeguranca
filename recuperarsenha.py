# -*- coding: utf-8 -*-
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import random
import crypt
import string
import fileinput
from random import choice
import sys

def recuperarSenha(email):
	alfabeto = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	newPassword = "".join(random.sample(alfabeto,8))

	redefinirSenha(encontrarUsuarioPorEmail(email), newPassword)

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

	print "E-mail enviado com sucesso para %s:" % (msg['To'])

def encontrarUsuarioPorEmail(email):
	file = open('passwdteste')
	for i in file.readlines():
		if email in i:
			line = i
	usuario = line.split(':')
	usuario = usuario[0]
	return usuario

def redefinirSenha(usuario, senha):
	newPassword = encriptPassword(senha)

	file = open('shadowteste')
	for i in file.readlines():
		if usuario in i:
			oldPassword = (i[len(usuario)+1 : i.index(':', i.index(':') + 1)])
			i.replace(oldPassword, newPassword)

			for line in fileinput.FileInput("shadowteste",inplace=1):
			   line = line.replace(oldPassword,newPassword)
			   sys.stdout.write(line)

def encriptPassword(senha):
	salt = '$6$'
	possibleSalt = string.ascii_letters + string.digits

	for a in range(8):
		salt = salt + choice(possibleSalt)

	salt = salt + '$'
	encriptedPassword = crypt.crypt(senha,salt)

	return encriptedPassword