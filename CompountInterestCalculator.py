
principle = 0
rate = 0
time=0

while True:
    principle= float (input('enter the principle amount: ') )
    if principle<0:
        print("principle can't be  less than  zero")
    else:
        break

while True:
    rate= float (input('enter the interest rate : ') )
    if rate<0:
        print("interest rate can't be  less than zero")
    else:
        break

while True:
    time= int (input('enter the time in years : ') )
    if time<0:
        print(" time can't be  less than zero") 
    else:
        break           

total = principle * pow(( 1 + rate / 100), time)
print(f"balance after {time} year/s: ₹ {total:.2f} :")
