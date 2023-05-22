def login():
    username = input("usermameInput :")
    password = input("passwordInput :")
    if username == "vinicitas" and password == "asdf":
        print("Success!")
        return showMenu()
    else:
        print("Fail!")
        return login()


def showMenu():
    print("Welcome Vinicitas !!")
    print("1. vatCalculate")
    print("2. priceCalculate")
    return menuSelect()


def menuSelect():
    userselected = int(input(">>"))
    if userselected == 1:
        return vatCalculate()
    elif userselected == 2:
        return priceCalculate()


def vatCalculate():
    totalprice = int(input("total price :"))
    vat = 7
    result = totalprice + (totalprice * vat / 100)
    return result


def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return price2+price1
print("ราคารวม",login(),"บาท")