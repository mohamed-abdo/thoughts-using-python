class PrimGenerator:
    def __init__(self):
        self.num=0
    
    def __isPrime(self, num):
        return not any(i for i in range(2,num) if num % i ==0)

    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            self.num +=1
            if self.__isPrime(self.num):
                return self.num

pGen= PrimGenerator()         

def isPrime(num):
    return not any(i for i in range(2,num) if num % i ==0)

for i in range(1,10000):
    print(i,isPrime(i),next(pGen))
