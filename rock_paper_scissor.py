import random
#function

#rock=1 paper=2 scissors=3

def results(comp, you):
    if comp == you:
        return None
    elif comp == 1:
        if you == 2:
            return True
        elif you == 3:
            return False
    elif comp == 2:
        if you == 3:
            return True
        elif you == 1:
            return False
    elif comp == 3:
        if you == 1:
            return True
        elif you == 2:
            return False    

#main part

print("Computers turn: Rock(1) , Paper(2), Scissors(3)?")
comp = random.randint(1,3)
you = int(input("Your turn: Rock(1) , Paper(2), Scissors(3)?"))
print(comp)
a = results(comp, you)
if a == None:
    print("Its a tie")
elif a == True:
    print("Congrats!! You Won!!")
else:
    prints("Sorry! You Lost!!")