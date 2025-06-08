import re

def main():
    inp = input("input text to be stripped: ")
    inc = input("input char to be removed: ") 
    print("\"%s\"" % strip(inp, inc))

def strip(instr: str, char: str = " ") -> str:
    reg = re.compile("^(%s*)(.*?)(%s*)$" % (char,char))
    grps = reg.search(instr)
    if(grps != None):
        return grps.group(2)
    else:
        return "error"


if __name__ == "__main__":
    main()
