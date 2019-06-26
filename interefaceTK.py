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
  
  
    #Método verificar senha
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "usuariodevmedia" and senha == "dev":
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Erro na autenticação"
  
  
if __name__ == "__main__":
    
    backend_passwd = Psswd()
    app = SampleApp(backend_passwd)
    app.title("NEW PASSWD")
    app.geometry("500x200")
    app.mainloop()
