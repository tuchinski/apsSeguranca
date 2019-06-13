import crypt
import string
from random import choice

def criaSenha():
    senhaUser = input("Digite a nova senha:")
    arq = open('/etc/shadow')

    # Começando a criação do salt
    salt = '$6$'

    # Todos os caracteres alfanuméricos
    possiveisSalt = string.ascii_letters + string.digits

    # Criando salt da senha
    for i in range(8):
        salt = salt + choice(possiveisSalt)
    salt = salt + '$'


    senhaCriptografada = crypt.crypt(senhaUser,salt)

    print(senhaCriptografada)

if __name__ == "__main__":
    criaSenha()