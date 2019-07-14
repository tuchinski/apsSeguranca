import crypt
import string, random
from random import choice

class Psswd:
    def __init__(self):
         print("---")

    # GET shadow's lines users and return a simple list
    def get_file_shadow(self):
        users_shadow = []
        fileShadow = open("/etc/shadow")
        for line in fileShadow:
            users_shadow.append(line)
        return users_shadow

    # GET passwd's lines users and return a simple list
    def get_file_passwd(self):
        users_passwd= []
        filePasswd= open("/etc/passwd")
        for line in filePasswd:
            users_passwd.append(line)
        return users_passwd

    def get_tokens_by_user_shadow(self):
        list_users = self.get_file_shadow()
        list_users_tokens = []
        for users in list_users:
            tokens = []
            tokens = users.split(':')
            list_users_tokens.append(tokens)
        return list_users_tokens

    def get_tokens_by_user_passwd(self):
        list_users = self.get_file_passwd()
        list_users_tokens = []
        for users in list_users:
            tokens = []
            tokens = users.split(':')
            list_users_tokens.append(tokens)
        return list_users_tokens

    def who_is_the_biggest_ID(self):
        list_tokens = self.get_tokens_by_user_passwd()
        maior = 0
        for user in list_tokens:
            if (int(user[2]) > maior):
                maior = int(user[2]) 
        return maior

    def create_new_user(self, username, password, fullname=None, tellphone=None, email=None, other=None, nivel_access=None):
        # Here, we have the line that goint to add in the file shadow
        randomsalt = ''.join(random.sample(string.ascii_letters,8))
        randomsalt = '$6$' + randomsalt + '$'
        line_shadow = crypt.crypt(password, randomsalt)
        line_shadow = username + ':' + line_shadow
        print(line_shadow)
        self.adduser_shadow(line_shadow)

        # Here, we have the line that goint to add in the file passwd
        the_last_biggest_ID = self.who_is_the_biggest_ID() + 1
        comentarios = '['+ 'fullname:' + str(fullname) + ', tellphone:' + str(tellphone) + ', email:' + str(email) + ', other:' + str(other) + ']'
        line_passwd = username + ':x:' + str(the_last_biggest_ID) + ':' + str(the_last_biggest_ID) + ':' + comentarios + ':/home/' + username + ':/bin/bash'
        print(line_passwd)
        # self.save_passwd(line_passwd)

        
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
        fileShadow = open('/etc/shadow.def')
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


    def blockUser(self,username):
        tokens = self.get_tokens_by_user_passwd()
        token_change = ''
        for user in tokens:
            if user[0] == username:
                user[1] = '!x'
                token_change = user
                break
        
        self.update_passwd(user)

    # Atualiza um usuario
    def update_passwd(self, user):
        users_tokens = []
        users_tokens = self.get_tokens_by_user_passwd()
        for i in users_tokens:
            if(i[0] == user[0]):
                users_tokens.remove(i)
                break

        users_tokens.append(user)
        users_tokens_str = ''
        for i in users_tokens:
            users_tokens_str += ':'.join(i)

        fileShadow = open('/etc/passwd.teste', 'w+')
        fileShadow.write(users_tokens_str)
     
        fileShadow.close()

        fileShadow = open('/etc/passwd.teste')
        print(fileShadow.read())

    # salva a galerinha
    def save_passwd(self, user):
        # print(user)
        users_tokens = []
        users_tokens = self.get_tokens_by_user_passwd()
        
        users_tokens_str = ''
        for i in users_tokens:
            users_tokens_str += ':'.join(i)

        users_tokens_str += user
        fileShadow = open('/etc/passwd.teste', 'w+')
        fileShadow.write(users_tokens_str)
     
        fileShadow.close()

        fileShadow = open('/etc/passwd.teste')
        print(fileShadow.read())

    # Save a new user on shadow file. Recieves the line to add on /etc/shadow
    def adduser_shadow(self,line):
        file = self.get_file_shadow()
        file.append(line)
        passwd = open('/etc/shadow.teste', 'w+')

        string_to_save = ''.join(file)
        passwd.write(string_to_save)

        passwd.close()
        # print(string_to_save)

    # desbloqueia o usuario
    def unlockUser(self, user):
        users_tokens = []
        users_tokens = self.get_tokens_by_user_passwd()
        for i in users_tokens:
            if i[0] == user:
                i[1] = "x"
                user_unlock = i
                break
        self.update_passwd(user_unlock)
        # print(user_unlock)
        return 

    






if __name__ == "__main__":
    passwdng = Psswd()
    #passwdng.create_new_user("rafael", "rafaelsenha123", "Rafael Menezes Barboza", "4499X4534X", "ra29fa@gmail.com", "User to study", "1")
    # passwdng.save_shadow2('usersemsenha:*:18089:0:99999:7:::\n')
    passwdng.unlockUser('teste2')

