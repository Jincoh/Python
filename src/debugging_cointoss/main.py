import random
import logging

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
logging.disable(logging.CRITICAL)
def main():
    guess = ''
    while guess not in ('heads', 'tails'):
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()

    logging.debug("Guess = " + guess)
    toss = random.randint(0, 1) # 0 is tails, 1 is heads
    logging.debug("toss = " + str(toss))

    if toss == 0:
        tossStr = "tails" 
    else:
        tossStr = "heads"
    logging.debug("toss = " + str(tossStr))
    if tossStr == guess:
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guess = input()
        if tossStr == guess:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')

if __name__ == "__main__":
    main()
