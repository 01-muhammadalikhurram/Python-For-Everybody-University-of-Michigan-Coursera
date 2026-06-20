def computepay(h, r):
    if h<=40:
        return h*r
    return (40*r) + ((h-40)*(r*1.5))

hrs = float(input("Enter Hours: "))
ratePerHour = float(input("Enter Rate per Hour: "))
p = computepay(hrs, ratePerHour)
print("Pay", p)