import random
import math
x=int(input("Enter the lower bound\n"))
y=int(input("enter the upper bound\n"))
guess=random.randint(x,y)
print("you have only",3," chance to guess\n")
count=1
while count<=3:
    new_guess=int(input("enter the guess number\n"))
    if(new_guess==guess):
        print("you have guessed correctly\n")
        break
    elif(new_guess>guess):
        print("the number to guess is lower than what you entered\n")
        count=count+1
    else:
        print("the number to guess is higher than what you entered\n")
        count=count+1
if count>3:
    print("the number to guess is\n",guess)
    print("\n better luck next time\n")
