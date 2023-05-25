systemMenu = {"ข้าวหมกไก่":45,"ข้าวมันไก่":40,"ข้าวมันหมกไก่":50,"ข้าวหน้าไก่":40}
menuList = []
def showBill():
    print("------My food------")
    totalprice = 0
    for i in range(len(menuList)):
        print(menuList[i][0],menuList[i][1])
        totalprice += menuList[i][1]
    print("Totalprice is",totalprice,"THB")

while True:
    menuName = input("please enter menu :")
    if (menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])
print(menuList)
showBill()