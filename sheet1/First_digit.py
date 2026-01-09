X = int(input())
if X >=100 and X<=999:
    x = X//100
    if(x % 2 == 0):
      print("EVEN")
    else:
     print("ODD")
elif X >999 and X<=9999:
    y = X//1000
    if(y % 2 == 0):
      print("EVEN")
    else:
       print("ODD")