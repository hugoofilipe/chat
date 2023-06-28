import time
import socket


token=""
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ('10.2.10.250',10000)

sock.connect(server_address)

utilizador=input("Digite o seu nickname:") #Ildze
utilizador=utilizador.replace(";","")

password=input("Digite a password:") #Ildze
password=password.replace("'","")
password=password.replace("--","")

mens = utilizador +"|"+password
sock.sendall(("Valida;"+mens+';EOF').encode())
data=sock.recv(1024)

#print("["+data.decode()+"]")

tk=data.decode().split(";")

print(tk[0])

if tk[0]=="0":
  print("Nickname ou Password Invalida!")
  sock.close()
  quit()
  
if tk[0]=="-1":
  print("Já está logado no ip " + tk[1] +"!")
  sock.close()
  quit()  

token=tk[1]
if len(utilizador)>1:
    doit=True
    while doit:
       mens=input("Mensagem:")
       mens=mens.replace(";","")  #Sveiki
       if len(mens)>0:
          #"Ildze;Sveiki;EOF"
          sock.sendall((utilizador+";"+mens+';'+token+';EOF').encode())
       else:
         doit=False

    sock.close()
    print("Terminado")
else:
    print("Utilizador invalido")
    