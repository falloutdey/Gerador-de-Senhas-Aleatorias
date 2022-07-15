#Bibliotecas
import random as r

# Caracteres
number = '0123456789'
min = 'abcdefghijklmnopqrstuvwxyz'
max = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
simb = '._#-@&!'

# Programa Principal
def programa():
  caract = number + min + max + simb
  control = 0
  try:
    while control != 1:
        if control == 0:
          q = int(input('\nQuantas senhas deverão ser criadas?\n> '))
          tam = int(input('\nQual deverá ser o tamanho da(s) senha(s)?\n> '))
          if q == 0 or tam == 0:
              print('\nInformação Nula! Tente novamente.')
          else:
            for i in range(q):
                senha = ''.join(r.sample(caract, tam))
                print(senha)
            control = int(input('\nVocê deseja criar mais senhas?\n0 - Sim\n1 - Não\n> '))
        if control != 1 and control != 0:
          print('Opção Inválida!')
          control = int(input('Você deseja criar mais senhas?\n0 - Sim\n1 - Não\n> '))
    else:
      print('\nPrograma finalizado!')
  except ValueError:
    exc_control = int(input('\nValor Inválido!\nDeseja Reiniciar?\n0 - Sim\n1 - Não\n> '))
    if exc_control == 0:
      programa()
    else:
      print('\nPrograma Finalizado!')

programa()
