try:
    import random 
    r=random.randint(1,100) #Generating a random number 
    a=int(input("You wanna play a game..? (\"Number Guessing Game\")\n_______________\nEnter 1 for Start and Enter 2 for Exit\nEnter you choice:"))
    print("____________________________________________________________________________")
    if a==1:
        c=1
        while True:
            u=int(input("Enter a Number:")) #Taking input from user
            
            if u==r:
                print(f"You guessed it right in {c} attempts")
                break
            if u<r:
                print("Goo Higher")
            elif u>r:
                print("Go Lower")
            c+=1
        print("___________________________________")
        print("Thanks For Playing..")
    elif a==2:
        print("You Exit.")

    else:
        print("Wrong entry.")
except:
    print("Error: something went Wrong !")