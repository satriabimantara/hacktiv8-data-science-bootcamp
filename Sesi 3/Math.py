def sum(a,b):
    return a+b

def substract(a,b):
    return a-b

def factorial(n):
    return n*factorial(n-1) if n>1 else 1


if __name__ == "__main__":
    import sys
    if len(sys.argv) >1:
        print(factorial(int(sys.argv[1])))