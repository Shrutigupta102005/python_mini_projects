bill = int(input("enter your bill amount"))
person = int(input("enter the number of person "))
tip = int(input("enter the amount of tip in %"))
pay_tip = bill *(tip/100)
amt = (bill/person ) + pay_tip
print(f"you have to pay{amt}")
