import time
import sys
#Valores padr�es para l�gica
current=0
score=0
inicio=False #N�o come�a o jogo enquanto mostra o pequeno tutorial

def fizzbuzz(): #Define ao Programa o que � Fizz,Buzz,FizzBuzz e nada
       if score>=0:
           global r
           if (current%3==0) and (current%5!=0): #Fizz
            r=1
           if (current%3!=0) and (current%5==0): #Buzz 
            r=2
           if (current%3==0) and (current%5==0): #FizzBuzz 
            r=3
           if current%3!=0 and current%5!=0: #Nada
            r=0
def gameover(): #GameOver
    if score < 0:
        print('Game Over')
        print(score)
        inicio=False
        sys.exit()
        
def check(): #Checa se a resposta do usu�rio est� correta e adiciona o score
       global score
       if lol=='Fizz' and r==1: 
           score+= 5
       elif lol!='Fizz' and r==1:
            score-=10

       if lol=='Buzz' and r==2:
            score+= 5
       elif lol!='Buzz' and r==2:
            score-=10

       if lol=='FizzBuzz' and r==3:
            score+= 5
       elif lol!='FizzBuzz' and r==3:
            score-=10
       if lol=='' and r==0:
            score+=5
       elif lol!='' and r==0:
            score-=10

#Tutorial
print('Fizz - N�meros divis�veis por 3')
time.sleep(2)
print('Buzz - N�meros divis�veis por 5')
time.sleep(2)
print('FizzBuzz - N�meros Divis�veis por 3 e 5')
time.sleep(2)
print(' ')
print('Caso n�o seja nenhum dos tr�s, deixe em branco')
time.sleep(2)
print(' ')
inicio=True #Come�a o jogo p�s tutorial


while inicio==True: #Looping do jogo
    current+= 1
    print('O n�mero � '+str(current))
    lol = raw_input('Fizz,Buzz,FizzBuzz, ou nenhum(deixe em branco) ? ')
    fizzbuzz()
    check()
    gameover()
    print('Seu score � '+str(score))
    time.sleep(1)
    
    
