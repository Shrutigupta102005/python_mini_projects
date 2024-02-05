menu = {
    "black tea": {"ingredients": {"water": 50, "tea": 18}, "cost": 10},
    "plain tea": {"ingredients": {"water": 200, "milk": 150, "tea": 24}, "cost": 15},
    "elachi tea": {"ingredients": {"water": 250, "milk": 100, "tea": 24}, "cost": 30},
}

report = {"Water": 100, "Milk": 50, "tea": 76, "Money": 25}

ch = input("What would you like to have? (black tea/plain tea/elachi tea) ").lower()

if ch == "off":
    print("Have a nice day!")
elif ch == "report":
    print(report)
else:
    if ch in menu:
        if all(report.get(ingredient, 0) >= quantity for ingredient, quantity in menu[ch]["ingredients"].items()):
            print("Money please!")
            if report["Money"] >= menu[ch]["cost"]:
                print("Enjoy your tea!")
                report["Money"] -= menu[ch]["cost"]
                for ingredient, quantity in menu[ch]["ingredients"].items():
                    report[ingredient] -= quantity
            else:
                print("Sorry, not enough money.")
        else:
            print("Sorry, not enough ingredients.")
    else:
        print("Invalid choice.")
