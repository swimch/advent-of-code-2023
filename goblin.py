import browser_cookie3
import webbrowser
import requests
from pathlib import Path

day = input()
url = f"https://adventofcode.com/2023/day/{day}"
url_input = f"https://adventofcode.com/2023/day/{day}"

webbrowser.open(url, new=2)

cj = browser_cookie3.firefox()
if not (".adventofcode.com" in str(cj)):
    cj = browser_cookie3.chrome()

webpage = requests.get(f"https://adventofcode.com/2023/day/" + day + "/input", cookies=cj)
Path(f"C:/Users/Sven/OneDrive/Documents/GitHub/advent-of-code-2023/{day:0>2}_SexyCurryboy").mkdir(parents=True, exist_ok=True)
daily_input = open(f"C:/Users/Sven/OneDrive/Documents/GitHub/advent-of-code-2023/{day:0>2}_SexyCurryboy/input.txt", "w")
daily_input.write(webpage.text)
daily_input.close()

f = open(f"C:/Users/Sven/OneDrive/Documents/GitHub/advent-of-code-2023/{day:0>2}_SexyCurryboy/day{day}.py", "w")
