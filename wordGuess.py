import random
rand=random.randint(1,10)
number=5
while number > 0:
    a=int(input('Enter you guess'))
    if(a<rand):
        print('Your guess is smaller , guess a number greater than ',a)
    elif(a>rand):
        print('Your guess is greater , guess a number smaller than ',a)
    else:
        print('congratulation You are right! the no is',a)
        break
    number-=1
