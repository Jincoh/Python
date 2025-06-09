import random
import pandas as pd

from pathlib import Path as path

def main():
    CVSPATH = path("us-state-capitals.csv")
    csv = pd.read_csv(CVSPATH)

    QUESTIONS: int = 50
    NUMFILES: int = 10

    for j in range(NUMFILES):

        qfilepath = path(r"sheets/qfiles/qfile%s" % (j + 1))
        afilepath = path(r"sheets/afiles/afile%s" % (j + 1))
        qfile = open(qfilepath, "w")
        afile = open(afilepath, "w")
        qfile.write("")
        afile.write("")
        qfile.close
        afile.close

        qfile = open(qfilepath, "a")
        afile = open(afilepath, "a")

        for i in range(QUESTIONS):
            """to change it to random questions uncomment line 30 and remove the "i" """

            x = i #random.randint(0, len(csv) -1)
            
            possibleAns = [csv.iat[x,1]]
            while(len(possibleAns) < 4):
                y = random.randint(0,len(csv)-1)
                if csv.iat[y,1] not in possibleAns:
                    possibleAns.append(csv.iat[y,1])

            random.shuffle(possibleAns)

            a, b, c, d = possibleAns
            print(" %s out of %s"% (x,len(csv) - 1))
            print("%s : %s \n (a) %s, (b) %s, (c) %s, (d) %s" % (csv.iat[x,0], csv.iat[x,1], a,b,c,d))
            qfile.write("(Q%s) %s :\n (a) %s, (b) %s, (c) %s, (d) %s\n" % (i + 1, csv.iat[x,0], a, b, c, d))
            afile.write("(Q%s) capital of %s = %s\n" % (i + 1, csv.iat[x,0], csv.iat[x,1]))


if __name__ == "__main__":
    main()
