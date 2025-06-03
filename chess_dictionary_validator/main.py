import pprint
import sys
import re

def main():
    chd = {'1h': 'bking', '6c': 'wqueen', '2g' : "bbishop", "5h" : "bqueen", "3e" : "wking"}
    pieces = {}

    for x in chd.values():
        pieces.setdefault(x , 0)
        pieces[x] = pieces[x] + 1


    try:
        if(not (pieces["bking"] == 1 and pieces["wking"] == 1)):
            print("too many kings")
            sys.exit()

    except KeyError:
        print("missing king")
        sys.exit()

    pieces.setdefault("wpawn", 0)
    pieces.setdefault("bpawn", 0)
    if((pieces["bpawn"] > 8 or pieces["wpawn"] > 8)):
        print("Too many pawns")
        sys.exit()

    sum = 0
    for x in pieces.values():
        sum += x

    if sum > 16:
        print("too many pieces")
        sys.exit()

    for x in chd:
        if(not(re.match("[1-8][a-h]", x))):
            print("invalid position: " + x)
            sys.exit()

    pprint.pp(pieces, width = 1)

if __name__ == "__main__":
    main()
