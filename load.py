import pickle
import collections
from operator import itemgetter

from champion import Champion

stats = {}


def checkKey(dict, key):
    if key in dict:
        return dict[key]
    else:
        return 0


def find(allies: list, enemies: list, data: list):
    for ally in allies:
        champion = data[data.index(Champion(data_name=ally))]
        for good in champion.good_with:
            last = checkKey(stats, good.secondary.data_name)
            stats[good.secondary.data_name] = good.value + last

    for enemy in enemies:
        champion = data[data.index(Champion(data_name=enemy))]
        for strong in champion.strong_against:
            last = checkKey(stats, strong.secondary.data_name)
            stats[strong.secondary.data_name] = strong.value - last

        for weak in champion.weak_against:
            last = checkKey(stats, weak.secondary.data_name)
            stats[weak.secondary.data_name] = weak.value + last


def main():
    with open('data.lol', 'rb') as data:
        champions = pickle.load(data)
        find(
            allies=[
                'hecarim',
                'vayne',
                'lulu',
                'ezreal',
            ],
            enemies=[
                'ekko',
                'renekton',
                'syndra',
            ],
            data=champions
        )

        sorted_dict = collections.OrderedDict(sorted(stats.items(), key=itemgetter(1)))
        print(sorted_dict)


if __name__ == '__main__':
    main()
