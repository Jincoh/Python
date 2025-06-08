import pyperclip
import sys

def main():
    while(True):
        inp = input("input message to go to clipboard")
        if(inp == "q"):
            sys.exit()
        pyperclip.copy(inp)
        
"""
note,
copying to clipboard from pyperclip then attempting to paste either freeses the window where the text is pasted or crashes it

this is happening on debian trixie 04/06/2025

note to self future project idea:
make this but it actually works
"""

if __name__ == "__main__":
    main()
