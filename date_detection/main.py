import re
import pprint

def main():
    teststring = """
    on the date 12/02/1995 a man by the name of wonk emerged from a deep slumber,
    a day later 13/02/1995 he died. On the same day 4 years later 13/02/1999 absolutely
    nothing interesting happened whatsoever. 29/02/2020 29/02/2100
    """
    reg = re.compile(r"""
        ((0[1-9])|([1-3][0-9]))\/
        ((0?[1-9])|(1[0-3]))\/
        ([1-2][0-9]{3})
    """, re.VERBOSE)

    out = reg.findall(teststring)
    
    validDates = []
    for x in out:
        match x[3]:
            case "01" | "03" | "05" | "07" | "08" | "10" | "12":
                if(int(x[0]) <= 31):
                    validDates.append("%s/%s/%s" % (x[0],x[3],x[6]))
            case "04" | "06" | "09" | "11":
                if(int(x[0]) <= 30):
                    validDates.append("%s/%s/%s" % (x[0],x[3],x[6]))
            case "02":
                year = int(x[6])
                if(int(x[0]) <= 28 or
                (int(x[0]) == 29 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)))):
                    validDates.append("%s/%s/%s" % (x[0],x[3],x[6]))
    pprint.pprint(validDates,width = 1)


if __name__ == "__main__":
    main()
