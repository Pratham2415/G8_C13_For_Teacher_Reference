import matplotlib.pyplot as plt

Temperature = [17, 20, 24, 30, 32, 35, 40]
Precipitation = [300, 200, 200, 250, 240, 320, 330]

plt.xlabel("Temperature in degree centigrades")
plt.ylabel("Precipitation in centimeters")

plt.scatter(Temperature, Precipitation)

plt.show()

plt.xlabel("Temperature in degree centigrades")
plt.ylabel("Precipitation in centimeters")

plt.plot(Temperature, Precipitation)

plt.show()