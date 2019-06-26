import tkinter as tk
from passwdNG import Psswd


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

        self.titulo = tk.Label(titleContainer, text="-- Login --")
        self.titulo["font"] = ("Arial", "15", "bold")
        self.titulo.pack(pady=5)

        self.nomeLabel = tk.Label(primeiroContainer, text="Username:", anchor="w")
        self.nomeLabel["width"] = 10
        self.nomeLabel["justify"] = tk.LEFT
        self.nomeLabel.pack(side=tk.LEFT, pady=5)

        self.nome = tk.Entry(primeiroContainer)
        self.nome["width"] = 50
        self.nome.pack(side=tk.RIGHT, pady=5)

        self.senhaLabel = tk.Label(segundoContainer, text="Password:", anchor="w")
        self.senhaLabel["width"] = 10
        self.senhaLabel["justify"] = tk.LEFT
        self.senhaLabel.pack(side=tk.LEFT, pady=5)

        self.senha = tk.Entry(segundoContainer, show="*")
        self.senha["width"] = 50
        self.senha.pack(side=tk.RIGHT, pady=5)

        self.botao_login = tk.Button(terceiroContainer, command=lambda: master.switch_frame(Painel, passwdNG))
        self.botao_login["text"] = "Login"
        self.botao_login["width"] = 58
        self.botao_login.pack(pady=5)
  
  
    #Método verificar senha
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "usuariodevmedia" and senha == "dev":
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Erro na autenticação"
  

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

        self.botao_Finish = tk.Button(quartoContainer, command=lambda: master.switch_frame(SelectUser, passwdNG))
        self.botao_Finish["text"] = "Finish"
        self.botao_Finish["width"] = 58
        self.botao_Finish.pack(pady=5)

    def get_data_edit_user(self, username, pass1, pass2):
        if ((username and pass1 and pass2) != ""):
            if pass1 == pass2:
                self.titulo["text"] =  "The user was created."
                self.titulo["fg"] = "green"
                print(self.passwdNG.get_file_shadow())
            else:
                self.titulo["text"] =  "The passwords do not match."
                self.titulo["fg"] = "red"
        else:
            self.titulo["text"] =  "Please fill in all fields."
            self.titulo["fg"] = "red"


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
    
        self.titulo = tk.Label(quartoContainer)
        self.titulo["text"] = ""
        self.titulo["font"] = ("Arial", "9", "bold")
        self.titulo.pack()

    def get_data_new_user(self, username, pass1, pass2):
        if ((username and pass1 and pass2) != ""):
            if pass1 == pass2:
                self.titulo["text"] =  "The user was created."
                self.titulo["fg"] = "green"
                print(self.passwdNG.get_file_shadow())
            else:
                self.titulo["text"] =  "The passwords do not match."
                self.titulo["fg"] = "red"
        else:
            self.titulo["text"] =  "Please fill in all fields."
            self.titulo["fg"] = "red"

  
if __name__ == "__main__":
    
    backend_passwd = Psswd()
    app = SampleApp(backend_passwd)
    app.title("NEW PASSWD")
    app.geometry("500x200")
    app.mainloop()
