from bs4 import BeautifulSoup
import requests

url = "https://www.facebook.com/muftimenk/?hc_ref=NEWSFEED&fref=nf"
res = requests.get(url)
def get_posts():
    soup = BeautifulSoup(res.content,'html.parser')
    p = soup.find_all('p')
    return p

p = get_posts()
print(p)
