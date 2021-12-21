from pymongo import MongoClient

class DbFunc():
    def __init__(self):
        #!Inicializando conexão com o mongoDB
        self.client = MongoClient("localhost", 27017)
        self.db = self.client['LoginTkinter']
       
    def verifica_Login(self, nome):
        self.nome = nome
        self.dados = self.db.Users.find_one({"username": self.nome})
        return self.dados
    
    def verifica_Email(self, email):
        self.email = email
        self.dados = self.db.Users.find_one({"useremail": self.email})
        return self.dados
    
    def send_UserData(self, data):
        self.data = data
        self.dados = self.db.Users.insert_one(data)
        return self.dados
        


        
    
    



