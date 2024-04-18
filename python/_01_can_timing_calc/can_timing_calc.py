import sys

# Define the first number and the target result
bus_clock = 42e6 # Hz
can_bus_baudrate = 240_000 # Bit per second

# Define the ranges for the second and third numbers
prescalar = range(1, 1024+1)
time_quanta = range(8, 25+1)

# Initialize variables to keep track of the closest values
closest_error = sys.float_info.max
closest_prescalar = 0
closest_time_quanta = 0

# Loop through all possible combinations of second and third numbers
for second in prescalar:
    for third in time_quanta:
        result = second * third

        # Calculate the error
        error = abs(bus_clock / result - can_bus_baudrate)

        # Update the closest values if the current error is smaller
        if error < closest_error:
            closest_error = error
            closest_prescalar = second
            closest_time_quanta = third

# Output the closest values found
print(f"The closest values for the prescalar is {closest_prescalar} and for the time quanta is {closest_time_quanta}.")
print(f"{bus_clock} / ({closest_prescalar} * {closest_time_quanta}) = {bus_clock /(closest_prescalar*closest_time_quanta)} (target = {can_bus_baudrate})")