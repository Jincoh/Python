#! /bin/python3
import sys
import pyperclip
"""Do not use this script on debian trixie, it will copy something to clipboard that freezes anything its pasted into"""


#import gi
#gi.require_version("Gtk", "3.0")
#from gi.repository import Gtk, Gdk

def main():
#    clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
    phrases = {
            "busy" : "Hey I'm busy right now",
            "agree": "Yeah that sounds great",
            "upsell": "would you like to make a monthly donation"
    }
    if len(sys.argv) < 2:
        print("usage: mclip.py [keyword]")
        sys.exit()

    try:
#       clipboard.set_text(phrases[sys.argv[1]], -1)
        pyperclip.copy(phrases[sys.argv[1]])
        print("copying phrase to keyboard: \n%s" % phrases[sys.argv[1]])
    except KeyError:
        print("no key called %s"% sys.argv[1])

if __name__ == "__main__":
    main()


