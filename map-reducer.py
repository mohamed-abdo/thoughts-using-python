from functools import reduce
def doubleNum(i):
    return i*2
def evenNum(i):
    return i % 2 == 0
ar=range(0,10)
def mapReducre(xf,predicate,iterateble):
    def _reducer(accumlate,value):
        if predicate(value):
            accumlate.append(xf(value))
            return accumlate
        else:
            return accumlate
    return reduce(_reducer,iterateble,[])
result=mapReducre(doubleNum,evenNum,ar)
print('map reducre of list:',list(ar),' is after double even numbers:',result)
