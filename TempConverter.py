unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
value = float(input("Enter the temperature: "))
if unit.upper() == "C":
    value = round(value * (9 / 5) + 32, 1)
    print(f"The temperature in Fahrenheit is {value}°F")
elif unit.upper() == "F":
    value = round((value - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is {value}°C")
else:
    print(f"{unit} is an invalid unit of measurement.")
