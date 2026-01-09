X = input()
if ord(X)>=48 and ord(X)<=64:
    print("IS DIGIT")
elif ord(X)>=65 and ord(X)<=91:
    print("ALPHA\nIS CAPITAL")
elif ord(X)>=97 and ord(X)<=123:
    print("ALPHA\nIS SMALL")