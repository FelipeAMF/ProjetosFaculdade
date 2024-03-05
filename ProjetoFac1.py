import getpass
import os

User = {'1'}
Pass = {'123'}
Login = {'S','s'}
Cad = {'N','n'}
LogorCad = input('Deseja fazer login Digite [S] ou [N] para se cadastrar: ')
if(LogorCad in Login):
 UserF = input('Insira seu Nome de usuario:')
 PassF = getpass.getpass('Insira sua Senha:')
 os.system('cls')
 os.system('clear')
if(LogorCad in Cad):
   User = input('Defina seu Usuario: ')
   Pass = input('Defina sua Senha: ')
   os.system('cls')
   os.system('clear')
   print('Usuario criado com sucesso!!!\n')
   
   UserF = input('Insira seu Nome de Usuario: ')
   PassF = getpass.getpass('Insira sua Senha: ')
   os.system('cls')
   os.system('clear')
#codigo do programa iniciado caso Usuario e senha corretos.
if (UserF in User and PassF  in Pass):
  print("Login Aprovado Sr(a):{}".format(UserF))
  comida = float(input('Insira seus gastos com comida: '))
  energia = float(input('Insira seus gastos com energia: '))
  agua = float(input('Insira seus gastos com agua: '))
  outros = float(input('Insira outros gastos: '))
  #soma dos gastos
  total = comida + energia + agua + outros
  os.system('cls')
  os.system('clear')
  limite = 1320.0
  #if para verificar se o total for maior que limite
  if(total>limite):
   print('Sr(a):{}\n'' \nO total este mes foi de: R$:{:.2f}\n'' \nSeus gastos passaram do limite porfavor mantenha os gastos no verde proximo mes!!!'.format(UserF,total))
   #elif se total por menor ou igual a limite
  elif(total<=limite):
   print('Sr(a):{}\n'' \nO total este mes foi de: R$:{:.2f}\n'' \nSeus gastos ficaram no verde continue assim!!'.format(UserF,total) )
   # IFs para verificar qual o maior gasto Abaixo
  if(comida>energia and comida>agua and comida>outros):
    print('\n \nSeu maior gasto foi com comida: R${:.2f}'.format(comida))
  if(energia>comida and energia>agua and energia>outros):
    print('\n \nSeu maior gasto foi com energia: R${:.2f}'.format(energia))
  if(agua>comida and  agua>energia and agua>outros):
    print('\n \nSeu maior gasto foi com agua: R${:.2f}'.format(agua))
  if(outros>comida and outros>energia and outros>agua):
    print('\n \nSeu maior gasto foi com outros: R${:.2f}'.format(outros))
    
#Programa finalizado por Usuario e senha incorretos.
else:
  print('Usuario ou senha incorretos.')