import os
from basedados import bd

def menu(total):
  os.system("cls") 
  print("Total de Utilizadores :", total,"\n")
  print("1 - Adicão de Utilizadores")  
  print("2 - Alteração de Utilizadores")
  print("3 - Procura de Utilizadores")
  print("4 - Visualização de Utilizadores")
  print("5 - Remoção de Utilizadores") 
  print("0 - Sair")
  opcao=input(":")
  return opcao

def main():
  escolha=""
  while escolha!="0":
    escolha=menu(bd.totalalunos())
    match escolha:
      case "1":
        bd.adicionar()
      case "2":
        bd.atualizar()
      case "4":      
        bd.visualizar()
      case "5":
        bd.remover()
      case "6": 
        bd.clone()
  

main()