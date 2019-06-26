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

        titulo = tk.Label(titleContainer, text=" -- USERS -- ")
        titulo["font"] = ("Arial", "15", "bold")
        titulo.pack()

        lbl = tk.Label(segundoContainer, text="List of Users:", anchor="w")  
        lbl["font"] = ("Calibri", "8")
        lbl.pack(pady=5)  

        list_users = passwdNG.get_file_shadow()
        tonkes = passwdNG.get_tokens_by_user_shadow()
        i = 1
        listbox = tk.Listbox(terceiroContainer)
        listbox["width"] = 50
        for line in tonkes:
            listbox.insert(i,line[0])
            i = i + 1
            
        listbox.pack(side=tk.LEFT, pady=5, padx=1)

        bottao_select = tk.Button(terceiroContainer, text="SELECT", command = lambda: master.switch_frame(EditPass, passwdNG, str(listbox.get(tk.ANCHOR))))
        bottao_select["width"] = 5
        bottao_select["height"] = 10
        bottao_select.pack(side=tk.RIGHT, pady=5, padx=1)

    def selectUser(self, username):
        print(username)

class Login(tk.Frame):
    def __init__(self, master, passwdNG, data=None):
        tk.Frame.__init__(self, master)

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

        titulo = tk.Label(titleContainer, text="-- Login --")
        titulo["font"] = ("Arial", "15", "bold")
        titulo.pack()

        nomeLabel = tk.Label(primeiroContainer, text="Username:", anchor="w")
        nomeLabel["width"] = 10
        nomeLabel["justify"] = tk.LEFT
        nomeLabel.pack(side=tk.LEFT, pady=5)

        nome = tk.Entry(primeiroContainer)
        nome["width"] = 50
        nome.pack(side=tk.RIGHT, pady=5)

        senhaLabel = tk.Label(segundoContainer, text="Password:", anchor="w")
        senhaLabel["width"] = 10
        senhaLabel["justify"] = tk.LEFT
        senhaLabel.pack(side=tk.LEFT, pady=5)

        senha = tk.Entry(segundoContainer, show="*")
        senha["width"] = 50
        senha.pack(side=tk.RIGHT, pady=5)

        botao_login = tk.Button(terceiroContainer, command=lambda: master.switch_frame(Painel, passwdNG))
        botao_login["text"] = "Login"
        botao_login["width"] = 58
        botao_login.pack(pady=5)
  
  
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

        ###### DEFINE CONTAINER 00 ######
        titleContainer = tk.Frame(self)
        titleContainer.pack()

        ###### DEFINE CONTAINER 01 ######
        primeiroContainer = tk.Frame(self)
        primeiroContainer.pack()

        titulo = tk.Label(titleContainer, text=" -- Operation Painel -- ")
        titulo["font"] = ("Arial", "15", "bold")
        titulo.pack()

        botao_create_user = tk.Button(primeiroContainer, command=lambda: master.switch_frame(CreateUser, passwdNG))
        botao_create_user["text"] = "Create User"
        botao_create_user["width"] = 58
        botao_create_user.pack(pady=5)

        botao_change_pass_user = tk.Button(primeiroContainer, command=lambda: master.switch_frame(EditPass, passwdNG))
        botao_change_pass_user["text"] = "Change Pass User"
        botao_change_pass_user["width"] = 58
        botao_change_pass_user.pack(pady=5)



class EditPass(tk.Frame):
    def __init__(self, master, passwdNG, data=None):
        tk.Frame.__init__(self, master)

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

        print(data)

        titulo = tk.Label(titleContainer, text=" -- Edit Pass -- ")
        titulo["font"] = ("Arial", "15", "bold")
        titulo.pack()

        lb_pass_current = tk.Label(primeiroContainer, text="Current password:", anchor="w")
        lb_pass_current["width"] = 30
        lb_pass_current["justify"] = tk.LEFT
        lb_pass_current.pack(side=tk.LEFT, pady=5)

        pass_current = tk.Entry(primeiroContainer, show="*")
        pass_current["width"] = 30
        pass_current.pack(side=tk.RIGHT, pady=5)

        lb_pass_new = tk.Label(segundoContainer, text="New password:", anchor="w")
        lb_pass_new["width"] = 30
        lb_pass_new["justify"] = tk.LEFT
        lb_pass_new.pack(side=tk.LEFT, pady=5)

        pass_new1 = tk.Entry(segundoContainer, show="*")
        pass_new1["width"] = 30
        pass_new1.pack(side=tk.RIGHT, pady=5)

        lb_pass_new = tk.Label(terceiroContainer, text="New Password again:", anchor="w")
        lb_pass_new["width"] = 30
        lb_pass_new["justify"] = tk.LEFT
        lb_pass_new.pack(side=tk.LEFT, pady=5)

        pass_new2 = tk.Entry(terceiroContainer, show="*")
        pass_new2["width"] = 30
        pass_new2.pack(side=tk.RIGHT, pady=5)

        botao_Finish = tk.Button(quartoContainer, command=lambda: master.switch_frame(SelectUser, passwdNG))
        botao_Finish["text"] = "Finish"
        botao_Finish["width"] = 58
        botao_Finish.pack(pady=5)

class CreateUser(tk.Frame):
    def __init__(self, master, passwdNG, data=None):
        tk.Frame.__init__(self, master)

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

        print(data)

        titulo = tk.Label(titleContainer, text=" -- Create User -- ")
        titulo["font"] = ("Arial", "15", "bold")
        titulo.pack()

        lb_username = tk.Label(primeiroContainer, text="Username:", anchor="w")
        lb_username["width"] = 30
        lb_username["justify"] = tk.LEFT
        lb_username.pack(side=tk.LEFT, pady=5)

        username = tk.Entry(primeiroContainer, show="*")
        username["width"] = 30
        username.pack(side=tk.RIGHT, pady=5)

        lb_pass = tk.Label(segundoContainer, text="Password:", anchor="w")
        lb_pass["width"] = 30
        lb_pass["justify"] = tk.LEFT
        lb_pass.pack(side=tk.LEFT, pady=5)

        password1 = tk.Entry(segundoContainer, show="*")
        password1["width"] = 30
        password1.pack(side=tk.RIGHT, pady=5)

        lb_pass_new = tk.Label(terceiroContainer, text="Password again:", anchor="w")
        lb_pass_new["width"] = 30
        lb_pass_new["justify"] = tk.LEFT
        lb_pass_new.pack(side=tk.LEFT, pady=5)

        password2 = tk.Entry(terceiroContainer, show="*")
        password2["width"] = 30
        password2.pack(side=tk.RIGHT, pady=5)

        botao_Finish = tk.Button(quartoContainer, command=lambda: master.switch_frame(Login, passwdNG))
        botao_Finish["text"] = "Finish"
        botao_Finish["width"] = 58
        botao_Finish.pack(pady=5)
  
  
  
if __name__ == "__main__":
    
    backend_passwd = Psswd()
    app = SampleApp(backend_passwd)
    app.title("NEW PASSWD")
    app.geometry("500x200")
    app.mainloop()
