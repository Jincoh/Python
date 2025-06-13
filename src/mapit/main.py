import webbrowser
import logging
logging.basicConfig(level=logging.DEBUG, format=f"%(asctime)s - %(levelname)s - %(message)s")

from sys import argv
def main():
    search = []
    for x in range(1, len(argv) -1):
        if x < len(argv) -2:
            print(argv[x].strip(","), end="+")
            search.append("%s+" % (argv[x].strip(",")))
        else:
            print(argv[x].strip(","))
            search.append("%s" % (argv[x].strip(",")))
    sStr = "".join(search)
    logging.debug(f"sStr = {sStr}")
    webbrowser.open(f"https://www.google.com/maps/place/{sStr}")

if __name__ == "__main__":
    main()
