def main():
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]

    """
    we take as assumed the inner lists are always the same length to save
    time, the point of this excersise is to mess with text justification
    """
    for x in range(len(tableData)):
        biggest = 0
        for y in range(len(tableData[x])):
            if len(tableData[x][y]) > biggest: biggest = len(tableData[x][y])
        for y in range(len(tableData[x])):
            tableData[x][y] = tableData[x][y].rjust(biggest)

    buf = [[tableData[x][y] for x in range(len(tableData))]for y in range(len(tableData[0]))]

    for x in buf:
        for y in x:
            print(y, end = "   ")
        print()

if __name__ == "__main__":
    main()
