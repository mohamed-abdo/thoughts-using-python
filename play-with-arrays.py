
def kDifference(a, k):
        # O(N**2)
        # return len([(x,y) for x in a for y in a if x+k==y])
        # mask results with bit wise operator to get linear complexity O(N)
        return len(set(a) & set(x + k for x in a))

print(kDifference([1,2,3,4,5,6,7],3))

def mergeArrays(a, b):
    return sorted([i for subList in ((x,y) for x,y in zip(a,b)) for i in subList])

print(mergeArrays([1,2,3,4,5],[0,5,3,2,1,0]))
