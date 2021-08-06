#This is my first idea of simple quiz type math(sum,sub,mul,div) game in terminal and this is my first project.
#output will looks better in black theme of your IDE.
#a and b are two variable used for addition
#c and d are two variable used for substraction
#x and y are two variable used for multiplication
#w and z are two variable used for division
import random
import time
def add(a,b):
    return a+b
def sub(c,d):
    return c-d
def mul(x,y):
    return x*y
def div(w,z):
    return w//z
def beginner():
    print("\033[95m"+"\t\t\t\t\t\t\tYOU ARE IN FIRST LEVEL!"+"\033[0m")
    print("\033[96m"+"\t\t\t\t\t\t  EARN 100 POINTS TO PLAY INTERMEDIATE LEVEL."+"\033[0m")
    points=0
    x=1
    list = ['+', '-', '*', '/']
    while x:
        print("\033[91m" + "\t\t\t\t\t\t\t\tPOINTS=", points, "\033[0m")
        if(points == 100):
            return points+intermediate()
        #how they will select from these three options
        index=random.randrange(0,4)
        if list[index]=='+':
            a=random.randrange(5,21)
            b=random.randrange(0,11)
            print(a,'+',b,'=',end='?')
            start = time.time()
            result = int(input())
            stop = time.time()
            if (stop-start)>5:
                print("You take more than 5 seconds to answer i.e, {}"%(stop-start))
                print("Times Up!")
                return points
            if result==add(a,b):
                points=points+10
            else:
                print('\033[92m' + 'WRONG ANSWER! BETTER LUCK NEXT TIME' + '\033[0m')
                return points
        elif list[index]=='-':
            c=random.randrange(5,21)
            d=random.randrange(0,11)
            print(c,'-',d,'=',end='?')
            start = time.time()
            result = int(input())
            stop = time.time()
            if (stop-start)>5:
                print(stop-start)
                print("Times Up!")
                return points
            if result==sub(c,d):
                points=points+10
            else:
                print('\033[92m' + 'WRONG ANSWER! BETTER LUCK NEXT TIME' + '\033[0m')
                return points
        elif list[index]=='*':
            x=random.randrange(5,21)
            y=random.randrange(0,11)
            print(x,'*',y,'=',end='?')
            #result=int(input())instead of this line learn how to add options(for ex sum=20,then option should in range 17 to 23)
            start = time.time()
            result = int(input())
            stop = time.time()
            if (stop-start)>5:
                print("You take more than 5 seconds to answer i.e, {}"%(stop-start))
                print("Times Up!")
                return points
            if result==mul(x,y):
                points=points+10
            else:
                print('\033[92m' + 'WRONG ANSWER! BETTER LUCK NEXT TIME' + '\033[0m')
                return points
        else:
            w=random.randrange(5,21)
            z=random.randrange(1,11)
            print(w,'/',z,'=',end='?')
            start = time.time()
            result = int(input())
            stop = time.time()
            if (stop-start)>5:
                print(stop-start)
                print("Times Up!")
                return points
            if result==div(w,z):
                points=points+10
            else:
                print('\033[92m' + 'WRONG ANSWER! BETTER LUCK NEXT TIME' + '\033[0m')
                return points
        x=1
def intermediate():
    print("\033[95m" + "\t\t\t\t\t\t\t   YOU ARE IN SECOND LEVEL!" + "\033[0m")
    print("\033[96m" + "\t\t\t\t\t\t  EARN 100 POINTS TO PLAY EXPERT LEVEL." + "\033[0m")
    points = 0
    x=1
    list = ['+', '-', '*', '/']
    while x:
        print("\033[91m"+"\t\t\t\t\t\t\t\tPOINTS=", points,"\033[0m")
        if (points == 300):
            return points+expert()
        #how they will select from these three options
        index=random.randrange(0,4)
        if list[index]=='+':
            a=random.randrange(21,36)
            b=random.randrange(0,11)
            print(a,'+',b,'=',end='?')
            start = time.time()
            result = int(input())
            stop = time.time()
            if (stop-start)>5:
                print(stop-start)
                print("Times Up!")
                return points
            if result==add(a,b):
                points=points+10
            else:
                print('\033[92m' + 'WRONG ANSWER! BETTER LUCK NEXT TIME' + '\033[0m')
                return points
        elif list[index]=='-':
            c=random.randrange(21,36)
            d=random.randrange(0,11)
            print(c,'-',d,'=',end='?')
            start = time.time()
            result = int(input())
            stop = time.time()
            if (stop-start)>5:
                print(stop-start)
                print("Times Up!")
                return points
            if result==sub(c,d):
                points=points+10
            else:
                print('\033[92m' + 'WRONG ANSWER! BETTER LUCK NEXT TIME' + '\033[0m')
                return points
        elif list[index]=='*':
            x=random.randrange(0,51)
            y=random.randrange(0,11)
            print(x,'*',y,'=',end='?')
            #result=int(input())#instead of this line learn how to add options(for ex sum=20,then option should in range 17 to 23)
            start = time.time()
            result = int(input())
            stop = time.time()
            if (stop-start)>5:
                print(stop-start)
                print("Times Up!")
                return points
            if result==mul(x,y):
                points=points+10
            else:
                print('\033[92m' + 'WRONG ANSWER! BETTER LUCK NEXT TIME' + '\033[0m')
                return points
        else:
            w=random.randrange(0,10)
            z=random.randrange(10,21)
            print(w,'/',z,'=',end='?')
            start = time.time()
            result = int(input())
            stop = time.time()
            if (stop-start)>5:
                print(stop-start)
                print("Times Up!")
                return points
            if result==div(w,z):
                points=points+10
            else:
                print('\033[92m' + 'WRONG ANSWER! BETTER LUCK NEXT TIME' + '\033[0m')
                return points
        x=1
def expert():
    print("\033[95m" +"\t\t\t\t\t\t\t HEY! CONGRATS, YOU ARE IN FINAL LEVEL." + "\033[0m")
    points = 0
    x=1
    list = ['+', '-', '*', '/']
    while x:
        print("\033[91m" + "\t\t\t\t\t\t\t\tPOINTS=", points, "\033[0m")
        #how they will select from these three options
        index=random.randrange(0,4)
        if list[index]=='+':
            a=random.randrange(0,10)
            b=random.randrange(10,21)
            print(a,'+',b,'=',end='?')
            start = time.time()
            result = int(input())
            stop = time.time()
            if (stop-start)>5:
                print(stop-start)
                print("Times Up!")
                return points
            if result==add(a,b):
                points=points+10
            else:
                print('\033[92m' + 'WRONG ANSWER! BETTER LUCK NEXT TIME' + '\033[0m')
                return points
        elif list[index]=='-':
            c=random.randrange(0,10)
            d=random.randrange(10,21)
            print(c,'-',d,'=',end='?')
            start = time.time()
            result = int(input())
            stop = time.time()
            if (stop-start)>5:
                print(stop-start)
                print("Times Up!")
                return points
            if result==sub(c,d):
                points=points+10
            else:
                print('\033[92m' + 'WRONG ANSWER! BETTER LUCK NEXT TIME' + '\033[0m')
                return points
        elif list[index]=='*':
            x=random.randrange(0,10)
            y=random.randrange(10,21)
            print(x,'*',y,'=',end='?')
            #result=int(input())#instead of this line learn how to add options(for ex sum=20,then option should in range 17 to 23)
            start = time.time()
            result = int(input())
            stop = time.time()
            if (stop-start)>5:
                print(stop-start)
                print("Times Up!")
                return points
            if result==mul(x,y):
                points=points+10
            else:
                print('\033[92m' + 'WRONG ANSWER! BETTER LUCK NEXT TIME' + '\033[0m')
                return points
        else:
            w=random.randrange(0,10)
            z=random.randrange(10,21)
            print(w,'/',z,'=',end='?')
            start = time.time()
            print(start)
            result = int(input())
            stop = time.time()
            print(stop)
            if (stop-start)>5:
                print(stop-start)
                print("Times Up!")
                return points
            if result==div(w,z):
                points=points+10
            else:
                print('\033[92m'+'WRONG ANSWER! BETTER LUCK NEXT TIME'+'\033[0m')
                return points
        x=1
print("\033[91m"+"\t\t\t\t\t\t\t\tWELCOME MATH LOVERS"+"\033[0m")
print('\033[93m'+'\033[4m'+'1. Beginner')
print('2. Intermediate')
print('3. Expert'+'\033[0m')
x=1
while x:
    choice=int(input('\033[92m'+"Enter Your CHOICE: "+"\033[0m"))
    if choice == 1:
        print("\033[92m"+"\t\t\t\t\t\t\t1LET'S START THE GAME!"+"\033[0m")
        print("\033[96m"+'YOU EARNED',beginner(),'POINTS.'+'\033[0m')
    elif choice == 2:
        print("\033[92m"+"\t\t\t\t\t\t\t\tLETS START THE GAME!"+'\033[0m')
        print("\033[96m"'YOU EARNED',intermediate(),'POINTS.'+'\033[0m')
    elif choice==3:
        print("\033[92m" + "\t\t\t\t\t\t\t\tLETS START THE GAME!" + '\033[0m')
        print("\033[96m"+'YOU EARNED',expert(),'POINTS.'+'\033[0m')
    else:
        print('Please, Enter a valid choice')
        continue
    x = int(input("\033[93m"+'You Can Press 0 To Exit And 1 To Continue The Game: '+"\033[0m"))
