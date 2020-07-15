import requests
from bs4 import BeautifulSoup
from champion import Champion, get_data
from utils import get_all_champions
import pickle

url_list = get_all_champions()


def save():
    champions = get_data()
    with open('data.lol', 'wb') as data:
        pickle.dump(champions, data)


def main():
    for champ_url in url_list:
        url = f'http://www.championcounter.com.br{champ_url}'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        champion = Champion().parse(soup).process_all(soup)
        print(champion.name, 'ok')
    save()


if __name__ == '__main__':
    main()
