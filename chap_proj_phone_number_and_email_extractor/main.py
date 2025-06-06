import re
import pyperclip

def main():
    print(pyperclip.paste())
    text = pyperclip.paste()
    phonenum = re.compile(r"""
        (\d{3})
        (\s|-|\.)?
        (\d{3})
        (\s|-|\.)?
        (\d{4})
    """, re.VERBOSE)

    email = re.compile(r"""
        ([a-zA-Z0-9]+)
        (@)
        ([a-zA-Z0-9]+)
        (\.)
        ([a-zA-Z0-9]{2,4})
    """, re.VERBOSE)

    pn = phonenum.findall(text)
    em = email.findall(text)

    print("Phone Numbers")
    for x in pn:
        print("".join(x))
    print()

    print("Emails")
    for x in em:
        print("".join(x))
    print()

if __name__ == "__main__":
    main()
