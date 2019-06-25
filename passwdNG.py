import crypt
import string
from random import choice

class Psswd:
    def __init__(self):
         print("INIT DA CLASSE Psswd")
         

    # GET shadow's lines users and return a simple list
    def get_file_shadow(self):
        users_shadow = []
        fileShadow = open("/etc/shadow")
        for line in fileShadow:
            users_shadow.append(line)
        return users_shadow

    def get_tokens_by_user_shadow(self):
        list_users = self.get_file_shadow()
        list_users_tokens = []
        for users in list_users:
            tokens = []
            tokens = users.split(':')
            list_users_tokens.append(tokens)
        return list_users_tokens


    def createPassword(self):
        userName = input('Digite o nome do usuário:')
        userPassword = input("Digite a nova senha:")

        # Starting salt creation
        salt = '$6$'

        # All alphanumeric ascii
        possibleSalt = string.ascii_letters + string.digits

        # Creating salt password
        for a in range(8):
            salt = salt + choice(possibleSalt)
        salt = salt + '$'
        

        encriptedPassword = crypt.crypt(userPassword,salt)

        user_change = "false"
        # print(encriptedPassword)
        fileShadow = open('/etc/shadow')
        conteudo = fileShadow.readlines()
        fileShadowRead = fileShadow.read().split()
        for line in fileShadowRead:
            lineBreak = line.split(':')
            if(lineBreak[0] == userName):
                print(encriptedPassword)
                lineBreak[1] = encriptedPassword
                print(lineBreak)
                user_change = "true"
                fileShadow.write(makeLineShadow(lineBreak))
                break
    
        if user_change == "false":
            print ("Este usuario não esta presente sistema")       
                


    def makeLineShadow(self, lineBreak):
        new_line = ""
        for i in lineBreak:
            new_line = new_line + i +":"
        return new_line[:-1]

        # print(len(fileShadowRead))
        



if __name__ == "__main__":
    print("MAIN")