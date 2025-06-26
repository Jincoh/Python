import subprocess
import time
from pathlib import Path
import pyinputplus
from sys import argv

def main():
    path = Path("soundfiles/alarm.wav")
    if len(argv) < 2:
        print("usage: py main.py {duration}")
        return
    try:
        inp = int(argv[1])
    except ValueError:
        print("please supply an integer value as the first argument")
        return

    for i in reversed(range(1, inp + 1)):
        print(i)
        time.sleep(1)
    subprocess.Popen(["play", path])

if __name__ == "__main__":
    main()
