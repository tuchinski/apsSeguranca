import tkinter as tk
import re
from passwdNG import Psswd
import time
from tkcalendar import Calendar, DateEntry


class SampleApp(tk.Tk):
    def __init__(self, psw):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(GerenciarSenha, psw)

    def switch_frame(self, frame_class, psw, data=None):
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

        self.lbl = tk.Label(
            segundoContainer, text="List of Users:", anchor="w")
        self.lbl["font"] = ("Calibri", "8")
        self.lbl.pack(pady=5)

        list_users = passwdNG.get_file_shadow()
        tonkes = passwdNG.get_tokens_by_user_shadow()
        i = 1
        self.listbox = tk.Listbox(terceiroContainer)
        self.listbox["width"] = 50
        for line in tonkes:
            self.listbox.insert(i, line[0])
            i = i + 1

        self.listbox.pack(side=tk.LEFT, pady=5, padx=1)

        self.bottao_select = tk.Button(terceiroContainer, text="SELECT", command=lambda: master.switch_frame(
            EditPass, passwdNG, str(self.listbox.get(tk.ANCHOR))))
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

        self.nomeLabel = tk.Label(
            primeiroContainer, text="Username:", anchor="w")
        self.nomeLabel["width"] = 10
        self.nomeLabel["justify"] = tk.LEFT
        self.nomeLabel.pack(side=tk.LEFT, pady=5)

        self.username = tk.Entry(primeiroContainer)
        self.username["width"] = 50
        self.username.pack(side=tk.RIGHT, pady=5)

        self.senhaLabel = tk.Label(
            segundoContainer, text="Password:", anchor="w")
        self.senhaLabel["width"] = 10
        self.senhaLabel["justify"] = tk.LEFT
        self.senhaLabel.pack(side=tk.LEFT, pady=5)

        self.password = tk.Entry(segundoContainer, show="*")
        self.password["width"] = 50
        self.password.pack(side=tk.RIGHT, pady=5)

        self.botao_login = tk.Button(terceiroContainer, command=lambda: self.get_data_login_user(
            str(self.username.get()), str(self.password.get())))
        self.botao_login["text"] = "Login"
        self.botao_login["width"] = 58
        self.botao_login.pack(pady=5)

        self.lb_alert = tk.Label(quartoContainer)
        self.lb_alert["text"] = ""
        self.lb_alert["font"] = ("Arial", "9", "bold")
        self.lb_alert.pack()

    def get_data_login_user(self, username, password):
        if ((username and password) != ""):
            self.lb_alert["text"] = "Sucessfull Login."
            self.lb_alert["fg"] = "green"
            self.master.switch_frame(Painel, self.passwdNG)
        else:
            self.lb_alert["text"] = "Please fill in all fields."
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

        self.botao_create_user = tk.Button(
            primeiroContainer, command=lambda: master.switch_frame(CreateUser, passwdNG))
        self.botao_create_user["text"] = "Create User"
        self.botao_create_user["width"] = 58
        self.botao_create_user.pack(pady=5)

        self.botao_change_pass_user = tk.Button(
            primeiroContainer, command=lambda: master.switch_frame(SelectUser, passwdNG))
        self.botao_change_pass_user["text"] = "Change Pass User"
        self.botao_change_pass_user["width"] = 58
        self.botao_change_pass_user.pack(pady=5)

        self.botao_change_pass_user = tk.Button(
            primeiroContainer, command=lambda: master.switch_frame(SelectUser, passwdNG))
        self.botao_change_pass_user["text"] = "Recover Password"
        self.botao_change_pass_user["width"] = 58
        self.botao_change_pass_user.pack(pady=5)

        self.botao_adm_paienl = tk.Button(
            primeiroContainer, command=lambda: master.switch_frame(PainelAdm, passwdNG))
        self.botao_adm_paienl["text"] = "Adm Painel"
        self.botao_adm_paienl["width"] = 58
        self.botao_adm_paienl.pack(pady=5)


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

        self.lb_pass_current = tk.Label(
            primeiroContainer, text="Current password:", anchor="w")
        self.lb_pass_current["width"] = 30
        self.lb_pass_current["justify"] = tk.LEFT
        self.lb_pass_current.pack(side=tk.LEFT, pady=5)

        self.pass_current = tk.Entry(primeiroContainer, show="*")
        self.pass_current["width"] = 30
        self.pass_current.pack(side=tk.RIGHT, pady=5)

        self.lb_pass_new = tk.Label(
            segundoContainer, text="New password:", anchor="w")
        self.lb_pass_new["width"] = 30
        self.lb_pass_new["justify"] = tk.LEFT
        self.lb_pass_new.pack(side=tk.LEFT, pady=5)

        self.pass_new1 = tk.Entry(segundoContainer, show="*")
        self.pass_new1["width"] = 30
        self.pass_new1.pack(side=tk.RIGHT, pady=5)

        self.lb_pass_new = tk.Label(
            terceiroContainer, text="New Password again:", anchor="w")
        self.lb_pass_new["width"] = 30
        self.lb_pass_new["justify"] = tk.LEFT
        self.lb_pass_new.pack(side=tk.LEFT, pady=5)

        self.pass_new2 = tk.Entry(terceiroContainer, show="*")
        self.pass_new2["width"] = 30
        self.pass_new2.pack(side=tk.RIGHT, pady=5)

        self.botao_back = tk.Button(
            quartoContainer, text="<-", command=lambda: self.master.switch_frame(Painel, self.passwdNG))
        self.botao_back["width"] = 1
        self.botao_back.pack(side=tk.LEFT)

        self.botao_Finish = tk.Button(quartoContainer, command=lambda: self.get_data_edit_user(
            str(self.pass_current.get()), str(self.pass_new1.get()), str(self.pass_new2.get())))
        self.botao_Finish["text"] = "Finish"
        self.botao_Finish["width"] = 58
        self.botao_Finish.pack(side=tk.RIGHT, pady=5)

        self.lb_alert = tk.Label(quartoContainer)
        self.lb_alert["text"] = ""
        self.lb_alert["font"] = ("Arial", "9", "bold")
        self.lb_alert.pack()

    def get_data_edit_user(self, username, pass1, pass2):
        if ((username and pass1 and pass2) != ""):
            if pass1 == pass2:
                if (self.valid_password(pass1) == True):
                    self.lb_alert["text"] = "The user was edited."
                    self.lb_alert["fg"] = "green"
                    time.sleep(0.3)
                    self.master.switch_frame(SelectUser, self.passwdNG)
            else:
                self.lb_alert["text"] = "The passwords do not match."
                self.lb_alert["fg"] = "red"
        else:
            self.lb_alert["text"] = "Please fill in all fields."
            self.lb_alert["fg"] = "red"

    
    def return_count_regex_text(self, text, regex_string, qtd_defined):
        cont = 0
        for i in text:
            thereare = re.match(regex_string, i)
            if thereare != None:
                cont = cont + 1
        
        if int(qtd_defined) == int(cont) or int(qtd_defined) < int(cont):
            return True
        else:
            return False

    def valid_password(self, password):
        rules_password = self.passwdNG.get_value_pass()
        num = self.return_count_regex_text(password, "\d", int(rules_password[2]))
        low = self.return_count_regex_text(password, "[a-z]", int(rules_password[0]))
        upp = self.return_count_regex_text(password, "[A-Z]", int(rules_password[1]))
        syb = self.return_count_regex_text(password, "(?=.*?[#?!@$%^&*-])", int(rules_password[3]))

        if(num == False):
            print(self.return_count_regex_text(password, "\d", int(rules_password[2])))
            self.lb_alert["text"] = "Passwords should contain " + str(rules_password[2]) + " or more numbers" 
            self.lb_alert["fg"] = "red"

        if(low == False):
            self.lb_alert["text"] = "Passwords should contain " + str(rules_password[2]) + " or more lower case characters" 
            self.lb_alert["fg"] = "red"
            
        if(upp == False):
            self.lb_alert["text"] = "Passwords should contain " + str(rules_password[0]) + " or more uppercase case characters" 
            self.lb_alert["fg"] = "red"

        if(syb == False):
            self.lb_alert["text"] = "Passwords should contain " + str(rules_password[3]) + " or more symbols" 
            self.lb_alert["fg"] = "red"
        
        if(int(len(password)) >= int(rules_password[4])):
            qtd = True
        else:
            self.lb_alert["text"] = "Passwords should contain " + str(rules_password[4]) + " or more characters" 
            self.lb_alert["fg"] = "red"

        if ((num and low and upp and syb and qtd) == True):
            return True
        else:
            return False

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

        ###### DEFINE CONTAINER 05 ######
        quintoContainer = tk.Frame(self)
        quintoContainer.pack()

        ###### DEFINE CONTAINER 02 ######
        segundoContainer = tk.Frame(self)
        segundoContainer.pack()

        ###### DEFINE CONTAINER 03 ######
        terceiroContainer = tk.Frame(self)
        terceiroContainer.pack()

        ###### DEFINE CONTAINER Name ######
        nameContainer = tk.Frame(self)
        nameContainer.pack()

        ###### DEFINE CONTAINER Phone ######
        phoneContainer = tk.Frame(self)
        phoneContainer.pack()

        ###### DEFINE CONTAINER 04 ######
        quartoContainer = tk.Frame(self)
        quartoContainer.pack()

        perguntaContainer = tk.Frame(self)
        perguntaContainer.pack()

        respostaContainer = tk.Frame(self)
        respostaContainer.pack()

        ###### DEFINE CONTAINER Other ######
        otherContainer = tk.Frame(self)
        otherContainer.pack()

        ###### DEFINE CONTAINER 05 ######
        quintoContainer = tk.Frame(self)
        quintoContainer.pack()

        ###### DEFINE CONTAINER 06 ######
        sextoContainer = tk.Frame(self)
        sextoContainer.pack()

        setimoContainer = tk.Frame(self)
        setimoContainer.pack()

        oitavoContainer = tk.Frame(self)
        oitavoContainer.pack()

        self.titulo = tk.Label(titleContainer, text=" -- Create New User -- ")
        self.titulo["font"] = ("Arial", "15", "bold")
        self.titulo.pack()

        self.lb_username = tk.Label(
            primeiroContainer, text="Username:", anchor="w")
        self.lb_username["width"] = 30
        self.lb_username["justify"] = tk.LEFT
        self.lb_username.pack(side=tk.LEFT, pady=5)

        self.username = tk.Entry(primeiroContainer, show="")
        self.username["width"] = 30
        self.username.pack(side=tk.RIGHT, pady=5)

        self.lb_pass = tk.Label(segundoContainer, text="Password:", anchor="w")
        self.lb_pass["width"] = 30
        self.lb_pass["justify"] = tk.LEFT
        self.lb_pass.pack(side=tk.LEFT, pady=5)

        self.password1 = tk.Entry(segundoContainer, show="*")
        self.password1["width"] = 30
        self.password1.pack(side=tk.RIGHT, pady=5)

        self.lb_pass_new = tk.Label(
            terceiroContainer, text="Password again:", anchor="w")
        self.lb_pass_new["width"] = 30
        self.lb_pass_new["justify"] = tk.LEFT
        self.lb_pass_new.pack(side=tk.LEFT, pady=5)

        self.password2 = tk.Entry(terceiroContainer, show="*")
        self.password2["width"] = 30
        self.password2.pack(side=tk.RIGHT, pady=5)

        self.lb_name = tk.Label(nameContainer, text="Full Name:", anchor="w")
        self.lb_name["width"] = 30
        self.lb_name["justify"] = tk.LEFT
        self.lb_name.pack(side=tk.LEFT, pady=5)

        self.name = tk.Entry(nameContainer, show="")
        self.name["width"] = 30
        self.name.pack(side=tk.RIGHT, pady=5)

        self.lb_tell = tk.Label(phoneContainer, text="Tell Phone:", anchor="w")
        self.lb_tell["width"] = 30
        self.lb_tell["justify"] = tk.LEFT
        self.lb_tell.pack(side=tk.LEFT, pady=5)

        self.tell = tk.Entry(phoneContainer, show="")
        self.tell["width"] = 30
        self.tell.pack(side=tk.RIGHT, pady=5)

        self.questions = ["Qual o nome do seu primeiro animal de estimação?",
                          "Qual sua comida favorita ?",
                          "Qual o nome do seu melhor amigo de infancia?",
                          "Qual o nome da sua professora favorita ?",
                          "Em que cidade voce nasceu ?",
                          "Qual sua série favorita ?",
                          "Onde sua mão nasceu ?",
                          "Onde seu pai nasceu ?"
                          ]

        self.lb_pergunta = tk.Label(
            perguntaContainer, text="Question:", anchor="w")
        self.lb_pergunta["width"] = 10
        self.lb_pergunta["justify"] = tk.LEFT
        self.lb_pergunta.pack(side=tk.LEFT, pady=5)

        self.variable = tk.StringVar(perguntaContainer)
        self.variable.set(self.questions[1])  # default value

        self.box_pergunta = tk.OptionMenu(
            perguntaContainer, self.variable, *self.questions)
        self.box_pergunta["width"] = 46
        self.box_pergunta.pack(side=tk.RIGHT, pady=5)

        self.lb_resposta = tk.Label(
            respostaContainer, text="Answer:", anchor="w")
        self.lb_resposta["width"] = 30
        self.lb_resposta["justify"] = tk.LEFT
        self.lb_resposta.pack(side=tk.LEFT, pady=5)

        self.resposta = tk.Entry(respostaContainer, show="")
        self.resposta["width"] = 30
        self.resposta.pack(side=tk.RIGHT, pady=5)

        self.lb_other = tk.Label(otherContainer, text="Other:", anchor="w")
        self.lb_other["width"] = 30
        self.lb_other["justify"] = tk.LEFT
        self.lb_other.pack(side=tk.LEFT, pady=5)

        self.other = tk.Text(otherContainer)
        self.other["width"] = 30
        self.other["height"] = 3
        self.other.pack(side=tk.RIGHT, pady=5)

        self.lb_email = tk.Label(quartoContainer, text="Email:", anchor="w")
        self.lb_email["width"] = 30
        self.lb_email["justify"] = tk.LEFT
        self.lb_email.pack(side=tk.LEFT, pady=5)

        self.email = tk.Entry(quartoContainer, show="")
        self.email["width"] = 30
        self.email.pack(side=tk.RIGHT, pady=5)

        self.lb_validate = tk.Label(
            quintoContainer, text='I want to choose an expiration date:', anchor="w")
        self.lb_validate["width"] = 30
        self.lb_validate["justify"] = tk.LEFT
        self.lb_validate.pack(side=tk.LEFT, pady=5)

        self.var = tk.IntVar()
        self.btn_radio_yes = tk.Radiobutton(
            quintoContainer, text="Yes", variable=self.var, value=1, command=self.sel)
        self.btn_radio_yes["width"] = 15
        self.btn_radio_yes.pack(side=tk.RIGHT, pady=5)

        self.btn_radio_no = tk.Radiobutton(
            quintoContainer, text="No", variable=self.var, value=2, command=self.sel)
        self.btn_radio_no["width"] = 15
        self.btn_radio_no.pack(side=tk.RIGHT, pady=5)

        self.lb_date1 = tk.Label(
            sextoContainer, text='Validade-Inicio:', anchor="w")
        self.lb_date1["width"] = 15
        self.lb_date1["justify"] = tk.LEFT

        self.cal1 = DateEntry(sextoContainer, foreground='white', anchor="w", )

        self.lb_date2 = tk.Label(
            sextoContainer, text='Validade-Final:', anchor="w")
        self.lb_date2["width"] = 15
        self.lb_date2["justify"] = tk.LEFT

        self.cal2 = DateEntry(sextoContainer, foreground='white', anchor="c")

        self.botao_back = tk.Button(
            setimoContainer, text="<-", command=lambda: self.master.switch_frame(Painel, self.passwdNG))
        self.botao_back["width"] = 1
        self.botao_back.pack(side=tk.LEFT)

        self.botao_Finish = tk.Button(setimoContainer, command=lambda: self.get_data_new_user(self.username.get(), self.password1.get(), self.password2.get(), self.name.get(), self.tell.get(), self.email.get(), self.variable.get(), self.resposta.get(), self.other.get("1.0", tk.END), self.var.get(), self.cal1.get_date(), self.cal2.get_date()))
        self.botao_Finish["text"] = "Finish"
        self.botao_Finish["width"] = 58
        self.botao_Finish.pack(side=tk.LEFT, pady=5)

        self.lb_alert = tk.Label(oitavoContainer)
        self.lb_alert["text"] = ""
        self.lb_alert["font"] = ("Arial", "9", "bold")
        self.lb_alert.pack()

    def sel(self):
        if str(self.var.get()) == "1":
            self.lb_date1.pack(side=tk.LEFT, pady=5)
            self.cal1.pack(side=tk.LEFT, pady=5)
            self.lb_date2.pack(side=tk.LEFT, pady=5)
            self.cal2.pack(side=tk.RIGHT, pady=5)
        else:
            self.lb_date1.pack_forget()
            self.cal1.pack_forget()
            self.lb_date2.pack_forget()
            self.cal2.pack_forget()
    
    def return_count_regex_text(self, text, regex_string, qtd_defined):
        cont = 0
        for i in text:
            thereare = re.match(regex_string, i)
            if thereare != None:
                cont = cont + 1
        
        if int(qtd_defined) == int(cont) or int(qtd_defined) < int(cont):
            return True
        else:
            return False

    def valid_password(self, password):
        rules_password = self.passwdNG.get_value_pass()
        num = self.return_count_regex_text(password, "\d", int(rules_password[2]))
        low = self.return_count_regex_text(password, "[a-z]", int(rules_password[0]))
        upp = self.return_count_regex_text(password, "[A-Z]", int(rules_password[1]))
        syb = self.return_count_regex_text(password, "(?=.*?[#?!@$%^&*-])", int(rules_password[3]))

        if(num == False):
            print(self.return_count_regex_text(password, "\d", int(rules_password[2])))
            self.lb_alert["text"] = "Passwords should contain " + str(rules_password[2]) + " or more numbers" 
            self.lb_alert["fg"] = "red"

        if(low == False):
            self.lb_alert["text"] = "Passwords should contain " + str(rules_password[2]) + " or more lower case characters" 
            self.lb_alert["fg"] = "red"
            
        if(upp == False):
            self.lb_alert["text"] = "Passwords should contain " + str(rules_password[0]) + " or more uppercase case characters" 
            self.lb_alert["fg"] = "red"

        if(syb == False):
            self.lb_alert["text"] = "Passwords should contain " + str(rules_password[3]) + " or more symbols" 
            self.lb_alert["fg"] = "red"
        
        if(int(len(password)) >= int(rules_password[4])):
            qtd = True
        else:
            self.lb_alert["text"] = "Passwords should contain " + str(rules_password[4]) + " or more characters" 
            self.lb_alert["fg"] = "red"

        if ((num and low and upp and syb and qtd) == True):
            return True
        else:
            return False

    def get_data_new_user(self, username, pass1, pass2, name, tell, email, var1, res, other, var2, ca11, cal2):
        if ((username and pass1 and pass2) != ""):
            if pass1 == pass2:
                if (self.valid_password(pass1)):
                    self.lb_alert["text"] = "The user was created."
                    self.lb_alert["fg"] = "green"
                    print(self.passwdNG.get_file_shadow())

            else:
                self.lb_alert["text"] = "The passwords do not match."
                self.lb_alert["fg"] = "red"
        else:
            self.lb_alert["text"] = "Please fill in all fields."
            self.lb_alert["fg"] = "red"


class GerenciarSenha(tk.Frame):
    def __init__(self, master, passwdNG, data=None):
        tk.Frame.__init__(self, master)
        self.passwdNG = passwdNG

        ###### DEFINE CONTAINER TITULO ######
        titleContainer = tk.Frame(self)
        titleContainer.pack()

        ###### DEFINE CONTAINER Lower Case ######
        lowerContainer = tk.Frame(self)
        lowerContainer.pack()

        ###### DEFINE CONTAINER Upper Case ######
        upperContainer = tk.Frame(self)
        upperContainer.pack()

        ###### DEFINE CONTAINER qtd.number ######
        qtdNumberContainer = tk.Frame(self)
        qtdNumberContainer.pack()

        ###### DEFINE CONTAINER qtd.simbolos ######
        qtdSimbolosContainer = tk.Frame(self)
        qtdSimbolosContainer.pack()

        ###### DEFINE CONTAINER tamanho senha ######
        tamanhoSenhaContainer = tk.Frame(self)
        tamanhoSenhaContainer.pack()

        alertContainer = tk.Frame(self)
        alertContainer.pack()

        ###### DEFINE CONTAINER voltar ######
        voltar = tk.Frame(self)
        voltar.pack()

        self.titulo = tk.Label(titleContainer, text=" -- Gerenciar Senha -- ")
        self.titulo["font"] = ("Arial", "15", "bold")
        self.titulo.pack()

        self.lb_lowerCase = tk.Label(
            lowerContainer, text="Quantidade de caracteres minúsculos(a - z)", anchor="w")
        self.lb_lowerCase["width"] = 50
        self.lb_lowerCase["justify"] = tk.LEFT
        self.lb_lowerCase.pack(side=tk.LEFT, pady=5)

        self.qtdLower = tk.Entry(lowerContainer)
        self.qtdLower["width"] = 10
        self.qtdLower.pack(side=tk.RIGHT, pady=5)

        self.lb_upperCase = tk.Label(
            upperContainer, text="Quantidade de caracteres maiusculos (A - Z)", anchor="w")
        self.lb_upperCase["width"] = 50
        self.lb_upperCase["justify"] = tk.LEFT
        self.lb_upperCase.pack(side=tk.LEFT, pady=5)

        self.qtdUpper = tk.Entry(upperContainer)
        self.qtdUpper["width"] = 10
        self.qtdUpper.pack(side=tk.RIGHT, pady=5)

        self.lb_qtdNumeros = tk.Label(
            qtdNumberContainer, text="Quantidade de numeros(0 - 9)", anchor="w")
        self.lb_qtdNumeros["width"] = 50
        self.lb_qtdNumeros["justify"] = tk.LEFT
        self.lb_qtdNumeros.pack(side=tk.LEFT, pady=5)

        self.qtdNumeros = tk.Entry(qtdNumberContainer)
        self.qtdNumeros["width"] = 10
        self.qtdNumeros.pack(side=tk.RIGHT, pady=5)

        self.lb_qtdSimbolos = tk.Label(
            qtdSimbolosContainer, text="Quantidade de simbolos (!@$-)(*&¨%)", anchor="w")
        self.lb_qtdSimbolos["width"] = 50
        self.lb_qtdSimbolos["justify"] = tk.LEFT
        self.lb_qtdSimbolos.pack(side=tk.LEFT, pady=5)

        self.qtdSimbolos = tk.Entry(qtdSimbolosContainer)
        self.qtdSimbolos["width"] = 10
        self.qtdSimbolos.pack(side=tk.RIGHT, pady=5)

        self.lb_tamanhodaSenha = tk.Label(
            tamanhoSenhaContainer, text="Tamanho da senha", anchor="w")
        self.lb_tamanhodaSenha["width"] = 50
        self.lb_tamanhodaSenha["justify"] = tk.LEFT
        self.lb_tamanhodaSenha.pack(side=tk.LEFT, pady=5)

        self.tamanhoSenha = tk.Entry(tamanhoSenhaContainer)
        self.tamanhoSenha["width"] = 10
        self.tamanhoSenha.pack(side=tk.RIGHT, pady=5)

        self.btn_ok = tk.Button(
            voltar, text="Concluir", command=lambda: self.funcao_ok(self.qtdLower.get(), self.qtdUpper.get(),
                                                                    self.qtdNumeros.get(), self.qtdSimbolos.get(), self.tamanhoSenha.get()))
        self.btn_ok["width"] = 50
        self.btn_ok.pack(side=tk.RIGHT)

        self.botao_back = tk.Button(
            voltar, text="<-", command=lambda: self.master.switch_frame(PainelAdm, self.passwdNG))
        self.botao_back["width"] = 1
        self.botao_back.pack(side=tk.RIGHT)

        self.lb_alert = tk.Label(alertContainer)
        self.lb_alert["text"] = ""
        self.lb_alert["font"] = ("Arial", "9", "bold")
        self.lb_alert.pack()

    def funcao_ok(self, lower, upper, numero, simbolos, tamSenha):
        if lower.isnumeric() and upper.isnumeric() and numero.isnumeric() and simbolos.isnumeric() and tamSenha.isnumeric():
            if int(tamSenha) >= 6:
                self.lb_alert["text"] = "Sucess."
                self.lb_alert["fg"] = "green"
                self.passwdNG.values_pass(self.qtdLower.get(), self.qtdUpper.get(), self.qtdNumeros.get(), self.qtdSimbolos.get(), self.tamanhoSenha.get())
            else:
                self.lb_alert["text"] = "The minimum size of your password must be 6 digits"
                self.lb_alert["fg"] = "red"

        else:
            self.lb_alert["text"] = "Just numbers."
            self.lb_alert["fg"] = "red"

    # def valid_password_2(self, password, lower, upper, numeros, simbols, tam):
    #     digit = re.search(r"\d", password)
    #     uppercase = re.search(r"[A-Z]{3}", password)
    #     lowercase = re.search(r"[a-z]{3}", password)
    #     symbol = re.search(
    #         r"[ !#$%@%&'()*+,-./[\\\]^_`{|}~"+r'"]{3}', password)

    #     print(str(len(str(password))), digit, uppercase, lowercase, symbol)
    #     print(len(str(password)))
    #     if len(str(password)) < tam:
    #         self.lb_alert["text"] = "Passwords should consist of" + \
    #             tam + " characters."
    #         self.lb_alert["fg"] = "red"
    #     if digit == None:
    #         self.lb_alert["text"] = "Passwords should contain digits [0-9]."
    #         self.lb_alert["fg"] = "red"
    #     if len(digit) < numeros:
    #         self.lb_alert["text"] = "Passwords should contain" + \
    #             numeros + " digits [0-9]."
    #         self.lb_alert["fg"] = "red"
    #     if uppercase == None:
    #         self.lb_alert["text"] = "Passwords should contain upper case characters."
    #         self.lb_alert["fg"] = "red"
    #     if len(uppercase) < upper:
    #         self.lb_alert["text"] = "Passwords should contain" + \
    #             upper + " upper case characters."
    #         self.lb_alert["fg"] = "red"
    #     if lowercase == None:
    #         self.lb_alert["text"] = "Passwords should contain lower case characters."
    #         self.lb_alert["fg"] = "red"
    #     if len(lowercase) < lower:
    #         self.lb_alert["text"] = "Passwords should contain" + \
    #             lower + " lower case characters."
    #         self.lb_alert["fg"] = "red"
    #     if symbol == None:
    #         self.lb_alert["text"] = "Passwords should contain symbols."
    #         self.lb_alert["fg"] = "red"
    #     if len(symbol) < simbols:
    #         self.lb_alert["text"] = "Passwords should contain" + \
    #             simbols + " symbols."
    #         self.lb_alert["fg"] = "red"

    #     if (digit != None and uppercase != None and lowercase != None and symbol != None):
    #         return (True)
    #     else:
    #         return (False)


class PainelAdm(tk.Frame):
    def __init__(self, master, passwdNG, data=None):
        tk.Frame.__init__(self, master)
        self.passwdNG = passwdNG

        ###### DEFINE CONTAINER TITULO ######
        titleContainer = tk.Frame(self)
        titleContainer.pack()

        ###### DEFINE CONTAINER linha Acoes ######
        acaoContainer = tk.Frame(self)
        acaoContainer.pack()

        ###### DEFINE CONTAINER gerenciar senha ######
        gerenciarsenha = tk.Frame(self)
        gerenciarsenha.pack()

        ###### DEFINE CONTAINER voltar ######
        voltar = tk.Frame(self)
        voltar.pack()

        self.titulo = tk.Label(titleContainer, text=" -- Painel do ADM -- ")
        self.titulo["font"] = ("Arial", "15", "bold")
        self.titulo.pack()

        self.lb_acao = tk.Label(acaoContainer, text="Ações", anchor="w")
        self.lb_acao["width"] = 30
        self.lb_acao["justify"] = tk.LEFT
        self.lb_acao.pack(side=tk.LEFT, pady=5)

        self.btn_gerenciarSenha = tk.Button(gerenciarsenha, text="Gerenciar Senha", command=lambda: master.switch_frame(
            GerenciarSenha, passwdNG, ""))
        self.btn_gerenciarSenha["width"] = 30
        self.btn_gerenciarSenha["justify"] = tk.LEFT
        self.btn_gerenciarSenha.pack(side=tk.LEFT, pady=5)

        self.botao_back = tk.Button(
            voltar, text="<-", command=lambda: self.master.switch_frame(Painel, self.passwdNG))
        self.botao_back["width"] = 1
        self.botao_back.pack(side=tk.LEFT)


if __name__ == "__main__":

    backend_passwd = Psswd()
    app = SampleApp(backend_passwd)
    app.title("NEW PASSWD")
    app.geometry("500x600")
    app.mainloop()
