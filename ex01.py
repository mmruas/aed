import re

def is_int(num):
    while True:
        try:
            int(num)
            return True
        except ValueError:
            return False

def askFibonacci():
    print("Enter the number for fibonacci")
    nFib = (input("n: "))

    if is_int(nFib):
        return int(nFib)
    else:
        print("Please enter a valid number")
        return askFibonacci()

def invertString(s):

    if len(s) < 1:
        return s
    else:
        lastLetter = s[len(s) - 1:]
        s = s[:-1]
        return lastLetter + invertString(s)

def cleanString(s):
    s = s.replace(" ", "")
    s = s.replace(";", "")
    s = s.replace(".", "")
    s = s.replace(",", "")
    s = s.replace("!", "")
    s = s.replace("?", "")
    s = s.replace(":", "")
    s = s.replace("-", "")
    s = s.replace("_", "")
    s = s.replace("(", "")
    s = s.replace(")", "")
    s = s.replace("/", "")
    s = s.lower()
    #s = re.sub(r'[^\w\s]', '', s)
    return s

def checkPalyndrome(s):
    s = cleanString(s)

    if len(s) <= 2:
        return True
    else:
        firstLetter = s[:1]
        lastLetter = s[len(s) - 1:]
        if firstLetter == lastLetter:
            s = s[1:-1]

            return checkPalyndrome(s)
        else:
            return False


def invertList(l):
    return [l.pop()] + invertList(l) if len(l) > 1 else l


def factorial(n):
    return 1 if n <= 1 else n * factorial(n-1)

def fibonacciRecursive(n: int):
    return 1 if n < 2 else fibonacciRecursive(n-1) + fibonacciRecursive(n-2)

def fibonacciIterative(n: int):
    if n < 2:
        return 0
    else:
        x = 0
        y = 1
        for i in range(n):
            z = (x + y)
            x = y
            y = z
        return y

def pascalTriangle(n):
    m = n - 1
    if n > 1:
        for i in range(m):
            a = (factorial(m)) / (factorial(i) * factorial(m - i))
            print(int(a), end = ' ')
        print("1")
        return pascalTriangle(m)
    else:
        print("1")





print(invertString("ramo"))
print(checkPalyndrome("live not on evil"))
print(checkPalyndrome("Reviver"))
print(invertList([1, 2, 3, 4, 5]))
print(invertList([1]))
print(fibonacciRecursive(5))
print((fibonacciIterative(5)))
print(fibonacciIterative((askFibonacci())))
print(fibonacciRecursive((askFibonacci())))
print(factorial(5))
pascalTriangle(5)