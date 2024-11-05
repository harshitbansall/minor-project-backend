import matplotlib.pyplot as plt

time = []
voltage = []
with open("rc_output.log", "r") as file:
    for line in file:
        parts = line.split()

        if len(parts) >= 2:
            try:
                time_val = float(parts[0])
                voltage_val = float(parts[1])

                time.append(time_val)
                voltage.append(voltage_val)

            except ValueError:
                continue

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
