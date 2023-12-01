import browser_cookie3
import webbrowser
import requests
import os

day = input()
url = "https://adventofcode.com/2023/day/" + day
url_input = "https://adventofcode.com/2023/day/" + day



webbrowser.open(url, new=2)

cj = browser_cookie3.firefox()
if not (".adventofcode.com" in str(cj)):
    cj = browser_cookie3.chrome()

webpage = requests.get(f"https://adventofcode.com/2023/day/" + day + "/input", cookies=cj)
daily_input = open("C:/Users/Sven/OneDrive/Documents/GitHub/advent-of-code-2023/" + day + "_SexyCurryboy/input.txt", "w")
daily_input.write(webpage.text)
daily_input.close()

f = open("C:/Users/Sven/OneDrive/Documents/GitHub/advent-of-code-2023/" + day + "_SexyCurryboy/day" + day + ".py", "w")
