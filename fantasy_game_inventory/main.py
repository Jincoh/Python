def main():
    inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    invPrinter(inv)
    addToInventory(inv, dragonLoot)
    invPrinter(inv)

def invPrinter(inv: dict):
    inv_sorted = dict(sorted(inv.items()))
    print("Inventory: ")
    for x in inv_sorted:
        print(inv_sorted[x], x,sep=" ", end="\n")
    count = 0
    for x in inv_sorted.values():
        count += x
    print("Total number of items:", count)
    print()

def addToInventory(inv: dict, addItems: list):
    for x in addItems:
        inv.setdefault(x, 0)
        inv[x] += 1

if __name__ == "__main__":
    main()
