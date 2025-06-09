from pathlib import Path

def main():
    path = Path("lib/madlib1")
    outpath = Path("output/ofile")

    with open(path) as f:
        madlib = f.read()

    for x in madlib.split():
        #print("\"%s\"" % x)
        if x.strip(".") in ["VERB", "NOUN"]:
            madlib = madlib.replace(x,input("Enter a %s:\n" % (x.strip("."))), count=1)
        elif x.strip(".") in ["ADJECTIVE", "ADVERB"]:
            madlib = madlib.replace(x,input("Enter an %s:\n" % (x.strip("."))), count=1)

    with open(outpath, "w") as f:
        f.write(madlib)


if __name__ == "__main__":
    main()
