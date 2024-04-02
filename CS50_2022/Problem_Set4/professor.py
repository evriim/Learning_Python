"""Little Professor Toy"""
import random


def main():
    """Data is received from the user and checked. 
    Score is calculated based on the number of mistakes"""
    level=get_level()
    i, j, point = 0 , 0 , 10
    a,b, sol = generate_integer(level)

    while i<10:
        try:
            answer =int(input(f"{a} + {b}= "))
            if answer == sol:
                a,b, sol = generate_integer(level)
                i+=1
                j=0
            else:
                print("EEE")
                j+=1
                if j ==1:
                    point-=1
                elif j == 3:
                    print(f"{a} + {b}= {sol}")
                    a,b, sol = generate_integer(level)
                    j=0
                    continue
                raise ValueError
        except ValueError:
            continue
    print("Point: ", point)

def get_level():
    """Setting up level"""
    while True:
        try:
            level=int(input("Level: "))
            if level in {1,2,3}:
                break
        except ValueError:
            continue
    return level

def generate_integer(level):
    """Creating random integer"""
    if level == 1:
        a = int(random.uniform(0,10))
        b = int(random.uniform(0,10))
    elif level == 2:
        a = int(random.uniform(10,99))
        b = int(random.uniform(10,99))
    else:
        a = int(random.uniform(10,999))
        b = int(random.uniform(10,999))
    return a,b, a+b

if __name__ == "__main__":
    main()
