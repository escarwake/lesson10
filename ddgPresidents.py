import requests
import pytest

url = "https://api.duckduckgo.com/?q=presidents+of+the+united+states&format=json"
response = requests.get(url)
mydata = response.json()
related = mydata["RelatedTopics"]

presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Jackson", "Van Buren",
              "Harrison", "Tyler", "Polk", "Taylor", "Fillmore", "Pierce", "Buchanan",
              "Lincoln", "Johnson", "Grant", "Hayes", "Garfield", "Arthur", "Cleveland",
              "McKinley", "Roosevelt", "Taft", "Wilson", "Harding", "Coolidge", "Hoover",
              "Truman", "Eisenhower", "Kennedy", "Nixon", "Ford", "Carter", "Reagan",
              "Bush", "Clinton", "Obama", "Biden"]

textToCheck = []

for i in related:
    check = i['Text']
    textToCheck.append(check)


def test_presidents():
    for pres in presidents:
        for text in textToCheck:
            if text.__contains__(pres):
                test = 1
                continue
            else:
                continue
    assert test == 1,  "President " + pres + " not listed"


test_presidents()

