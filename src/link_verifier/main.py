import requests
from sys import argv

def main():
    res = requests.get(argv[1])
    try:
        res.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print("Broken Link")
        else:
            print("error = ", e)
    else:
        print("link works fine")

if __name__ == "__main__":
    main()
