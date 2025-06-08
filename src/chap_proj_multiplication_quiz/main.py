import pyinputplus as inp
import time
import random

def main():
    num = 10
    correctAns = 0
    for q in range(num):
        n1 = random.randint(0,12)
        n2 = random.randint(0,12)
        try:
            inp.inputStr("#%s: %s x %s = " % (q, n1, n2), allowRegexes=["^%s$" % (n1 * n2)], blockRegexes=[(".*", "Incorrect!")], timeout=8, limit=3)
        except inp.TimeoutException:
            print("Out of time")
        except inp.RetryLimitException:
            print("Out of tries")
        else:
            print("Correct")
            correctAns += 1

        time.sleep(1)
    print("Score = %s / %s" % (correctAns, num))


if __name__ == "__main__":
    main()
