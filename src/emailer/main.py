from sys import argv
from smtplib import SMTP

def main():
    with SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("darksoulcgee@gmail.com", argv[1])
        ebody = ("Subject: automated message. \nDear splonkwomble, \nI regret to inform you that iladies have infiltrated the corporation")
        result = smtp.sendmail("darksoulcgee@gmail.com","autotheautomaton@gmail.com", ebody)
        if result != {}:
            print(result)

    print("done")

if __name__ == "__main__":
    main()
