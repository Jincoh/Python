import json
import pprint
import sys

from pathlib import Path

def main():
    fpath = Path("json")
    SAVE = "save"
    
    with open(fpath) as f:
        outdata = json.load(f)

    if( len(sys.argv) < 2 or
    sys.argv[1] == SAVE and len(sys.argv) < 4):

        print("""Usage:
        python3 main.py [save] option [value]

        if the save option is used it will write
        to the json file with option as the key and
        value as the value
        """)

        return None

    if(sys.argv[1] == SAVE):
        key = sys.argv[2]
        value = sys.argv[3]

        outdata[key] = value
        with open(fpath, "w") as f:
            json.dump(outdata,f, indent=4)

    else:
        key = sys.argv[1]

        if key in outdata:
            print(outdata[key])
        else:
            print("no option of this name exits, Available options:\n%s" % (pprint.pformat(outdata)))

if __name__ == "__main__":
    main()
