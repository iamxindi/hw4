

from random import randrange

name = input("What's your questions?")

magiceight=['It is certain', 'It is decidedly so', 'Without a doubt','Yes definitely','You may rely on it', 'As I see it, yes','Most likely',' Outlook good','Yes','Signs point to yes','Reply hazy try again','Ask again later','Better not tell you now','Cannot predict now',' Concentrate and ask again',"Don't count on it",'My reply is no',' My sources say no','Outlook not so good','Very doubtful']
answer=magiceight[randrange(len(magiceight))]
print(answer)


if name[-1] != "?":
    print("I’m sorry, I can only answer questions")
    name = input("What's your question?")
    
