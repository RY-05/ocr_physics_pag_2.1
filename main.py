from matplotlib import pyplot as plt
import numpy as np

LENGTH_m = 2.58
DIAMETER_m = 0.38 * (10**-3)
GFS = 9.81

mass_kg = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
extension_mm = [0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 4.2, 4.5, 4.9, 5.0]

extension_m = []
for i in extension_mm:
    extension_m.append(i*(10**-3))

print(extension_mm)
print(extension_m)

strain_perc = []
for i in extension_m:
    strain_perc.append(100 * i / LENGTH_m)

strain = []
for i in strain_perc:
    strain.append(i / 100)

stress = []
for i in mass_kg:
    # stress equals force applied over surface area
    stress.append((i * GFS) / (np.pi * ((DIAMETER_m / 2) ** 2)))

# Young's modulus

vals = 0
for i in range(len(stress)):
    vals += stress[i] / strain[i]

young_mod = vals / len(stress)

print("Young's modulus is equal to " + str(young_mod) + " for a copper wire")


# stress-strain graph

plt.plot(strain_perc, stress)
plt.show()
