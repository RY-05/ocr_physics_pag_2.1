from matplotlib import pyplot as plt
import numpy as np
from scipy import stats

LENGTH_m = 2.58
DIAMETER_m = 0.38 * (10**-3)
grav_field_str = 9.81

mass_kg = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
extension_mm = [0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 4.2, 4.5, 4.9, 5.0]

extension_m = []
for i in extension_mm:
    extension_m.append(i*(10**-3))

avg_ext_m = sum(extension_m) / len(extension_m)


strain = []
for i in extension_m:
    strain.append(i / LENGTH_m)

strain_perc = []
for i in strain:
    strain_perc.append(str(i * 100) + '%')


stress = []
for i in mass_kg:
    # stress equals force applied over surface area
    stress.append((i * grav_field_str) / (np.pi * ((DIAMETER_m / 2) ** 2)))


# Young's modulus
vals = 0
for i in range(len(stress)):
    vals += stress[i] / strain[i]

young_mod = vals / len(stress)

print(f"Young's modulus is equal to {young_mod}.")
print(f"Strain values are {strain_perc}.")
print(f"Stress values are {stress}.")

# stress-strain graph
slope, intercept, r, p, std_err = stats.linregress(strain, stress)


def myfunc(strain):
    return slope * strain + intercept


mymodel = list(map(myfunc, strain))

plt.scatter(strain, stress)
plt.plot(strain, mymodel)
plt.show()


# natural length uncertainty, half of a millimetre
length_unc_m = 0.0005


# area uncertainty, based on diameter, 1/20 of a millimetre
area_unc_m2 = 0.000005 ** 2


# extension uncertainty, half a millimetre
ext_unc_m = 0.0005


print(f"The uncertainty is {young_mod} plus / minus {(length_unc_m + area_unc_m2 + ext_unc_m)}.")
print(f"The percentage uncertainty is \
{((length_unc_m / LENGTH_m) + (area_unc_m2 / DIAMETER_m) + (ext_unc_m / avg_ext_m)) * 100}%.")


