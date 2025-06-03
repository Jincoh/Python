def main():
    inp = 0
    while(inp == 0):
        try:
            inps = input("input an integer: ")
            inp: int = int(inps)
        except ValueError:
            print("Integer, dumbass")

    while(inp > 1):
        inp = collatz(inp)

def collatz(inp: int) -> int: 
    if(inp  % 2 == 0):
        print(int(inp / 2))
        return int(inp / 2)
    else:
        print((inp * 3) +1)
        return (inp * 3) +1
if (__name__ == "__main__"):
    main()
