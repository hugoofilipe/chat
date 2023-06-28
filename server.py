import socket
import threading
from datetime import datetime
from basedados import bd

def validamensagem(_v):   
   for tk in tokens:
      if _v==tk:
        return True      

   return False

def comrecebida(conn):
   try:
      #print(conn)

      lermen=True
      while lermen:
          dados=b''
          while True:
             buff=conn.recv(64)         
             if len(buff)>0:
                 dados +=buff
                 if b';EOF' in dados:         
                   break
             else:
               lermen=False
               break
               
          dados2=dados.decode()
          dados2=dados2.replace(";EOF","")          
          dados3=dados2.split(";")

          if dados3[0]=="Valida":
             info= dados3[1].split("|")
             #print(info)
             res=""
             for tk in tokens:
               _tk=tk.split(";")
               if _tk[0]==info[0]:
                 res="-1;"+_tk[2]
                 break
                 
             if res=="":
                 res=bd.validauser(info[0], info[1])
                 
                 token = bd.get_random_string(40)
                 ip = conn.getpeername()[0]
                 
                 #print(res,token,ip)
                 if res=="1":
                   res = res + ";"+token
                   tokens.append(info[0]+";"+token+";"+ip)
                 else:
                   res="0;0"
                 
             conn.sendall(res.encode())
          else:
            try:
              v=dados3[0]+";"+dados3[2]+";"+str(conn.getpeername()[0])
              #print(v)
              if validamensagem(v):
                 #print(conn.getsockname(), dados2) Servidor
                 print(dados3[0],conn.getpeername(), dados3[1])

                 hoje = datetime.now()
                      
                 datareg = str(hoje.year) + "-" + str(hoje.month)+ "-" + str(hoje.day)
                 datareg += "\t"
                 datareg += str(hoje.hour) + ":" + str(hoje.minute)
                 datareg += "\t"

                 ficheiro = open("chat.log","a")
                 #ficheiro.write(dados3[0]+chr(9)+str(conn.getpeername())+chr(9)+dados3[1]+"\n")
                 ficheiro.write(datareg + dados3[0]+"\t"+str(conn.getpeername())+"\t"+dados3[1]+"\n")
                 ficheiro.close()            
            except:
              dummy1=0


   except AssertionError as error:
     #print(error)
     print(":(  -- Com terminada remotamente.")
   finally:
     print(":(")
   
   conn.close()      
   quit()

#inicio

tokens = []

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=('10.2.10.250',10000)
print('A reservar porta 10000')
sock.bind(server_address)
sock.listen(30)

while True:
   print("A espera de conexao:")
   connection, client = sock.accept()
   th = threading.Thread(target=comrecebida, args=(connection,))
   th.start()
