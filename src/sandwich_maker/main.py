import pyinputplus as inp
def main():
    price = 1
    print("Pick your Bread")
    inp.inputMenu(choices=["Wheat €1", "White €1", "Sourdough €1"], numbered=True)
    print("Pick your protein")
    if inp.inputMenu(choices=["Chicken €2", "Turkey €2", "Ham €2", "Tofu €4"], numbered=True) == "Tofu €4":
        price += 4
    else: 
        price += 2
    if inp.inputYesNo("Do you want cheese €1: ") == "yes":
        inp.inputMenu(["Cheddar", "Swiss", "Mozzarella"], "Cheese choices", numbered=True)
        price += 1

    if inp.inputYesNo("Any salad or sauce? €1: ") == "yes":
        inp.inputMenu(["mayo", "mustard", "lettuce", "tomato"], "Salad or sauce", numbered=True)
        price += 1

    price = price * inp.inputInt("How many sandwiches", min=1)
    print(price)




if __name__ == "__main__":
    main()
