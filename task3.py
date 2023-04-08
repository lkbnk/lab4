def MagicDate(dd,mm,yy):
    dm = dd * mm
    year = int(yy[-1] + yy[-2])
    if dm == year:
        return print("True")
    else:
        return print("False")

a = int(input("Введите день: "))
b = int(input("Введите месяц: "))
c = list(input("Введите год: "))

MagicDate(a,b,c)