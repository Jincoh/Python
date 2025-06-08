import pyinputplus as inp

def main():
    while(True):
        if inp.inputYesNo("Do you want to know how to keep an idiot busy for hours?\n") == "no":
            break
        else:
            print("Thank you have a nice day")


if __name__ == "__main__":
    main()
