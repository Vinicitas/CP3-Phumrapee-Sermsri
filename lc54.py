def login():
    username = input("usermameInput :")
    password = input("passwordInput :")
    if username == "vinicitas" and password == "asdf":
        return True
    else :
        return False
def showMenu():
    print("Welcome Vinicitas !!")
    print("1. vatCalculate")
    print("2. priceCalculate")
def menuSelect():
    userselected = int(input(">>"))
    return userselected
def vatCalculate(totalprice):
    vat = 7
    result = totalprice + (totalprice*vat/100)
    return result
def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculate(price1 + price2)

login()
showMenu()
menuSelect()
    if menuSelect() == 1:
        print(priceCalculate())
    elif menuSelect() == 2:
        price1 = int(input("First Product Price : "))
        print(price1+price2)