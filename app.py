from pickle import TRUE
import random
def gameWin(comp,you):
    if comp==you:
        return None

    elif comp=='r':
        if you== 's':
            return False
    elif you =='p':
        return TRUE 
    elif comp=='s':
        if you== 'p':
           return True
    elif you =='r':
        return False 



print("comp turn: rock(r) paper(P) scissor(s)")
randno=random.randint(1,2)
print(randno)
if randno ==1:
    comp='r'
elif randno ==2:
    comp='p'
elif randno== 3:
    comp='s'

you=input("your turn: rock(r) paper(p) scissor(s)")
a = gameWin(comp,you)


print(f"computer chose{comp}")
print(f"you chose{you}")

if a==None:
    print("the game is tie")
elif a:
    print("you win")
else:
    print("you lose")