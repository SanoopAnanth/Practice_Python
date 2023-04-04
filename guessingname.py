import random
words=["Shashank","Mallikarjun","Sanoop","Madhukar","Aditya"]
word=random.choice(words)
turn=12
print("guess the character")
guesses=" "
while turn>0:
    failed=0
    for char in word:
        if char in guesses:
            print(char,end="")
        else:
            print("_")
            failed+=1
    if failed==0:
        print("You have won\n")
        print("the word is",word)
        break
    print()
    guess=input("enter a character")
    guesses=guesses+guess
    if guess not in word:
        turn=turn-1
        print("wrong")
        print("you have only ",turn," left")
        if(turn==0):
            print("you lost")

