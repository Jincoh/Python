import time
import random

def main():
    numQs = 10
    score = 0

    for Q in range(numQs):
        try:
            if takeInput(Q+1):
                print("Correct")
                score += 1
        except outOfTriesException:
            print("Out of tries")
        except TimeoutError:
            print("Out of time")

    print("\nScore: %s" % score)

def takeInput(qnum):
    start = time.time()
    a = random.randint(1,12)
    b = random.randint(1,12)

    count = 0
    while True:
        while True:
            try:
                inp = int(input("Q%s: %s x %s = " % (qnum, a, b)))
                break
            except ValueError:
                print("integers only")
                continue

        if inp == a * b:
            if(not (time.time() - start) < 8.0):
                raise TimeoutError
            return True
        else:
            count += 1
            print("Wrong, %s tries left" % (3 - count))

        if count == 3:
            raise outOfTriesException


class outOfTriesException(Exception):
    pass

if __name__ == "__main__":
    main()
