def main():
    spam = ["apples", "bananas", "tofu", "cats"]
    for x in range(len(spam)):
        if(x < len(spam) -1):
            print(spam[x], end = " and ")
        else:
            print(spam[x])

if __name__ == "__main__":
    main()
