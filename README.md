# attenuation-calculator

Summary:

Simple script which calculates the linear attenuation coefficient, transmission probability and absorption probability of a photon
with a selected amount of energy (in keV), through a selected distance (in mm) of a certain material up to a photon energy of 1 MeV.


Materials:

The attenuation coefficients of the materials as a function of energy are in a .txt file in the materials directory - taken from the NIST XCOM database. New .txt files for more materials can easily be added.

The density for each new material must be added to the function in densities.py.


Use from cmd line, ignoring [square brackets]:

python att_calc.py material [not case-sensitive] thickness [mm] energy [keV]
