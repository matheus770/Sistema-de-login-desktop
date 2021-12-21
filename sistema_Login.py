import tkinter as tk
from tkinter import *
from tkinter import Tk, messagebox
from tkinter import font
import re, sys, os

from Login.db import DbFunc 

class SistemaLogin:        
    def __init__(self):
        self.db = DbFunc() #! Importando conexão e funções do banco de dados
        
        #! Cores
        self.corBranca = "#feffff"
        self.corAzulLight2 = "#0893F0"
        self.corAzulLight3 = "#86CCFA"
        self.corAzulLight = "#9ECDEC"
        self.corRed = "#EE5151"

        #!self.window - Background
        self.window = Tk()
        self.window.title("Login")
        self.window.geometry('420x240') #! Witdh x Height
        self.window.configure(background=self.corAzulLight)
        self.window.resizable(width=FALSE, height=FALSE) #!Não editavel, Defini tamanho fixo 

        #!Criando texto de login
        self.texto_Login = Label(self.window, text="Name", width=10, background=self.corAzulLight3, font=('Arial 12 bold'), relief="groove")
        self.texto_Login.grid(column=1, row=1, padx=10, pady=10)
        #!Criando entry de dados de login
        self.entry_Login = Entry(self.window, width=25, relief='solid', bd=2, font=('Arial 12'),)
        self.entry_Login.grid(column=2, row=1, padx=20)

        #!Criando texto de password
        self.texto_Password = Label(self.window, text="Password", width=10, background=self.corAzulLight3, font=('Arial 12 bold'),  relief="groove")
        self.texto_Password.grid(column=1, row=2, )
        #!Criando entry de dados de Password
        self.entry_Password = Entry(self.window, width=25, relief='solid', bd=2, show="*", font=('Arial 12'))
        self.entry_Password.grid(column=2, row=2, )
        
        #!Criando Caixa para linkar os botoes Login e cadastro
        self.entry_Caixa = Entry(self.window, relief="solid", bd=2, width=30)
        self.entry_Caixa.grid(column=2, row=3, pady=30)
        #!Criando Botão de Login
        self.button_Login = Button(self.entry_Caixa, text="Sign in", width=8, relief="raised", background=self.corAzulLight2, fg=self.corBranca, command=lambda:self.login_ver())
        self.button_Login.grid(column=0, row=1,)

        #!Criando Botão de Cadastro
        self.button_Cadastre = Button(self.entry_Caixa, text="Sign up", width=8, relief="raised", background=self.corAzulLight2, fg=self.corBranca, command=lambda:self.tela_Login_Registro())
        self.button_Cadastre.grid(column=1, row=1,)
        #!Criando Botão de Sair
        self.button_Exit = Button(self.window, text="Exit", width=8, relief="solid", background=self.corRed, fg=self.corBranca, command=self.window.quit)
        self.button_Exit.grid(column=2, row=4,)

        mainloop() #!Rodando
    
    def login_ver(self):
        #!Pegando dados da entrada de dados do usuario 
        self.username = self.entry_Login.get()
        self.password = self.entry_Password.get()
        
        self.consul_login = self.db.verifica_Login(self.username)
        if(self.username == '' or self.password == ''):
            return tk.messagebox.showerror(title="ERRO", message="Campos de usuário e senhas impossiveis ficar em branco")
        elif(self.consul_login == None):
            return tk.messagebox.showerror(title="ERRO", message="Usuário não encontrado.")
        elif(self.consul_login != None):
            if(self.consul_login["userpassword"] == self.entry_Password.get()):
                self.login_Sucessfull(self.username)
                return 
            else:
                return tk.messagebox.showerror(title="ERRO", message="Senha errada.")
    
    def login_Sucessfull(self, username):
        self.username = username
        
        self.button_Exit.destroy()
        self.button_Cadastre.destroy()
        self.button_Login.destroy()
        self.entry_Caixa.destroy()
        self.entry_Password.destroy()
        self.texto_Password.destroy()
        self.entry_Login.destroy()
        self.texto_Login.destroy()
        
        self.welcome_text = Label(self.window, text=(f"Seja bem-vindo {self.username}"), width=25, background=self.corAzulLight3, font=('Arial 12 '), relief="groove", justify='center')
        self.welcome_text.grid(column=0, row=0,padx= 100,)
        
        self.button_Logout = Button(self.window, text="Logout", width=8, relief="solid", background=self.corRed, fg=self.corBranca, command=self.restart_program)
        self.button_Logout.grid(column=0, row=4,pady=50)
        
        tk.messagebox.showinfo(title="Bem Vindo", message="Login feito com sucesso.")
        return
    
    def tela_Login_Registro(self):
        self.button_Cadastre.destroy()
        self.button_Login.destroy()
        self.entry_Caixa.destroy()
        self.button_Exit.destroy()
        
        self.texto_Password_Confirm = Label(self.window, text="Password", width=10, background=self.corAzulLight3, font=('Arial 12 bold'),  relief="groove")
        self.texto_Password_Confirm.grid(column=1, row=3, padx=10, pady=10)
        self.entry_Password_Confirm = Entry(self.window, width=25, relief='solid', bd=2, show="*", font=('Arial 12'))
        self.entry_Password_Confirm.grid(column=2, row=3, padx=10, pady=10)
        
        self.texto_Email = Label(self.window, text="Email", width=10, background=self.corAzulLight3, font=('Arial 12 bold'), relief="groove")
        self.texto_Email.grid(column=1, row=4, padx=10, pady=10)
        self.entry_Email = Entry(self.window, width=25, relief='solid', bd=2, font=('Arial 12'))
        self.entry_Email.grid(column=2, row=4, )
        
        self.button_Registre = Button(self.window, text="Register", width=8, relief="raised", background=self.corAzulLight2, fg=self.corBranca, command=lambda:self.send_LoginData())
        self.button_Registre.grid(column=2, row=5)
        
        self.button_Exit = Button(self.window, text="Exit", width=8, relief="solid", background=self.corRed, fg=self.corBranca, command=self.restart_program)
        self.button_Exit.grid(column=2, row=6, pady=10)
        return 
    
    
    def send_LoginData(self):
        #!Pegando dados da entrada de dados do usuario 
        self.userlogin = self.entry_Login.get()
        self.password = self.entry_Password.get()
        self.password_confirm = self.entry_Password_Confirm.get()
        self.email = self.entry_Email.get()
        
        self.verifica_username = self.db.verifica_Login(self.userlogin)
        
        if(self.userlogin == '' or self.password == ''or self.password_confirm == ''  or self.email == ''):
            tk.messagebox.showerror(title="ERRO", message="Erro, Campo de dados vazio.")
        elif(self.verifica_username != None):
            tk.messagebox.showerror(title="ERRO", message="Erro, Nome de usuário já existente.")
        elif(len(self.userlogin) <= 6 or len(self.password) <= 6):
            tk.messagebox.showerror(title="ERRO", message="Erro, Tamanho minimo de 6 caracteres para login e password.")
        elif(self.password != self.password_confirm):
            tk.messagebox.showerror(title="ERRO", message="Erro, As senhas devem ser identicas.")
        elif(self.validate_email(self.email) == False):
            tk.messagebox.showerror(title="ERRO", message="Erro, Email Invalido.")
        elif(self.db.verifica_Email(self.email) != None):
            tk.messagebox.showerror(title="ERRO", message="Erro, Email ja cadastrado.")
        else:
            self.data = {
                "username": self.userlogin,
                "userpassword": self.password,
                "useremail": self.email,
            }
            try:
                self.db.send_UserData(self.data)
                tk.messagebox.showinfo(title="Sucesso", message="Usuário cadastrado com sucesso.")
                return self.restart_program()
            except:
                return tk.messagebox.showerror(title="ERRO", message="Erro, Impossivel cadastrar usuário.")
        
    def validate_email(self, email):
        self.regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        self.email = email
        if(re.fullmatch(self.regex, self.email)):
            return True
        else:
            return False
    
    def restart_program(self):
        self.python = sys.executable
        os.execl(self.python, self.python, * sys.argv)

