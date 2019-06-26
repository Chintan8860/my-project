while 1:
    print("1) sum + 2) sub - 3) mul * 4) div / ")
    x = input("enter a choise : ")
    c=x.lower()
    a = input("enter value of a : ")
    b = input("enter value of b : ")
    if c == 'sum' or  c == '+' or c == '1':
        if a=='' and b=='':
            print("value of sum 'a' and 'b' ")
        elif b=='':
            b=0;
            ans=int(a)+int(b);
            print("value of sum is ",ans)
        elif a=='':
            print(" please insert a value of a ")
        else:
            ans = int(a) + int(b)
            print("value of sum = ", ans)
    elif c == 'sub' or c == '-' or c == '2':
        if a == '' and b == '':
            print(" plese insert a value of 'a' and 'b' : ")
        elif b == '':
            b = 0;
            ans = int(a) - int(b);
            print("value of sub is ", ans)
        elif a == '':
            print(" please insert a value of a ")
        else:
            ans = int(a) - int(b)
            print("value of sub = ", ans)
    elif c == 'mul' or c == '*' or c == '3':
        if a == '' and b == '':
            print("insert value of 'a' and 'b' :")
        elif b == '':
            b = 1;
            ans = int(a) * int(b);
            print("value of multiplication  is ", ans)
        elif a == '':
            print(" please insert a value of a ")
        else:
            ans = int(a) * int(b)
            print("value of multiplication  = ", ans)
    elif c == 'div' or c == '/' or c == '4':
        if a == '' and b == '':
            print("insert value of 'a' and 'b' :")
        elif b == '':
            b = 1;
            ans = int(a) / int(b);
            print("value of division is ", ans)
        elif a == '':
            print(" please insert a value of a ")
        else:
            ans = int(a) / int(b)
            print("value of division   = ", ans)
    else:
        print("insert correct opration")
        break
