def TemperatureCalculator(celsius):
    F = (celsius * 9/5 + 32)
    print(f"your temperature in Fahrenheit{F}")

celsius=int(input("enter your temperature in celsius\n"))
TemperatureCalculator(celsius)
