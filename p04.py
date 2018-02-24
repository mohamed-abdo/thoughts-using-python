import re
def splitClosingChar(s):
    if s is None:
        raise TypeError('input string is mandatory')
    if len(s)>100000:
        raise ValueError('string length is too long')
    legal_chars= '^[(\(|\))]+$'
    if not re.match(legal_chars,s):
        raise ValueError('string contains illegal characters')
    right=[r for r in s if r ==')']
    return len(right)

def maxDistance(a, b, c, d):
    if not isinstance(a,int):
        raise TypeError('input must be integer')
    if not isinstance(b,int):
        raise TypeError('input must be integer')
    if not isinstance(c,int):
        raise TypeError('input must be integer')
    if not isinstance(d,int):
        raise TypeError('input must be integer')
    if a >5000 or a < -5000 :
        raise ValueError('input is out of range')
    if b >5000 or b < -5000 :
        raise ValueError('input is out of range')
    if c >5000 or c < -5000 :
        raise ValueError('input is out of range')
    if d >5000 or d < -5000 :
        raise ValueError('input is out of range')
    lst=[a, b, c, d]
    absLst=[abs(number) for number in lst]
    largest = max(absLst)
    dupLargest=absLst.count(largest)
    if dupLargest>1:
        return largest*2
    second_largest = max(i for i in absLst if i < largest)
    if second_largest is None:
        second_largest=largest
    return largest + second_largest
    # write your code in Python 3.6
if(__name__=='__main__'):
    print(maxDistance(-9,-4,9,4))
