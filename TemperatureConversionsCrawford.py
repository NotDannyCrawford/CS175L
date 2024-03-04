def main():
    controlLoop()

def convertToKelvin(fahrenheit):
    kelvin = ((fahrenheit - 32) * (5/9) + 273.15)
    return kelvin

def convertToCentigrade(fahrenheit):
    centigrade = (fahrenheit - 32) * (5/9)
    return centigrade

def doConversion():
    fahrenheit = getFahrenheit()
    kelvin = convertToKelvin(fahrenheit)
    centigrade = convertToCentigrade(fahrenheit)
    print("Fahrenheit: " + str(fahrenheit) + ", Kelvin: " + str(kelvin) + ", Centigrade: " + str(centigrade))

def repeat():
    b = int(input("How many conversions would you like to do this time? "))
    for x in range(b):
        doConversion()

def controlLoop():
    a = input("Do you want to do some conversions(Yes or No)? ").lower()
    if a == "yes":
        repeat()

def getFahrenheit():
    while True:
        try:
            fahrenheit = float(input('Enter Fahrenheit temperature (must be -50 to 130): '))
            if fahrenheit >= -50 and fahrenheit <= 130:
                return fahrenheit
            else:
                print('Please re-enter. Temperature must be between -50 and 130 Fahrenheit.')
        except ValueError:
            print('Invalid input. Please enter a valid number.')
    

# This code will call the 'main' function if the entire program was run.
if __name__ == '__main__':
    main()
