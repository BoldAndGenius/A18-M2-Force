a=int(input("Enter Number: "))
b=int(input("Enter Number: "))
c=int(input("Enter Number: "))
d=int(input("Enter Number: "))
if a>b:
    if a>c:
        if a>d:
          if d>b and d>c:
              print(" d is 2nd largest")
          elif b>d and b>c:
              print(" b is 2nd largest")
          else:
              print("c is 2nd largest")
        else:
            if a>b and a>c:
                print("a is 2nd largest")
            elif b>c and b>d:
                print("b is 2nd largest")
            else:
                print("c is 2nd largest")
    else:
        if c>d:
            if d>a and d>b:
                print("d is 2nd largest")
            elif b>a and b>d:
                print("b is 2nd largest")
            else:
                print("a is 2nd largest")
        else:
            if c>a and c>b:
                print("c is 2nd largest")
            elif a>c and a>b:
                print("a is 2nd largest")
            else:
                print("b is 2nd largest")
else:
    if b>c:
        if b>d:
            if d>a and d>c:
                print("d is 2nd largest")
            elif c>a and c>d:
                print(" c is 2nd largest")
            else:
                print("a is 2nd largest")
        else:
            if b>a and b>c:
                print("b is 2nd Largest")
            elif a>c and a>d:
                print("a is 2nd largest")
            else:
                print("c is 2nd largest")
    else:
        if c>d:
            if d>a and d>b:
                print("d is 2nd largest")
            elif a>b and a>d:
                print(" a is 2nd largest")
            else:
                print("b is 2nd largest")
        else:
            if c>a and c>b:
                print("c is 2nd largest")
            elif b>a and b>c:
                print("b is 2nd largest")
            else:
                print("a is 2nd largest")
                