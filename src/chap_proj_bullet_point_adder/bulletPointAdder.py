#! /bin/python3
import pyperclip

def main():
    text = pyperclip.paste()
    textl = text.split("\n")
    lines = []
    for x in range(len(textl)):
        lines.append('* ' + textl[x])
    out = "\n".join(lines)
    print(out)
    #pyperclip.copy(out) # still not working will find solution eventually if it ever comes up for now work around redirect output to txt file using > or >> to append
if __name__ == "__main__":
    main()
