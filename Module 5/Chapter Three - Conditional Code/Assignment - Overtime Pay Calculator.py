hrs = float(input("Enter Hours: "))
phr = float(input("Enter Pay per Hour: "))
if(hrs <= 40):
    print (hrs*phr)
else:
    print ((40*phr) + ((hrs-40)*(phr*1.5)))