username = input("usermameInput :")
password = input("passwordInput :")
if username == "vinicitas" and password == "asdf":
    print("Welcome Vinicitas !!")
    print("1. coke 10 THB")
    print("2. cake 20 THB")
    coke = 10
    cake = 20
    userselected = int(input(">>"))
    if userselected == 1:
        amount1 = int(input("amount1 :"))
        print("Net price =", coke * amount1, "THB")
    elif userselected == 2:
        amount2 = int(input("amount2 :"))
        print("Net price =", cake * amount2, "THB")
    elif userselected == 12:
        amount1 = int(input("amount1 :"))
        amount2 = int(input("amount2 :"))
        print("Net price =", coke * amount1 + cake * amount2, "THB")

