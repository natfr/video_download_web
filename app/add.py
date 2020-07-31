import requests
from bs4 import BeautifulSoup


def get_html(url):
    try:
        result=requests.get(url)
        result.raise_for_status()
        html=result.text
        return html
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False

def get_content(url):
    html = get_html(url)
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        print(soup)

#get_content("https://ok.ru/live/904068997114")




