import matplotlib.pyplot as plt

Temperature = [17, 20, 24, 30, 32, 35, 40]
Precipitation = [300, 280, 200, 250, 240, 320, 330]

plt.xlabel("Temperature in °C")
plt.ylabel("Precipitation in cm")

plt.scatter(Temperature, Precipitation)

plt.show()

plt.xlabel("Temperature in °C")
plt.ylabel("Precipitation in cm")

plt.plot(Temperature, Precipitation)

plt.show()