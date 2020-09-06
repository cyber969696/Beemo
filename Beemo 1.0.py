# Python 3.8.5
# Script criado em 06/08/2020 
#Projeto criado por 2 pessoas
# Se alguem ver e se interessar
# É so entrar em contato com um de nós dois
# Nosso nome ta na opção 0
#Obrigado e até a próxima


# Bibliotecas usadas
import os
from time import sleep
import time

# Listas da opção 3
par = list()
impar = list()

# Inicio que sera repetido de acordo com a escolha do usuário
# Inicio da parte do Lucas
while True:
  print('\033[1;32m==\033[m' * 77)
  print("""\033[1;91m
                                                      ██████╗ ███████╗███████╗███╗   ███╗ ██████╗ 
                                                      ██╔══██╗██╔════╝██╔════╝████╗ ████║██╔═══██╗
                                                      ██████╔╝█████╗  █████╗  ██╔████╔██║██║   ██║
                                                      ██╔══██╗██╔══╝  ██╔══╝  ██║╚██╔╝██║██║   ██║
                                                      ██████╔╝███████╗███████╗██║ ╚═╝ ██║╚██████╔╝
                                                      ╚═════╝ ╚══════╝╚══════╝╚═╝     ╚═╝ ╚═════╝

                                                                    Versão 1.0 \033[m""")
  print('\033[1;32m==\033[m' * 77, '\n')
  print("""
[ 1 ] - Número primo
[ 2 ] - Números negativos/positívos
[ 3 ] - Números pares/ímpares
[ 4 ] - Tabuada de um número
[ 0 ] - Mostrar nome dos desenvolvedores\n""")
  
# Caminhos de acordo com a escolha do usuário   
  escolha = int(input('\033[1m\nInforme sua escolha:\033[m '))

# Validação de escolha
  while escolha <0 or escolha > 5:
    print('\n\033[1;31mERROR! Opção escolhida não está no menu.\033[m\n')
    escolha = int(input('\033[1mInforme sua escolha:\033[m '))

# Repetirá sempre que o usuário quiser
  while True:
    if escolha == 1:
      print('\n')
      ap = '\033[1;32mSEJA BEM-VINDO!\033[m\n '
      print(" ")
      time.sleep(2)
      print(ap.center(77))
      print('\033[1mAqui iremos saber se um número é \033[32;4mprimo\033[m ou \033[31;4mnão.\033[m\n')

      total = 0
      num = int(input('\033[1mDigite um número:\033[m '))
      print('\n')
      sleep(2)
      print('Número \033[1;32mverde\033[m = Seu número foi divisível por ele.')
      sleep(1)
      print('Número \033[1;31mvermelho\033[m = Seu número não foi divisível por ele.\n')
      sleep(3)

# Irá verificar cada número e retornar uma resposta
      for c in range(1, num +1):
          if num %c ==0:
              print('\033[1;32m', end=' ')
              total = total +1
          else:
              print('\033[31m', end=' ')
          print('{}'.format(c), end=' ')
      print('\n')    
      print('\033[m\nO número \033[1;4;32m{}\033[m foi divisível \033[4m{}\033[m vezes\n'.format(num, total))
      if total ==2:
          print('\033[1;32mNúmero primo\033[m\n')
      else:
          print('\033[31mNão é primo\033[m\n')
      voltar =  str(input('\033[1mPara carregar o menu digite\033[m \033[4mM\033[m ou \033[4mO\033[m \033[1mpara digitar novos números.\033[m M/O: ')).upper().strip()    

# Validação de escolha
      while voltar.strip() not in 'M' and voltar.strip() not in 'O':
        voltar =  str(input('\033[1;31mOpção inválida!\033[m \033[1mPara carregar o menu digite\033[m \033[4mM\033[m \033[1mou\033[m \033[4mO\033[m \033[1mpara digitar novos números.\033[m M/O: ')).upper()

# De acordo com a escolha, ele reseta a opção de digitar números novamente
      if voltar in 'O':
        os.system("clear")

# De acordo com a escolha, ele reseta o menu
      if voltar == 'M':
        for x in range(10, 100+5, 10):
          print(" ")
          sleep(1)
          print('\033[1;32m{}% completo\033[m'.format(x))
          time.sleep(0.07)
        if x == 100:
          print('\n\033[42;1mReiniciando menu em 1 segundo...\033[m')
          time.sleep(2)
          os.system("clear")
          break
  
# Daqui pra cima foi Lucas
# Daqui pra baixo foi David
    
    elif escolha == 2:
# Menu da escolha 2   	
    	print("""
\033[32m[ 1 ] -\033[m \033[1;32mNúmeros posítivos\033[m
\033[32m[ 2 ] -\033[m \033[1;32mNúmeros negativos\033[m\n""")
		
# Qual caminho o usuário quer seguir    	
    	escolha2 = int(input("\033[1mInforme sua escolha\033[m: "))

#Validação de escolha
    	while escolha2 >2 or escolha2 <1:
    		   print('\n\033[1;31mERROR! Opção escolhida não está no menu.\033[m\n')
    		   escolha2 = int(input("\n\033[1mInforme sua escolha\033[m: "))
    		   print(" ")
    		   sleep(1)

# Caminho para a escolha 1   		   
    	if escolha2 == 1:
    		   perg2 = int(input("\n\033[1mDigite um número\033[m: "))
    		   print(" ")
    		   sleep(2)
    		   if perg2 >0:
    		   	print("\033[1;32mNúmero posítivo.\n\033[m")
    		   	sleep(2)
    		   	voltar2 = str(input("\033[1mPara carregar o menu digite\033[m \033[4mM\033[m \033[1mou\033[m \033[4mO\033[m \033[1mpara digitar novos números.\033[m M/O: ")).upper().strip()

# Validação de escolha
    		   	while voltar2 not in "M" and voltar2 not in "O":
    		   		voltar2 = str(input('\033[1;31mOpção inválida!\033[m \033[1mPara carregar o menu digite\033[m \033[4mM\033[m \033[1mou\033[m \033[4mO\033[m \033[1mpara digitar novos números.\033[m M/O: ')).upper()

# Reseta a opção de digitar novos números
    		   	if voltar2 in 'O':
    		   		os.system("clear")

# Reseta ao menu
    		   	if voltar2 == 'M':
    		   	   				for P in range(10, 100+5, 10):
    		   	   					print(" ")
    		   	   					sleep(1)
    		   	   					print('\033[1;32m{}% completo\033[m'.format(P))
    		   	   					time.sleep(0.07)
    		   	   				if P == 100:
    		   	   					print('\n\033[42;1mReiniciando menu em 1 segundo...\033[m')
    		   	   					time.sleep(2)
    		   	   					os.system("clear")
    		   	   					break

# Caminho para a escolha 2	    		   			 	
    	elif escolha2 == 2:
    		   	   perg2 = int(input("\n\033[1mDigite um número:\033[m "))
    		   	   print(" ")
    		   	   sleep(2)

# Verificação e resposta
    		   	   if perg2 <0:
    		   	   	print("\033[1;31mNúmero negativo.\n\033[m")
    		   	   	sleep(2)
    		   	   	voltar2 = str(input("\033[1mPara carregar o menu digite\033[m \033[4mM\033[m \033[1mou\033[m \033[4mO\033[m \033[1mpara digitar novos números.\033[m M/O: ")).upper().strip()
                 
#Validação
    		   	   	while voltar2 not in "M" and voltar2 not in "O":
    		   	   		voltar2 = str(input('\033[1;31mOpção inválida!\033[m \033[1mPara carregar o menu digite\033[m \033[4mM\033[m \033[1mou\033[m \033[4mO\033[m \033[1mpara digitar novos números.\033[m M/O: ')).upper()

# Reseta a opção de digitar novos números  
    		   	   	if voltar2 in 'O':
    		   	   		os.system("clear")

# Reseta ao menu
    		   	   	if voltar2 == 'M':
    		   	   					for P in range(10, 100+5, 10):
    		   	   					  print(" ")
    		   	   					  sleep(1)
    		   	   					  print('\033[1;32m{}% completo\033[m'.format(P))
    		   	   					  time.sleep(0.07)
    		   	   					if P == 100:
    		   	   							print('\n\033[42;1mReiniciando menu em 1 segundo...\033[m')
    		   	   							time.sleep(2)
    		   	   							os.system("clear")
    		   	   							break

#Fim da parte do David
#Inico da parte do Lucas

# Caminho se a escolha do menu for 3
    elif escolha == 3:
# Explicação 
          print(" ")
          print("""\033[1;32mEstá ferramenta funciona assim:\033[m
\033[1mvocê pode digitar o total de números que quiser, \033[1;4mporém tome cuidado!\033[m 
\033[1mSe seu sistema não tiver um processador bom, pode travar devido a quantidade enorme de números!\033[m\n""")

# Checagem
          checagem = str(input('\033[1mSe você leu e aceita prosseguir, digite \033[4mP\033[m\033[1m, se quer sair digite\033[m \033[4mS\033[m. P/S: ')).upper()[0]

# Validação de escolha
          while checagem.strip() not in 'P' and checagem.strip() not in 'S':
              print('\033[1;91mPor favor, informe uma opção válida!\033[m')
              checagem = str(input('\033[1mSe você leu e aceita prosseguir, digite\033[m \033[4mP\033[m\033[1, se quer sair digite\033[1m \033[4mS\033[m. P/S: ')).upper()[0]

# Começo da digitação de números
          if checagem == 'P':
             os.system("clear")
             num = int(input('\033[1mInforme um número para verificar os pares e ímpares entre ele:\033[m '))

# Verificação de par ou ímpar
             for y in range(0, num + 1):
               if y %2 == 0:

# Se tem par, ele adiciona na lista de pares
                 print('\033[1mO número\033[m \033[4m{}\033[m \033[1mé\033[m \033[32mPar\033[m.\n'.format(y))
                 par.append(y)

               elif y %2 == 1:
# Se tem ímpar ele adiciona na lista de ímpares
                print('\033[1mO número\033[m \033[4m{}\033[m \033[1mé\033[m \033[31mÍmar\033[m.\n'.format(y))
                impar.append(y)

             if y == num:
# Opção de escolha
              cont = str(input('\033[1mDeseja continuar? S/N ou \033[4mV\033[m \033[1mpara ver todos os números pares e ímpares digitados:\033[m ')).upper()[0]

# Validação de escolha
              while cont.strip() not in 'S' and cont.strip() not in 'N' and cont.strip() not in 'V':
                cont = str(input('\033[1;31mOpção inválida!\033[m Deseja continuar? S/N ou V para ver todos os números pares e ímpares digitados: ')).upper()[0]

# Reseta a opção de digitar novos números
             if cont == 'S':
               print('\n\033[1;32mVoltando...\033[m')
               time.sleep(1)
               os.system("clear")

# Mostra todos os números digitados em suas listas separadas
             elif cont == 'V':

# Mostra a lista de pares
                print('\033[32m==\033[m' * 38)
                print('\033[1mLista de pares\033[m = \033[4;32m{}\033[m'.format(par))
                par.sort(reverse=True)
                print('\033[1mLista de par do maior para o menor\033[m = \033[4;32m{}\033[m\n'.format(par))
                print('\033[32m==\033[m' * 38, '\n')
# Mostra a lista de ímpares
                print('\033[32m==\033[m' * 38)
                print('\033[1mLista de ímpares\033[m = \033[4;32m{}\033[m'.format(impar))
                impar.sort(reverse=True)
                print('\033[1mLista de ímpares do maior para o menor\033[m = \033[4;32m{}\033[m\n'.format(impar))
                print('\033[32m==\033[m' * 38, '\n')
# Opção de eescolha                
                sair = str(input('\033[1mPara sair para o menu aperte\033[m \033[4mQ\033[m: ')).upper()[0]

# Validação de escolha
                while sair.strip() not in 'Q':
                  sair = str(input('\033[1;91mOpção inválida!\033[m Para sair para o menu aperte Q: ')).upper()[0]

# Caminho que reseta ao menu da opçao 3
                if sair == 'Q':
                  time.sleep(1)
                  os.system("clear")

# Reseta direto ao menu se a escolha for N
             else:
               print('\n\033[1;32mVoltando para o menu...\033[m')
               time.sleep(1)
               os.system("clear")
               break

# Reseta o menu se a escolha for S
          elif checagem == 'S':

# Porcentagem completa de carregamento             
             for x in range(10, 100 + 1, 10):
                print(" ")
                print('\033[1;32m{}% Completo\033[m'.format(x))
                print(" ")
                time.sleep(1)

# Carregado ele reseta ao menu                
             if x == 100:
               print('\n\033[4;32mCarregando menu...\033[m')
               time.sleep(1)
               os.system("clear")
               break

# Início da parte do David

# Caminho se a escolha do menu for 4
    elif escolha == 4:    
# Apresentação
    		print("\n\033[1;32mIniciando...\033[m")
    		sleep(2)
    		
    		num = int(input("\n\033[1mDigite um número para saber a tabuada:\033[m "))
    		
    		ox = 0
    		print(" ")
    		print("\033[1mTabuada de \033[4;32m{}\033[m".format(num))
    		print(" ")

# Repetirá até chegar a 10
    		while ox <= 10:
    			print("\033[32m=\033[m"* 10)
    			print("\033[1;31m{}\033[m X \033[1;32m{}\033[m = \033[1m{}\033[m".format(ox, num, (ox * num)))
    			ox = ox + 1
    			print("\033[32m=\033[m"* 10)
    			
    		sleep(1)	
    		print(" ")	

# Opção de escolha
    		voltar4 =  str(input('\033[1mPara carregar o menu digite\033[m \033[4mM\033[m \033[1mou\033[m \033[4mO\033[m \033[1mpara ir novamente.\033[m M/O: ')).strip().upper()

# Validação de dados
    		while voltar4 not in "M" and voltar4 not in "O":
    			print(" ")
    			voltar4 = str(input('\033[1;31mOpção inválida!\033[m \033[1mPara carregar o menu digite\033[m \033[4mM\033[m \033[1mou\033[m \033[4mO\033[m \033[1mpara digitar novos números.\033[m M/O: ')).strip().upper()
    		
# Reseta a opção de digitar novos números
    		if voltar4 in "O":
    			os.system("clear")

# Reseta para o menu
    		if voltar4 == "M":
# Careegamento do menu
    			for A in range(10, 100+5, 10):
    				print(" ")
    				sleep(1)
    				print('\033[1;32m{}% completo\033[m'.format(A))
    				time.sleep(0.7)

# Carregado ao menu, ele ja inicia
    			if A == 100:
    				print('\n\033[42;1mReiniciando menu em 1 segundo...\033[m')
    				sleep(2)
    				os.system("clear")
    				break

# Caminho que mostra os nomes dos desenvolvedores
# Início da parte do Lucas
    elif escolha == 0:
      time.sleep(2)
      print('\n\033[1;4;32mNome dos desenvolvedores abaixo:\033[m\n')
      print("""
      \033[1;4;32mDavid Lins\033[m\n 
      \033[1;4;32mLucas\033[m 
      """)

# Opção de escolha
      menu = str(input('\033[1mPara voltar ao menu digite \033[1;4mX\033[m. \033[1mPara saber se vai ter\033[m \033[1;4mBeemo 2.0\033[m \033[1mdigite\033[m \033[1;4mB\033[m: ')).upper()
    
# Validação de escolha
      while menu.strip() not in 'X' and menu.strip() not in 'B':
        print('\t\t\t\t\t\033[1;31mERROR\033[m')
        menu = str(input('Para voltar ao menu digite \0333[1;4mX\033[m. Para saber se vai ter Beemo 2.0 digite \033[1;4mB\033[m: ')).upper()
        print(" ")

# Caminho se a escolha for X
      if menu == 'X':
        print(" ")
        for w in range(10, 100 +1, 10):
          print('\033[1;92m{}% completo\033[m\n'.format(w))
          time.sleep(1)   
        if w == 100:
          print('\033[1mRecarregando o menu em 1 segundo...\033[m')
          time.sleep(2)
          os.system("clear")
          break

# Caminho se a escolha for B
      elif menu == 'B':
        os.system("clear")
        print('\n\033[1mSim, vai ter o\033[m \033[4;1mBeemo 2.0\033[m \033[1mcom muito mais opções!\033[1m\n')
        print('\033[1mSe chegou nessa resposta é porque gostou do programa, agradecemos de coração!\033[m\n')

# Escolha
        menu_1 = str(input('\033[1mPara voltar ao menu digite\033[m \033[4;1mZ\033[m: ')).upper()

# Validação da escolha
        while menu_1.strip() not in 'Z':
          menu_1 = str(input('\033[1;91mDigite uma opção válida!\033[m \033[1mPara voltar ao menu digite\033[m \033[4;1mZ\033[m: ')).upper()
          print(" ")

# Caminho da escolha Z
        if menu_1 == 'Z':
          print(" ")
          for w in range(10, 100 +1, 10):
           print('\033[1;92m{}% Completo\033[m\n'.format(w))
           time.sleep(1)

# Resetando para o menu   
          if w == 100:
            print('\033[1mRecarregando o menu em 1 segundo...\033[m')
            time.sleep(2)
            os.system("clear")
            break

# Fim da parte do Lucas

# Finalização do projeto
#Está para chegar a versão 2.0 com muito mais rescursos além destes
# Programadores responsáveis:  >>> DAVID LINS  E  LUCAS SILVA <<<
