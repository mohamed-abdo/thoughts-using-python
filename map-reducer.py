def LoggerWrapper():
    def deocrated(func):
        def call(*args,**kwargs):
            result=func(*args,**kwargs)
            print('result logging => ',result)
            return result
        return call
    return deocrated

from functools import reduce

def doubleNum(i):
    return i*2
def BinaryMulitpNum(i):
    return 2 ** i
def evenNum(i):
    return i % 2 == 0
ar=range(0,10)

@LoggerWrapper()
def mapReducre(xf,predicate,iterateble):
    def _reducer(accumlate,value):
        if predicate(value):
            accumlate.append(xf(value))
            return accumlate
        else:
            return accumlate
    return reduce(_reducer,iterateble,[])
result=mapReducre(doubleNum, evenNum, ar)
print('map reducre of list:',list(ar),' is after getting double of the even numbers:',result)

result=mapReducre(BinaryMulitpNum, evenNum, ar)
print('map reducre of list:',list(ar),' is after getting binay multiplication of the even numbers:',result)
