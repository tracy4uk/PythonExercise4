# a. Create a list of temperatures
temps = [25.2, 16.8, 31.4, 23.9, 28, 22.5, 19.6]

# b. Sort temps in ascending order
temps.sort()

# c. Create two new lists based on temperature criteria
cool_temps = temps[:temps.index(next(filter(lambda x: x > 20, temps)))]
warm_temps = temps[temps.index(next(filter(lambda x: x > 20, temps))):]

# d. Recombine lists using list arithmetic
temps_in_celsius = cool_temps + warm_temps

print(temps, cool_temps, warm_temps, temps_in_celsius)
