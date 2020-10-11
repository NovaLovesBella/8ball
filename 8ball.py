import random
speak = input('what do you want the 8ball to answer:\n')
if '?' not in speak :
  print('Needs to be a question')
  exit()
n = random.randint(1,13)
eightball = n
if (eightball == 1) :
  print('It it certain') 
elif (eightball == 2) :
  print('Not possible')
elif (eightball == 3) :
  print('Without a doubt')
elif (eightball == 4) :
  print('You may rely on it')
elif (eightball == 5) :
  print('Yes definitely')
elif (eightball == 6) :
  print('It is decidedly so')
elif (eightball == 7) :
  print('As I see it, yes')
elif (eightball == 8) :
  print('My reply is no')
elif (eightball == 9) :
  print('Yes')
elif (eightball == 10) :
  print('Outlook good')
elif (eightball == 11) :
  print('Signs point to yes')
elif (eightball == 12) :
  print('Reply hazy try again')
elif (eightball == 13) :
  print('Better not tell you now')

