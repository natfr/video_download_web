import requests
from bs4 import BeautifulSoup


def get_html(url):
    """
    The function allows to get the URL's data
    """
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False


def get_vk_video(url):
    """
    The function collects info about VK video
    """
    html = get_html(url)
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        # print(soup)
        title = soup.find('div', class_='VideoPageInfoRow__title').text
        video = soup.find('div', class_='VideoPage__video').find_all('source')[1]['src']
        image_url = soup.find('div', class_='VideoPage__video').find_all('img')[0]['src']
        views = soup.find('div', class_='VideoPageInfoRow__views').text
        vk_video = {'video': video, 'image_url': image_url, 'vk_url': url, 'title': title, 'views': views}

        return vk_video
    return False
