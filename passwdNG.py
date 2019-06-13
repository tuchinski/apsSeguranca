import crypt
import string
from random import choice

def criaSenha():
    senhaUser = input("Digite a nova senha:")
    arq = open('/etc/shadow')

    # Starting salt creation
    salt = '$6$'

    # All alphanumeric ascii
    possiveisSalt = string.ascii_letters + string.digits

    # Creating salt password
    for i in range(8):
        salt = salt + choice(possiveisSalt)
    salt = salt + '$'


    senhaCriptografada = crypt.crypt(senhaUser,salt)

    print(senhaCriptografada)

if __name__ == "__main__":
    criaSenha()