def main():
    inp = input("input the message to be turned to pig latin:\n")
    vowels = ("a", "e", "i", "o", "u","A","E","I","O","U")
    lst = []
    for word in inp.split():
        pfl = ""
        snl = ""

        if not word[1].isalpha():
            pfl = word[1]
            word = word[1:]
        if not word[-1].isalpha():
            snl = word[-1]
            word = word[:-1]

        if word.startswith(vowels):
            word = word + "yay"
        elif(word.isalpha()):
            word = word[1:] + word[0] + "ay"

        lst.append(pfl + word + snl)

    print(" ".join(lst))
if __name__ == "__main__":
    main()
