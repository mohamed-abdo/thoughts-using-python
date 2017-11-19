from datetime import datetime
def interceptor(before=None,after=None,onSuccess=None,onError=None):
    def decorator(func):
        def call(*args,**kwargs):
            try:
                if before is not None:
                    before()
                startTM = datetime.now()
                result = func(*args,**kwargs)
                timeEP = datetime.now() - startTM
                if after is not None:
                    after()
                if onSuccess is not None:
                    onSuccess(result,';time ellipased =>', timeEP.total_seconds() * 1000)
                return result
            except Exception as ex:
                if onError is not None:
                    onError(ex)
        return call
    return decorator

@interceptor(
    before=lambda:print('Before executing ....'),
    after=lambda:print('After executing ....'),
    onSuccess=lambda *x: print('Result =>',*x),
    onError=lambda *x:print(*x))
def SayHello():
    print("Hello world;")
    return 1010;
SayHello()

if __name__ == '__main__':
    print('Hello main ....!')
