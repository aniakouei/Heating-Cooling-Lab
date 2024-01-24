
#create a function that has two parameters
#create an if else statement to print an outcome if the actual temp is high, lower, or equal to desired temp
#have the user input the actual and desired temp
#use the function to print the correct statement

#create a function to convert celsius to target unit
#create if else statement depending on input to convert and print out statement for new unit
#print function with number for celsius and new unit chosen for conversion




def heating_cooling(actual_temp, desired_temp):
    if actual_temp < desired_temp:
        print("Run heat")
    elif actual_temp > desired_temp:
        print("Run A/C")
    else:
        print("Standby")


heating_cooling(70, 72)
heating_cooling(75, 70)
heating_cooling(68, 68)


user_actual_temp = float(input("Enter the actual temperature: "))
user_desired_temp = float(input("Enter the desired temperature: "))


heating_cooling(user_actual_temp, user_desired_temp)


def convert_temp(temp_celsius, target_unit):
    if target_unit == "C":
        print(f"The original temperature is {temp_celsius}°C")
    elif target_unit == "F":
        fahrenheit_temperature=(temp_celsius * 9/5) + 32
        print(f"{temp_celsius}°C is {fahrenheit_temperature}°F")
    elif target_unit == "K":
        Kelvin_temperature=temp_celsius + 273.15
        print(f"{temp_celsius}°C is {Kelvin_temperature}K")
    else:
        return "Invalid target unit"


print(convert_temp(temp_celsius=30, target_unit='K'))

