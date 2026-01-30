print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")

choice = int(input("Enter your choice (1-4): "))
temperature = float(input("Enter the temperature value: "))

if choice == 1:
    result = (temperature * 9/5) + 32
    print(f"{temperature}°C = {result:.2f}°F")

elif choice == 2:
    result = (temperature - 32) * 5/9
    print(f"{temperature}°F = {result:.2f}°C")

elif choice == 3:
    result = temperature + 273.15
    print(f"{temperature}°C = {result:.2f}K")

elif choice == 4:
    result = temperature - 273.15
    print(f"{temperature}K = {result:.2f}°C")

else:
    print("Invalid choice! Please enter a number between 1 and 4.")
