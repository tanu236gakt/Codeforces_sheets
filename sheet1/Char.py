X = input()
if ord(X)>=65 and ord(X)<=91:
    X=ord(X) +32
    print(chr(X))
elif ord(X)>=97 and ord(X)<=123:
    X = ord(X)-32
    print(chr(X))