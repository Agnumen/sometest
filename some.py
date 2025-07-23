def some_decorator(func):
    def wrapper():
        print("</--\>")
        func()
        print("<\--/>")
    return wrapper

@some_decorator
def burger(meat='~beef~'):
    print(meat)
    
burger()