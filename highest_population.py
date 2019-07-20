import pytest
'''
find the highest population in year givin list of birth and death year for some people
'''


def highest_pop(people):
    yrs = []
    [yrs.append(list(set(range(k, people[k])))) for k in people.keys()]
    d = {}
    flatten = [y for sublist in yrs for y in sublist]
    for y in flatten:
        d[y] = flatten.count(y)
    sorted_yrs = list(sorted(d.items(), key=lambda k: k[1], reverse=True))
    return sorted_yrs[0]


def highest_pop_using_inters(people):
    sets = []
    for k in people.keys():
        sets.append(set(range(k, people[k]+1)))
    s = sets.pop()
    inters = s.intersection(*sets)
    return inters


if __name__ == '__main__':
    lst = {1995: 2010, 1975: 2005, 1980: 2001,
           1999: 2010, 2000: 2010}
    print('highest pop:{}'.format(highest_pop(lst)))


@pytest.mark.parametrize('people,expected', [({1970: 2000, 1975: 2005, 1980: 2000, 1990: 2010, 1970: 2010}, 1990),
                                             ({1995: 2010, 1975: 2005, 1980: 2001,
                                               1999: 2010, 2000: 2010}, 2000)
                                             ])
def test_highest_pop(people, expected):
    assert expected in highest_pop(people), 'failed to get highest population'
