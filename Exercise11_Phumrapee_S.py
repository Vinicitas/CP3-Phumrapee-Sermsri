number = int(input())
for x in range(number):
    text = " "
    print(text*(number-x-1),"*"*(2*x+1))