import random
import time
#making a function
def one_():
    print("___________")
    time.sleep(0.5)
    print("[         ]")
    time.sleep(0.5)
    print("[    0    ]")
    time.sleep(0.5)
    print("[         ]")
    time.sleep(0.5)
    print("__________")

def two_():
    print("___________")
    time.sleep(0.5)
    print("[         ]")
    time.sleep(0.5)
    print("[  0    0 ]")
    time.sleep(0.5)
    print("[         ]")
    time.sleep(0.5)
    print("___________")

def three_():
    print("___________")
    time.sleep(0.5)
    print("[         ]")
    time.sleep(0.5)
    print("[ 0  0  0 ]")
    time.sleep(0.5)
    print("[         ]")
    time.sleep(0.5)
    print("___________")

def four_():
    print("___________")
    print("[         ]")
    time.sleep(0.5)
    print("[  0    0 ]")
    time.sleep(0.5)
    print("[  0    0 ]")
    time.sleep(0.5)
    print("[         ]")
    time.sleep(0.5)
    print("___________")

def five_():
    print("___________")
    time.sleep(0.5)
    print("[          ]")
    time.sleep(0.5)
    print("[  0    0  ]")
    time.sleep(0.5)
    print("[     0    ]")
    time.sleep(0.5)
    print("[  0    0  ]")
    time.sleep(0.5)
    print("[          ]")
    time.sleep(0.5)
    print("___________")

def six_():
    print("___________")
    time.sleep(0.5)
    print("[          ]")
    time.sleep(0.5)
    print("[  0  0  0 ]")
    time.sleep(0.5)
    print("[          ]")
    time.sleep(0.5)
    print("[  0  0  0 ]")
    time.sleep(0.5)
    print("[          ]")
    time.sleep(0.5)
    print("___________")

loop=True

while loop:
    try:
        a_a=input("enter for roll a dice>>>> ")
        print("please wait......")
        time.sleep(1)
        d=random.randint(1,6)

        if d==1:
            one_()
        elif d==2:
            two_()
        elif d==3:
            three_()
        elif d==4:
            four_()
        elif d==5:
            five_()
        elif d==6:
            six_()
    except:
        print("error....")
        loop=False


        
