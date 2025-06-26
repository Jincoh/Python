import requests
import json
from datetime import datetime
from pathlib import Path
from sys import argv

def main():

    path = Path(Path.home() / "Programming/Python/secrets/current_weather_key")

    if(len(argv) >= 3):
        cityname = str(argv[1]) 
        countrycode = "," +  str(argv[2]) 
    elif(len(argv) > 1):
        cityname = str(argv[1]) 
        countrycode = ""
    else:
        print("Usage: python3 main.py {cityname} {countrycode}")
        return

    apikey = None

    with open(path) as f:
        lines = f.readlines()
        apikey = lines[0].strip("\n")

    if apikey == None: 
        print("api key not found")
        return

    # seems that daily forecasts are now free for only students, substituting with 3-hour forecasts
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={cityname}{countrycode}&appid={apikey}&units=metric"

    res = requests.get(url)
    data = json.loads(res.text)
    #print(json.dumps(data, indent=4))
    #print(type(data))
    lst = data["list"]

    for dct in lst:
         print(f"""
+{"-" * 53}+
|{"|".rjust(54)}
|              {f"time: {datetime.fromtimestamp(dct["dt"])}".ljust(39)}|
|{"|".rjust(54)}
+{"-" * 26}+{"-" * 26}+
| {f"temp:                    | {dct["main"]["temp"]}".ljust(52)}|
+{"-" * 26}+{"-" * 26}+
| {f"feels like:              | {dct["main"]["feels_like"]}".ljust(52)}|
+{"-" * 26}+{"-" * 26}+
| {f"weather and descriprion: | {dct["weather"][0]["main"]}; {dct["weather"][0]["description"]}".ljust(52)}|
+{"-" * 26}+{"-" * 26}+
| {f"cloudiness:              | {dct["clouds"]["all"]}%".ljust(52)}|
+{"-" * 26}+{"-" * 26}+
| {f"windspeed and gust:      | {dct["wind"]["speed"]}; {dct["wind"]["gust"]}".ljust(52)}|
+{"-" * 53}+""")
if __name__ == "__main__":
    main()
