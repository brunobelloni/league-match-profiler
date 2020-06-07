from bs4 import BeautifulSoup
from enum import Enum
from utils import only_numerics

champions = list()


class TypeChampionRel(Enum):
    WEAK_AGAINST = 'weakAgainst', 1
    STRONG_AGAINST = 'strongAgainst', 2
    GOOD_WITH = 'goodWith', 3

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    # ignore the first param since it's already set by __new__
    def __init__(self, _: str, description: str = None):
        self._description_ = description

    def __str__(self):
        return self.value

    # this makes sure that the description is read-only
    @property
    def description(self):
        return self._description_


class Champion:
    def __init__(self, name: str = None, data_name: str = None, img_url: str = None):
        self.name = name
        self.img_url = img_url
        self.data_name = data_name
        self.good_with: list[ChampionRel] = list()
        self.weak_against: list[ChampionRel] = list()
        self.strong_against: list[ChampionRel] = list()

    def parse(self, soup: BeautifulSoup):
        div = soup.find(id='main_champ')
        self.name = div.find('h1').text
        self.data_name = div.attrs['data-name']
        self.img_url = div.find('img').attrs['src']
        if self in champions:
            return champions[champions.index(self)]
        champions.append(self)
        return self

    def execute(self, soup: BeautifulSoup, id_selector: str, list_ref: list):
        div = soup.find(id=id_selector)
        weakAgainstList = div.find_all('a', class_='entity')
        for weakAgainst in weakAgainstList:
            champion = Champion(
                name=weakAgainst.find('h4').text,
                data_name=weakAgainst.attrs['data-name'],
                img_url=weakAgainst.find('img').attrs['src'],
            )

            if champion in champions:
                champion = champions[champions.index(champion)]

            championRel = ChampionRel(
                primary=self,
                secondary=champion,
                type=TypeChampionRel(id_selector),
                value=only_numerics(weakAgainst.find('small').text),
            )

            list_ref.append(championRel)

    def process_all(self, soup: BeautifulSoup):
        self.execute(soup=soup, id_selector='goodWith', list_ref=self.good_with)
        self.execute(soup=soup, id_selector='weakAgainst', list_ref=self.weak_against)
        self.execute(soup=soup, id_selector='strongAgainst', list_ref=self.strong_against)
        return self

    def __eq__(self, o: object) -> bool:
        return o.data_name == self.data_name



class ChampionRel:
    def __init__(self, primary: Champion, secondary: Champion, value: int, type: TypeChampionRel):
        self.primary = primary
        self.secondary = secondary
        self.value = value
        self.type = type
