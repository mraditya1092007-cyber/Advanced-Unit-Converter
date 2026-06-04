# =====================================
# ADVANCED UNIT CONVERTER TOOL
# =====================================

while True:

    print("\n==============================")
    print("   ADVANCED UNIT CONVERTER")
    print("==============================")
    print("1. Kilometer to Meter")
    print("2. Meter to Kilometer")
    print("3. Kilogram to Gram")
    print("4. Gram to Kilogram")
    print("5. Celsius to Fahrenheit")
    print("6. Fahrenheit to Celsius")
    print("7. Square Meter to Square Kilometer")
    print("8. Square Kilometer to Square Meter")
    print("9. KM/H to M/S")
    print("10. M/S to KM/H")
    print("11. USD to INR")
    print("12. INR to USD")
    print("13. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        km = float(input("Enter Kilometers: "))
        print("Result =", km * 1000, "Meters")

    elif choice == "2":
        m = float(input("Enter Meters: "))
        print("Result =", m / 1000, "Kilometers")

    elif choice == "3":
        kg = float(input("Enter Kilograms: "))
        print("Result =", kg * 1000, "Grams")

    elif choice == "4":
        g = float(input("Enter Grams: "))
        print("Result =", g / 1000, "Kilograms")

    elif choice == "5":
        c = float(input("Enter Celsius: "))
        fahrenheit = (c * 9/5) + 32
        print("Result =", fahrenheit, "Fahrenheit")

    elif choice == "6":
        f = float(input("Enter Fahrenheit: "))
        celsius = (f - 32) * 5/9
        print("Result =", round(celsius, 2), "Celsius")

    elif choice == "7":
        sqm = float(input("Enter Square Meters: "))
        print("Result =", sqm / 1000000, "Square Kilometers")

    elif choice == "8":
        sqkm = float(input("Enter Square Kilometers: "))
        print("Result =", sqkm * 1000000, "Square Meters")

    elif choice == "9":
        kmh = float(input("Enter Speed (KM/H): "))
        print("Result =", round(kmh / 3.6, 2), "M/S")

    elif choice == "10":
        ms = float(input("Enter Speed (M/S): "))
        print("Result =", round(ms * 3.6, 2), "KM/H")

    elif choice == "11":
        usd = float(input("Enter USD: "))
        print("Result =", round(usd * 85, 2), "INR")

    elif choice == "12":
        inr = float(input("Enter INR: "))
        print("Result =", round(inr / 85, 2), "USD")

    elif choice == "13":
        print("\nThank You For Using Advanced Unit Converter!")
        break

    else:
        print("\nInvalid Choice! Please Try Again.")
