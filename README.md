# attenuation-calculator

Simple script which calculates the linear attenuation coefficient, transmission probability and absorption probability of a photon
with a selected amount of energy (in keV), through a selected distance (in mm) of a certain material up to a photon energy of 1 MeV.

The attenuation coefficients of the materials as a function of energy are required in a .txt file - taken from the NIST XCOM database. The density must be added to the function in densities.py.

Use from cmd line: python att_calc.py material thickness [in mm] energy [in keV]
