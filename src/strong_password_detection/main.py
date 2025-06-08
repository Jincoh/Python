import re

def main():
    teststr = input("input the pwd you wish to test: ")
    if(len(teststr) >= 8 and
       re.match(r".*[A-Z].*", teststr)and
       re.match(r".*[0-9].*", teststr)):
        print("password is stronk")
    else:
        print("password is floppy")

if __name__ == "__main__":
    main()
