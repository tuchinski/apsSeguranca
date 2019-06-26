<<<<<<< HEAD
import tkinter as tk
from passwdNG import Psswd


class SampleApp(tk.Tk):
    def __init__(self, psw):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(Login, psw)

    def switch_frame(self, frame_class, psw):
        new_frame = frame_class(self, psw)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame["padx"] = 10
        self._frame["pady"] = 10
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master, passwdNG):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Start page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go to page one",
                  command=lambda: master.switch_frame(PageOne)).pack()
        tk.Button(self, text="Go to page two",command=lambda: master.switch_frame(PageTwo)).pack()

class PageOne(tk.Frame):
    def __init__(self, master, passwdNG):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='blue')
        tk.Label(self, text="Page one", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page", command=lambda: master.switch_frame(StartPage)).pack()

class SelectUser(tk.Frame):
    def __init__(self, master, passwdNG):
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

        bottao_select = tk.Button(terceiroContainer, text="SELECT", command=lambda: master.switch_frame(StartPage))
        bottao_select["width"] = 5
        bottao_select["height"] = 10
        
        bottao_select.pack(side=tk.RIGHT, pady=5, padx=1)

class Login(tk.Frame):
    def __init__(self, master, passwdNG):
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

        senha = tk.Entry(segundoContainer)
        senha["width"] = 50
        senha.pack(side=tk.RIGHT, pady=5)

        botao_login = tk.Button(terceiroContainer, command=lambda: master.switch_frame(SelectUser, passwdNG))
        botao_login["text"] = "Login"
        botao_login["width"] = 58
        botao_login.pack(pady=5)
  
=======
from tkinter import *
from passwdNG import Psswd
  
class Application:
    def __init__(self, master, passwdNG):
        self.fontePadrao = ("Arial", "10")
        master.title("PasswdNG")

        ###### DEFINE CONTAINER 01 ######
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
  
        ###### DEFINE CONTAINER 02 ######
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
  
        ###### DEFINE CONTAINER 03 ######
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
  
        ###### DEFINE CONTAINER 04 ######
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        ###### DEFINE CONTAINER 05 ######
        self.quintoContainer = Frame(master)
        self.quintoContainer["padx"] = 20
        self.quintoContainer.pack()
    
        self.init_window()
    
    def init_window(self):
        self.titulo = Label(self.primeiroContainer, text="Dados do usuário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
  
        self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
  
        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)
  
        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)
  
        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)
  
        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()
  
        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

        self.lbl = Label(self.quintoContainer)  
        self.lbl["text"] = "List of Users"
        self.lbl["font"] = ("Calibri", "8")

        list_users = passwdNG.get_file_shadow()
        tonkes = passwdNG.get_tokens_by_user_shadow()
       
        i = 1
        self.listbox = Listbox(self.quintoContainer)
        self.listbox["width"] = 100
        for line in tonkes:
            self.listbox.insert(i,line[0])
            i = i + 1

        self.lbl.pack()  
        self.listbox.pack()
>>>>>>> 079374f3af4eeb6be57286addd58345d8c35371f
  
    #Método verificar senha
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "usuariodevmedia" and senha == "dev":
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Erro na autenticação"
  
  
<<<<<<< HEAD
if __name__ == "__main__":
    
    backend_passwd = Psswd()
    app = SampleApp(backend_passwd)
    app.title("NEW PASSWD")
    app.geometry("500x200")
    app.mainloop()
=======
root = Tk()
passwdNG = Psswd()
Application(root, passwdNG)
root.mainloop()
>>>>>>> 079374f3af4eeb6be57286addd58345d8c35371f
