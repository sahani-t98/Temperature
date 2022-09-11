temp = float(input("Temperature "))
ch = input("Convert Celsius to Fahrenheit: type-F or Convert Fahrenheit to Celsius: type-C :")
if ch == "C" or "c":
    y = temp * (9 / 5) + 32
    print("Temperature in Fahrenheit:", y, "F")
else:
    y = (temp - 32) * (5 / 9)
    print("Temperature in Celsius:", y, "C")
