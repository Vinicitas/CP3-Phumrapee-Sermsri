def vatCalculate(totalprice):
    result = totalprice+(totalprice*7/100)
    return result
x = int(input("input totalprice :"))
print(vatCalculate(x))