import ezsheets 
#reminder don't use this import in any production code
#reminder check import author before importing

def main():
    wb = ezsheets.Spreadsheet("1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg")
    sheet = wb["Sheet"]
    count = 1
    for row in sheet:
        if count > 1:
            try:
                if int(row[0]) * int(row[1]) != int(row[2]):
                    print(f"{count} is wrong")
            except ValueError:
                break
        count += 1


if __name__ == "__main__":
    main()
