
# create a function to convert Celsius to Fahrenheit
def convert_temperature(temperature):
    return temperature * 9/5 + 32

# create a function that takes a temperature in Fahrenheit and a windspeed and returns the wind chill
def calculate_windchill(T,V):
    return 35.74 + 0.6215*T - 35.75*(V**0.16) + 0.4275*T*(V**0.16)

#Wind Chill (ºF) = 35.74 + 0.6215T - 35.75(V0.16) + 0.4275T(V0.16)
# Ask the user for the temperature
temperature = float(input('What is the temperature?: '))

# Ask the user for Celsius or Fahrenheit
choice = input('Are you using Celcius or Fahrenheit  C/F ? ').upper()

# If the temperature is in Celsius call the function to convert to Fahrenheit and store the result
if choice == 'C':
    temperature = convert_temperature(temperature)
# Use a for loop to loop over wind speeds from 5 to 60 in increments of 5
for windspeed in range(5,61,5):

# Print each windchill as shown in the instructions by calling the windchill function with the given temperature and windspeed
    print(f'At temperature {temperature}, and wind speed {windspeed}, the windchill is: {calculate_windchill(temperature,windspeed):.2f}')
    
