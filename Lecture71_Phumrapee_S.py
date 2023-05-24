menuList = []
priceList = []
def showBill():
    print("------My food------")
    Totalprice = 0
    for i in range(len(menuList)):
        print(menuList[i],priceList[i])
        Totalprice += priceList[i]
        print("Totalprice is",Totalprice,"THB")

while True:
    menuName = input("please enter menu :")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("price :"))
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()