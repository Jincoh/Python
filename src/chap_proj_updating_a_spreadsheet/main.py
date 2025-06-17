import openpyxl

from pathlib import Path

def main():
    #lemons = 0.5   | garlic = 0.75   | Celery = 0.25
    path = Path("produceSales3.xlsx")
    wb = openpyxl.load_workbook(path)
    sheet = wb.active
    if sheet == None:
        return

    rows = sheet.iter_rows(min_col=1, max_col=2)
    for rowc in rows:
        products,price = rowc
        match products.value:
            case "Lemon":
                print("match L")
                sheet[price.coordinate].value = 0.5

            case "Garlic":
                print("match G")
                sheet[price.coordinate].value = 0.75

            case "Celery":
                print("match C")
                sheet[price.coordinate].value = 0.25
        
    wb.save("done.xlsx")

if __name__ == "__main__":
    main()
