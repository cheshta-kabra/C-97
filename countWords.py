import random
rand=random.randint(1,10)
name='Cheshta is 15 years old.'
wordCount=1
characterCount=0

for i in name:
    if(i==' '):
        wordCount+=1
    else:
        characterCount+=1
print(characterCount)
print (wordCount)
print(rand)