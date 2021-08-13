import requests


def get_latest(url):
    response = requests.get(url)
    temp = response.text.split("label-latest")[1].split("list-style-none")[1]
    latest = temp.split("title=\"")[1].split("\"")[0]
    if "v" in latest:
        latest = latest.replace("v", "")

    return latest


def isInternet():
    try:
        requests.get("https://www.google.com/")
        return True
    except:
        return False
