import random

def main():
    count = 0
    for _ in range(10000):
        flip = [random.randint(1,2) for _ in range (100)]
        if(consix(flip)):
            count += 1

    print("chance of Streak: %s%%" % (count/100))

def consix(flip):
    for i in range(0, 94, 1):
        if(flip[i:i+6].count(flip[i]) >= 6):
            return True
    return False

if __name__ == "__main__":
    main()
