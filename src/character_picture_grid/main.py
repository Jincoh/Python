def main():
    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]


    rows = len(grid)
    i = 0
    for y in range(len(grid[i])):
        if(i <= rows):
            for x in range(len(grid)):
                print(grid[x][y], end="")
            print()
            i += 1
        else:
            break

if __name__ == "__main__":
    main()
