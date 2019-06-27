import tkinter as tk
import re
from passwdNG import Psswd
import time


class SampleApp(tk.Tk):
    def __init__(self, psw):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(Login, psw)

    def switch_frame(self, frame_class, psw, data = None):
        new_frame = frame_class(self, psw, data)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame["padx"] = 10
        self._frame["pady"] = 10
        self._frame.pack()


class SelectUser(tk.Frame):
    def __init__(self, master, passwdNG, data=None):
        tk.Frame.__init__(self, master)
        self.passwdNG = passwdNG

        ###### DEFINE CONTAINER 00 ######
        titleContainer = tk.Frame(self)
        titleContainer.pack()

        ###### DEFINE CONTAINER 01 ######
        primeiroContainer = tk.Frame(self)
        primeiroContainer.pack()

        ###### DEFINE CONTAINER 02 ######
        segundoContainer = tk.Frame(self)
        segundoContainer.pack()

        ###### DEFINE CONTAINER 03 ######
        terceiroContainer = tk.Frame(self)
        terceiroContainer.pack()

        self.titulo = tk.Label(titleContainer, text=" -- USERS -- ")
        self.titulo["font"] = ("Arial", "15", "bold")
        self.titulo.pack()

        self.lbl = tk.Label(segundoContainer, text="List of Users:", anchor="w")  
        self.lbl["font"] = ("Calibri", "8")
        self.lbl.pack(pady=5)  

        list_users = passwdNG.get_file_shadow()
        tonkes = passwdNG.get_tokens_by_user_shadow()
        i = 1
        self.listbox = tk.Listbox(terceiroContainer)
        self.listbox["width"] = 50
        for line in tonkes:
            self.listbox.insert(i,line[0])
            i = i + 1
            
        self.listbox.pack(side=tk.LEFT, pady=5, padx=1)

        self.bottao_select = tk.Button(terceiroContainer, text="SELECT", command = lambda: master.switch_frame(EditPass, passwdNG, str(self.listbox.get(tk.ANCHOR))))
        self.bottao_select["width"] = 5
        self.bottao_select["height"] = 10
        self.bottao_select.pack(side=tk.RIGHT, pady=5, padx=1)

    def selectUser(self, username):
        print(username)

class Login(tk.Frame):
    def __init__(self, master, passwdNG, data=None):
        tk.Frame.__init__(self, master)
        self.passwdNG = passwdNG

        ###### DEFINE CONTAINER 00 ######
        titleContainer = tk.Frame(self)
        titleContainer.pack()

        ###### DEFINE CONTAINER 01 ######
        primeiroContainer = tk.Frame(self)
        primeiroContainer.pack()

        ###### DEFINE CONTAINER 02 ######
        segundoContainer = tk.Frame(self)
        segundoContainer.pack()

        ###### DEFINE CONTAINER 03 ######
        terceiroContainer = tk.Frame(self)
        terceiroContainer.pack()

        ###### DEFINE CONTAINER 04 ######
        quartoContainer = tk.Frame(self)
        quartoContainer.pack()

        self.titulo = tk.Label(titleContainer, text="-- Login --")
        self.titulo["font"] = ("Arial", "15", "bold")
        self.titulo.pack(pady=5)

        self.nomeLabel = tk.Label(primeiroContainer, text="Username:", anchor="w")
        self.nomeLabel["width"] = 10
        self.nomeLabel["justify"] = tk.LEFT
        self.nomeLabel.pack(side=tk.LEFT, pady=5)

        self.username = tk.Entry(primeiroContainer)
        self.username["width"] = 50
        self.username.pack(side=tk.RIGHT, pady=5)

        self.senhaLabel = tk.Label(segundoContainer, text="Password:", anchor="w")
        self.senhaLabel["width"] = 10
        self.senhaLabel["justify"] = tk.LEFT
        self.senhaLabel.pack(side=tk.LEFT, pady=5)

        self.password = tk.Entry(segundoContainer, show="*")
        self.password["width"] = 50
        self.password.pack(side=tk.RIGHT, pady=5)

        self.botao_login = tk.Button(terceiroContainer, command=lambda: self.get_data_login_user(str(self.username.get()), str(self.password.get())))
        self.botao_login["text"] = "Login"
        self.botao_login["width"] = 58
        self.botao_login.pack(pady=5)

        self.lb_alert = tk.Label(quartoContainer)
        self.lb_alert["text"] = ""
        self.lb_alert["font"] = ("Arial", "9", "bold")
        self.lb_alert.pack()

    def get_data_login_user(self, username, password):
        if ((username and password) != ""):
            self.lb_alert["text"] =  "Sucessfull Login."
            self.lb_alert["fg"] = "green"
            self.master.switch_frame(Painel, self.passwdNG)
        else:
            self.lb_alert["text"] =  "Please fill in all fields."
            self.lb_alert["fg"] = "red"
  

class Painel(tk.Frame):
    def __init__(self, master, passwdNG, data=None):
        tk.Frame.__init__(self, master)
        self.passwdNG = passwdNG

        ###### DEFINE CONTAINER 00 ######
        titleContainer = tk.Frame(self)
        titleContainer.pack()

        ###### DEFINE CONTAINER 01 ######
        primeiroContainer = tk.Frame(self)
        primeiroContainer.pack()

        self.titulo = tk.Label(titleContainer, text=" -- Operation Painel -- ")
        self.titulo["font"] = ("Arial", "15", "bold")
        self.titulo.pack()

        self.botao_create_user = tk.Button(primeiroContainer, command=lambda: master.switch_frame(CreateUser, passwdNG))
        self.botao_create_user["text"] = "Create User"
        self.botao_create_user["width"] = 58
        self.botao_create_user.pack(pady=5)

        self.botao_change_pass_user = tk.Button(primeiroContainer, command=lambda: master.switch_frame(SelectUser, passwdNG))
        self.botao_change_pass_user["text"] = "Change Pass User"
        self.botao_change_pass_user["width"] = 58
        self.botao_change_pass_user.pack(pady=5)


class EditPass(tk.Frame):
    def __init__(self, master, passwdNG, data=None):
        tk.Frame.__init__(self, master)
        self.passwdNG = passwdNG

        ###### DEFINE CONTAINER 00 ######
        titleContainer = tk.Frame(self)
        titleContainer.pack()

        ###### DEFINE CONTAINER 01 ######
        primeiroContainer = tk.Frame(self)
        primeiroContainer.pack()

        ###### DEFINE CONTAINER 02 ######
        segundoContainer = tk.Frame(self)
        segundoContainer.pack()

        ###### DEFINE CONTAINER 03 ######
        terceiroContainer = tk.Frame(self)
        terceiroContainer.pack()

        ###### DEFINE CONTAINER 04 ######
        quartoContainer = tk.Frame(self)
        quartoContainer.pack()

        self.titulo = tk.Label(titleContainer, text=" -- Edit Pass -- ")
        self.titulo["font"] = ("Arial", "15", "bold")
        self.titulo.pack()

        self.lb_pass_current = tk.Label(primeiroContainer, text="Current password:", anchor="w")
        self.lb_pass_current["width"] = 30
        self.lb_pass_current["justify"] = tk.LEFT
        self.lb_pass_current.pack(side=tk.LEFT, pady=5)

        self.pass_current = tk.Entry(primeiroContainer, show="*")
        self.pass_current["width"] = 30
        self.pass_current.pack(side=tk.RIGHT, pady=5)

        self.lb_pass_new = tk.Label(segundoContainer, text="New password:", anchor="w")
        self.lb_pass_new["width"] = 30
        self.lb_pass_new["justify"] = tk.LEFT
        self.lb_pass_new.pack(side=tk.LEFT, pady=5)

        self.pass_new1 = tk.Entry(segundoContainer, show="*")
        self.pass_new1["width"] = 30
        self.pass_new1.pack(side=tk.RIGHT, pady=5)

        self.lb_pass_new = tk.Label(terceiroContainer, text="New Password again:", anchor="w")
        self.lb_pass_new["width"] = 30
        self.lb_pass_new["justify"] = tk.LEFT
        self.lb_pass_new.pack(side=tk.LEFT, pady=5)

        self.pass_new2 = tk.Entry(terceiroContainer, show="*")
        self.pass_new2["width"] = 30
        self.pass_new2.pack(side=tk.RIGHT, pady=5)

        self.botao_Finish = tk.Button(quartoContainer, command=lambda: self.get_data_edit_user(str(self.pass_current.get()), str(self.pass_new1.get()), str(self.pass_new2.get())))
        self.botao_Finish["text"] = "Finish"
        self.botao_Finish["width"] = 58
        self.botao_Finish.pack(pady=5)

        self.lb_alert = tk.Label(quartoContainer)
        self.lb_alert["text"] = ""
        self.lb_alert["font"] = ("Arial", "9", "bold")
        self.lb_alert.pack()


    def get_data_edit_user(self, username, pass1, pass2):
        if ((username and pass1 and pass2) != ""):
            if pass1 == pass2:
                if (self.valid_password(pass1) == True):
                    self.lb_alert["text"] =  "The user was created."
                    self.lb_alert["fg"] = "green"
                    time.sleep(0.3)
                    self.master.switch_frame(SelectUser, self.passwdNG)
            else:
                self.lb_alert["text"] =  "The passwords do not match."
                self.lb_alert["fg"] = "red"
        else:
            self.lb_alert["text"] =  "Please fill in all fields."
            self.lb_alert["fg"] = "red"

    def valid_password(self, password):
        digit = re.search(r"\d", password)
        uppercase = re.search(r"[A-Z]", password)
        lowercase = re.search(r"[a-z]", password) 
        symbol = re.search(r"[ !#$%@%&'()*+,-./[\\\]^_`{|}~"+r'"]', password) 
        
        print (str(len(str(password))), digit, uppercase, lowercase, symbol)
        print(len(str(password)))
        if len(str(password)) < 6:
            self.lb_alert["text"] =  "Passwords should consist of 6 to 8 characters."
            self.lb_alert["fg"] = "red"
        if digit == None:
            self.lb_alert["text"] =  "Passwords should contain digits [0-9]."
            self.lb_alert["fg"] = "red"
        if uppercase == None:
            self.lb_alert["text"] =  "Passwords should contain upper case characters."
            self.lb_alert["fg"] = "red"
        if lowercase == None:
            self.lb_alert["text"] =  "Passwords should contain lower case characters."
            self.lb_alert["fg"] = "red"
        if symbol == None:
            self.lb_alert["text"] =  "Passwords should contain symbols."
            self.lb_alert["fg"] = "red"
        
        if (digit != None and uppercase != None and lowercase != None and symbol != None):
            self.lb_alert["text"] =  ""
            return (True)
        else:
            return (False)

class CreateUser(tk.Frame):
    def __init__(self, master, passwdNG, data=None):
        tk.Frame.__init__(self, master)
        self.passwdNG = passwdNG

        ###### DEFINE CONTAINER 00 ######
        titleContainer = tk.Frame(self)
        titleContainer.pack()

        ###### DEFINE CONTAINER 01 ######
        primeiroContainer = tk.Frame(self)
        primeiroContainer.pack()

        ###### DEFINE CONTAINER 02 ######
        segundoContainer = tk.Frame(self)
        segundoContainer.pack()

        ###### DEFINE CONTAINER 03 ######
        terceiroContainer = tk.Frame(self)
        terceiroContainer.pack()

        ###### DEFINE CONTAINER 04 ######
        quartoContainer = tk.Frame(self)
        quartoContainer.pack()

        self.titulo = tk.Label(titleContainer, text=" -- Create New User -- ")
        self.titulo["font"] = ("Arial", "15", "bold")
        self.titulo.pack()

        self.lb_username = tk.Label(primeiroContainer, text="Username:", anchor="w")
        self.lb_username["width"] = 30
        self.lb_username["justify"] = tk.LEFT
        self.lb_username.pack(side=tk.LEFT, pady=5)

        self.username = tk.Entry(primeiroContainer, show="*")
        self.username["width"] = 30
        self.username.pack(side=tk.RIGHT, pady=5)

        self.lb_pass = tk.Label(segundoContainer, text="Password:", anchor="w")
        self.lb_pass["width"] = 30
        self.lb_pass["justify"] = tk.LEFT
        self.lb_pass.pack(side=tk.LEFT, pady=5)

        self.password1 = tk.Entry(segundoContainer, show="*")
        self.password1["width"] = 30
        self.password1.pack(side=tk.RIGHT, pady=5)

        self.lb_pass_new = tk.Label(terceiroContainer, text="Password again:", anchor="w")
        self.lb_pass_new["width"] = 30
        self.lb_pass_new["justify"] = tk.LEFT
        self.lb_pass_new.pack(side=tk.LEFT, pady=5)

        self.password2 = tk.Entry(terceiroContainer, show="*")
        self.password2["width"] = 30
        self.password2.pack(side=tk.RIGHT, pady=5)

        self.botao_Finish = tk.Button(quartoContainer, command=lambda: self.get_data_new_user(self.username.get(), self.password1.get(), self.password2.get()))
        self.botao_Finish["text"] = "Finish"
        self.botao_Finish["width"] = 58
        self.botao_Finish.pack(pady=5)
    
        self.lb_alert = tk.Label(quartoContainer)
        self.lb_alert["text"] = ""
        self.lb_alert["font"] = ("Arial", "9", "bold")
        self.lb_alert.pack()

    def get_data_new_user(self, username, pass1, pass2):
        if ((username and pass1 and pass2) != ""):
            if pass1 == pass2:
                self.lb_alert["text"] =  "The user was created."
                self.lb_alert["fg"] = "green"
                print(self.passwdNG.get_file_shadow())
            else:
                self.lb_alert["text"] =  "The passwords do not match."
                self.lb_alert["fg"] = "red"
        else:
            self.lb_alert["text"] =  "Please fill in all fields."
            self.lb_alert["fg"] = "red"

  
if __name__ == "__main__":
    
    backend_passwd = Psswd()
    app = SampleApp(backend_passwd)
    app.title("NEW PASSWD")
    app.geometry("500x200")
    app.mainloop()
