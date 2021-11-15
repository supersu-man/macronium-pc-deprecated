import requests
from bs4 import BeautifulSoup

def get_latest(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    latestversion = soup.find_all(lambda tag: tag.name == 'span' and tag.get('class') == ['ml-1'])
    latest = latestversion[0].text.strip()
    if "v" in latest:
        latest = latest.replace("v", "")
    return latest

def isInternet():
    try:
        requests.get("https://www.google.com/")
        return True
    except:
        return False