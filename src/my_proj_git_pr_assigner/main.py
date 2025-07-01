import re
import requests
import json
import random
from smtplib import SMTP
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    res = requests.get("https://api.github.com/repos/Jincoh/Python-ATBS/pulls")
    res.raise_for_status()
    reslst = json.loads(res.text)

    path = Path("team.json")
    oapath = Path("/home/jinco/Programming/Python/secrets/gmailkey")
    goapath = Path("/home/jinco/Programming/Python/secrets/goatkey")
    with open(oapath) as f:
        oauth = f.readlines()[0]

    with open(path) as f:
        teamdct: dict = json.load(f)

    with open(goapath) as f:
        goat = f.readlines()[0]

    teamlst = list(teamdct.keys()) 
    tasklst = []

    print("compiling tasks...")
    for x in reslst:
        title = x["title"]
        url = x["html_url"]
        state = x["state"]
        aslst = x["assignees"]

        if aslst != [] or state == "closed":
            print("already assigned or already completed")
            continue

        assname = random.choice(teamlst)
        assemail = teamdct[assname] 

        dct = {"title": title, "assemail":assemail,"assname": assname, "state": state, "url": url}
        tasklst.append(dct)

        print(f"assignee = {assemail}\ntitle = {title}\nurl = {url}\nstate = {state}")
        print(json.dumps(tasklst, indent=4))

    print("sending emails...")
    for x in tasklst:
        with SMTP("smtp.gmail.com", 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login("darksoulcgee@gmail.com", oauth)
            body = (f"""Subject: New PR assignment.
You have been assigned a new PR.
    PR name: {x["title"]}
    PR url:  {x["url"]}""")
            result = smtp.sendmail("darksoulcgee@gmail.com", x["assemail"], body)
            logging.info(result)

    print("assigning users...")
    for task in tasklst:
        reg = re.compile(r"(.*\/pulls?\/)(\d+)")
        print(task["url"])
        searchres = reg.search(task["url"])
        if searchres == None:
            print("searchres = none")
            continue
        num = searchres.group(2)

        myheaders = {
                "Authorization": f"token {goat.strip()}"
        }
        mydata = {
                "assignees" : [task["assname"]],
        }

        url = f"https://api.github.com/repos/Jincoh/Python-ATBS/issues/{num}/assignees"
        print(url)
        res = requests.post(url, json=mydata, headers=myheaders)
        print(res.status_code)

    print("done")


if __name__ == "__main__":
    main()
