# -*- coding: utf-8 -*-
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import random

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
	fileShadow = open('/etc/shadow')
	for line in fileShadow.readlines():
		if email in line:
			print("line")

#recuperarSenha("allisonsampaiox@gmail.com")
encontrarUsuario("colour")