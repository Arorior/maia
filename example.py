from maia import switch

x = 10
for case in switch(x):
    if case(0):
        print('num is 0')
        break
    elif case(10):
        print('num is 10')
        break
    else:
        print('num not in list')
        break
