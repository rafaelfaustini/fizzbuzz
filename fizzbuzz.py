import time

inicio=False
current=1
score=0


print('Fizz - Números divisíveis por 3')
time.sleep(2)
print('Buzz - Números divisíveis por 5')
time.sleep(2)
print('FizzBuzz - Números Divisíveis por 3 e 5')
time.sleep(2)
print('Caso não seja nenhum dos três, deixe em branco')
time.sleep(2)
inicio=True



while inicio==True:
    print('O número é '+str(current))
    lol = raw_input('Fizz,Buzz,FizzBuzz, ou nenhum(deixe em branco) ? ')
    if score>=0:
       if (current%3==0) and (current%5!=0): #Fizz
            r=1
       if (current%3!=0) and (current%5==0): #Buzz 
            r=2
       if (current%3==0) and (current%5==0): #FizzBuzz 
            r=3
       if current%3!=0 and current%5!=0: #Nada
            r=0

       if lol=='Fizz' and r==1:
           score+= 5
       else:
           if lol!='Fizz' and r==1:
               score=score-10

       if lol=='Buzz' and r==2:
            score+= 5
       else:
           if lol!='Buzz' and r==2:
               score=score-10

       if lol=='FizzBuzz' and r==3:
            score+= 5
       else:
           if lol!='FizzBuzz' and r==3:
               score=score-10
       if lol=='' and r==0:
            score+=5
       else:
           if lol!='' and r==0:
               score=score-10
    else:
        print('Game Over')
        inicio=False
    print(lol)    
    print(r)    
    print('Seu score é '+str(score))
    time.sleep(1)
    current= current+1
    
    
