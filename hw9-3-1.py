#author CJP 1/18/2022

def temperature():
    
    while True:
        
        try: 
            temperature = float(input("Enter temperature: "))
            x = input("In fahrenheit or celcius (f/C)?").upper()
            if x == "c":
                ans = (temperature - 32) * (5 / 9)
                print("The temperature is {0} degrees celcius.".format(ans))
            elif x == "f":
                ans = temperature / 5 * 9 + 32
                print("The temperature is {0} degrees fahrenheit.".format(ans))
            else:
                print("Invalid, use f or c.")
        except ValueError:
            print("Invalid, use a number for the temperature")

temperature()