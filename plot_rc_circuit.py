import matplotlib.pyplot as plt

# Initialize lists to store time and voltage values
time = []
voltage = []

# Open and read the ngspice output file
with open("rc_output.log", "r") as file:
    for line in file:
        # Split each line and try to extract time and voltage if they are numeric
        parts = line.split()
        
        # Check if there are at least 2 parts and that both can be converted to floats
        if len(parts) >= 2:
            try:
                # Convert the first two elements to floats (assuming time and voltage)
                time_val = float(parts[0])
                voltage_val = float(parts[1])
                
                # Append to lists if conversion is successful
                time.append(time_val)
                voltage.append(voltage_val)
                
            except ValueError:
                # Skip lines that cannot be converted to float
                continue

# Plot the data using matplotlib if data was extracted
if time and voltage:
    plt.plot(time, voltage, label="V(out)")
    plt.xlabel("Time (s)")
    plt.ylabel("Voltage (V)")
    plt.title("RC Circuit Transient Response")
    plt.legend()
    plt.grid()
    plt.show()
else:
    print("No valid data found in rc_output.log.")