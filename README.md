# attenuation-calculator

Simple script which calculates the linear attenuation coefficient, transmission probability and absorption probability of a photon
with a selected amount of energy (in keV), through a selected distance (in mm) of a certain material.

The attenuation coefficients of the materials as a function of energy are required in a .txt file - taken here from the NIST database.

Use: python att_calc.py material thickness [in mm] energy [in keV]
