from colorama import Fore, Back, Style
from smtpmail import mail
import pyodbc
import random
import string

brilho_on  = Fore.GREEN+Style.BRIGHT
brilho_off = Fore.WHITE+Style.NORMAL
  
class bd():
  def __init__(self):
    self.NickName = ""
    self.Nome = ""
    self.email = ""
    self.TwoFA = ""
    self.Password = ""
    self.CodEnviado = ""
    
  def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) 
          for i in range(length))
    
  def adicionar():
    print("Inserção de Utilizadores")
    
    NickName = input(brilho_on +"NickName:"+brilho_off)
    Nome = input(brilho_on +"Nome:"+brilho_off)
    email = input(brilho_on +"Email:"+brilho_off)
    TwoFA = bd.get_random_string(10)
    Password = "DualChat2023"
    CodEnviado = "0"
    
    sql =  "insert into [dbo].[Utilizadores] ([NickName]"
    sql += ",[Nome],[email],[TwoFA],[Password],[CodEnviado])" 
    sql += " VALUES "
    sql += "('" + NickName + "','" 
    sql += Nome + "','" + email + "','"
    sql += TwoFA + "','" + Password + "','0')"
    
    result = bd.connect_db(sql) 
    result.commit()
    
    # Envio de email
    
    mail.envio(Nome, email, TwoFA)

  def atualizar():
     print("Atualização de Utilizadores")
     
     nickname=input("Digite o Nickname:\n")
     sql =  "select * from [dbo].[Utilizadores]"
     sql += " where nickname='" + nickname + "'"
     result = bd.connect_db(sql)   

     print("Valores Atuais\n")
        
     for reg in result:
       print("Nickname:", reg[0])
       print("Nome    :", reg[1])
       print("Email   :", reg[2])
       v1 = reg[0]
       v2 = reg[1]
       v3 = reg[2]
     
     print("\nNovos Valores\n")
     
     n2 = input("Nome  :")
     n3 = input("Email :")
     
     if len(n2)>1:
       if n2!=v2: v2=n2
     
     if len(n3)>1:
       if n3!=v3: v3=n3

     sql =  "update [dbo].[Utilizadores]"
     sql += " set nome='" + v2  + "', email ='" + v3 + "'"
     sql += " where nickname='" + nickname + "'"
     result = bd.connect_db(sql)
     result.commit()     
     
     b=input("Prima Enter para continuar...")     

  def visualizar():
     print("Visualização de Utilizadores")
     
     nickname=input("Digite o Nickname:\n")
     sql =  "select * from [dbo].[Utilizadores]"
     sql += " where nickname='" + nickname + "'"
     result = bd.connect_db(sql)   

     print("Valores Atuais\n")
        
     for reg in result:
       print("Nickname:", reg[0])
       print("Nome    :", reg[1])
       print("Email   :", reg[2])
       
     b=input("Prima Enter para continuar...")

  def remover():
     print("Remoção de Utilizadores")
     
     nickname=input("Digite o Nickname:")
     sql =  "select * from [dbo].[Utilizadores]"
     sql += " where nickname='" + nickname + "'"
     result = bd.connect_db(sql)   

     print("Valores Atuais\n")
     
     for reg in result:
       print("Nickname:", reg[0])
       print("Nome    :", reg[1])
       print("Email   :", reg[2])
     
     escolha=input("\nConfirma a remoção do utilizador (Y/N)\n")
     
     if escolha.upper()=="Y":
       sql =  "delete [dbo].[Utilizadores]"
       sql += " where nickname='" + nickname + "'"
       result = bd.connect_db(sql)
       result.commit()
    
  def connect_db(sqlstring):
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=10.2.10.2\Dual;'
                          'DataBase=DualChat;'
                          'UID=DualChat;'
                          'PWD=Dual2023')
    
    cursor = conn.cursor()
    return cursor.execute(sqlstring)       

  def validauser(n, p):
    query = "select count(*) from Utilizadores "
    query += "where NickName='" + n + "' and password='" + p + "'"
    registos = bd.connect_db(query)    
    for reg in registos:
      nreg=reg[0]
    return str(nreg)   

  def totalalunos():
    registos = bd.connect_db('select count(*) from Utilizadores')    
    for reg in registos:
      nreg=reg[0]    
    return nreg

  def clone():
     print("Clone de Utilizadores")
     
     nickname=input("Digite o Nickname:\n")
     sql =  "select * from [dbo].[Utilizadores]"
     sql += " where nickname='" + nickname + "'"
     result = bd.connect_db(sql)   

     print("Valores Atuais\n")
        
     for reg in result:
       print("Nickname:", reg[0])
       print("Nome    :", reg[1])
       print("Email   :", reg[2])
       Nome = reg[1]
       Email = reg[2]
     
     NovoNickName=input("\nDigite novo NickName:")
     TwoFA = bd.get_random_string(10)
     Password = "DualChat2023"
     CodEnviado = "0"
    
     sql =  "insert into [dbo].[Utilizadores] ([NickName]"
     sql += ",[Nome],[email],[TwoFA],[Password],[CodEnviado])" 
     sql += " VALUES "
     sql += "('" + NovoNickName + "','" 
     sql += Nome + "','" + Email + "','"
     sql += TwoFA + "','" + Password + "','0')"

     result = bd.connect_db(sql)
     result.commit()      
     
  def procurar():
    print("Procura de Utilizadores")
 
    filtro=input("Digite o filtro para a procura:")
    
    sql =  "select * from [dbo].[Utilizadores]"
    sql += " where nome like '%" + filtro + "%' or "
    sql += " email like '%" + filtro + "%'"
    result = bd.connect_db(sql)   

    print("Valores Atuais\n")
        
    for reg in result:
      print(reg[0].ljust(15," "),
            reg[1].ljust(30," "),
            reg[2].ljust(40," "))
    
    b=input("Prima Enter para continuar...")  
    