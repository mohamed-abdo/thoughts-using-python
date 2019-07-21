import re


def calculateScore(text, prefixString, suffixString):
    return getScore(prefixString, text) + getScore(suffixString, text)


def getScore(subStr, text):
    score = []
    for s in sliceText(subStr):
        score.append(re.findall(s, text))
    return max([len(item) for subScore in score for item in subScore if len(subScore) > 0])


def sliceText(text):
    s = []
    for idx in range(len(text)):
        [s.append(slice(idx, idx+i, 1)) for i in range(1, len(text))]
    ret = []
    [ret.append(text[i]) for i in s]
    return set(ret)


if __name__ == '__main__':
    print(calculateScore('germany', 'ginger', 'manegment'))
