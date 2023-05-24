menuList = []
def showBill():
    print("------My food------")
    for i in range(len(menuList)):
        print(menuList[i][0],menuList[i][1])

while True:
    menuName = input("please enter menu :")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("price :"))
        menuList.append([menuName,menuPrice])
print(menuList)
showBill()