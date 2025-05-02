weight = float(input("Enter you weight: "))
unit = input("Kilograms or Pounds? (K or L): ")
if unit.upper() == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is {round(weight,2)} {unit}")
elif unit.upper() == "L":
    weight = weight / 2.205
    unit = "Kilograms."
    print(f"Your weight is {round(weight,2)} {unit}")
else:
    print(f"{weight} is not valid.")
