# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 09:59:52 2018

Description: calculate attenuation and absorption efficiencies

Use: python att_calc.py material thickness (mm) energy (keV)

Output: results output to terminal...

@author: kalkm1
"""

import numpy as np
import pandas as pd
import sys
from scipy.interpolate import interp1d
import warnings
warnings.simplefilter("ignore")


def _run(material, x, ephot):

    # material
    if material == 'CdTe' or material == 'cdte':

        density = 5.85 #g/cm^3
        df = pd.read_csv('CdTe_absorptioncoe_all.csv') #NIST XCOM

    elif material == 'W' or material == 'w':

        density = 19.3 # g/cm^3
        df = pd.read_csv('W_absorptioncoe_all.csv') #NIST XCOM

    elif material == 'Al' or material == 'al':

        density = 2.7 # g/cm^3
        df = pd.read_csv('Al_absorptioncoe_all.csv') #NIST XCOM

    elif material == 'Mo' or material == 'mo':

        density = 10.28 # g/cm^3
        df = pd.read_csv('Mo_absorptioncoe_all.csv') #NIST XCOM

    elif material == 'Ag' or material == 'ag':

        density = 10.49 # g/cm^3
        df = pd.read_csv('Ag_absorptioncoe_all.csv') #NIST XCOM

    elif material == 'Cu' or material == 'cu':

        density = 8.96 # g/cm^3
        df = pd.read_csv('Cu_absorptioncoe_all.csv') #NIST XCOM

    else:
        if material == 'V' or material == 'v':
            density = 5.8 # g/cm^3
            df = np.loadtxt('V_absorptioncoe_all.txt', skiprows=2) # NIST XCOM
            df[:,0] = df[:,0] * 1000 # convert MeV to keV
            df = pd.DataFrame(df,columns=['keV', 'coherent','incoherent','photoelectric effect','tot(cm2/g)'])

        if material == 'Zn' or material == 'zn':
            density = 7.13 # g/cm^3
            df = np.loadtxt('Zn_absorptioncoe_all.txt', skiprows=2) # NIST XCOM
            df[:,0] = df[:,0] * 1000 # convert MeV to keV
            df = pd.DataFrame(df,columns=['keV', 'coherent','incoherent','photoelectric effect','tot(cm2/g)'])

        if material == 'Nb' or material == 'nb':
            density = 8.6 # g/cm^3
            df = np.loadtxt('Nb_absorptioncoe_all.txt', skiprows=2) # NIST XCOM
            df[:,0] = df[:,0] * 1000 # convert MeV to keV
            df = pd.DataFrame(df,columns=['keV', 'coherent','incoherent','photoelectric effect','tot(cm2/g)'])

        if material == 'Pd' or material == 'pd':
            density = 11.9 # g/cm^3
            df = np.loadtxt('Pd_absorptioncoe_all.txt', skiprows=2) # NIST XCOM
            df[:,0] = df[:,0] * 1000 # convert MeV to keV
            df = pd.DataFrame(df,columns=['keV', 'coherent','incoherent','photoelectric effect','tot(cm2/g)'])

        if material == 'Ge' or material == 'ge':
            density = 5.323 # g/cm^3
            df = np.loadtxt('Ge_absorptioncoe_all.txt', skiprows=2) # NIST XCOM
            df[:,0] = df[:,0] * 1000 # convert MeV to keV
            df = pd.DataFrame(df,columns=['keV', 'coherent','incoherent','photoelectric effect','tot(cm2/g)'])

        if material == 'Cr' or material == 'cr':
            density = 7.19 # g/cm^3
            df = np.loadtxt('Cr_absorptioncoe_all.txt', skiprows=2) # NIST XCOM
            df[:,0] = df[:,0] * 1000 # convert MeV to keV
            df = pd.DataFrame(df,columns=['keV', 'coherent','incoherent','photoelectric effect','tot(cm2/g)'])

        if material == 'Au' or material == 'au':
            density = 19.32 # g/cm^3
            df = np.loadtxt('Au_absorptioncoe_all.txt', skiprows=2) # NIST XCOM
            df[:,0] = df[:,0] * 1000 # convert MeV to keV
            df = pd.DataFrame(df,columns=['keV', 'coherent','incoherent','photoelectric effect','tot(cm2/g)'])

        if material == 'Mg' or material == 'mg':
            density = 1.738 # g/cm^3
            df = np.loadtxt('Mg_absorptioncoe_all.txt', skiprows=2) # NIST XCOM
            df[:,0] = df[:,0] * 1000 # convert MeV to keV
            df = pd.DataFrame(df,columns=['keV', 'coherent','incoherent','photoelectric effect','tot(cm2/g)'])

        if material == 'Mn' or material == 'mn':
            density = 7.43 # g/cm^3
            df = np.loadtxt('Mn_absorptioncoe_all.txt', skiprows=2) # NIST XCOM
            df[:,0] = df[:,0] * 1000 # convert MeV to keV
            df = pd.DataFrame(df,columns=['keV', 'coherent','incoherent','photoelectric effect','tot(cm2/g)'])
            

    # thickness to cm
    ephot = float(ephot)
    x = float(x)
    x = x/10

    # get attenuation coefficient
    f = interp1d(np.log10(df['keV']),np.log10(df['tot(cm2/g)']*density))
    u = f(np.log10(ephot)) # need to use log(x) not x
    u = 10**u # convert log(y) to y

    # get info
    l_att = (1/u)*10 #mm
    att = (1 - np.exp(-u*x))*100
    u_tot = u

    # get absorption coefficient
    f = interp1d(np.log10(df['keV']),np.log10(df['photoelectric effect']*density))
    u = f(np.log10(ephot)) # need to use log(x) not x
    u = 10**u # convert log(y) to y

    # get info
    l_ab = (1/u)*10 #mm
    ab = (1 - np.exp(-u*x))*100

    print('material: '+str(material)+ ', thickness: '+str(x*10)+'mm, energy: '+str(ephot)+'keV')
    print('total linear attenuation coefficient (cm^-1): '+str(u_tot))
    print('total linear absorption coefficient (cm^-1): '+str(u))
    print('mean path length until attenuation (mm): '+str(l_att))
    print('mean path length until absorbed (mm): '+str(l_ab))
    print('attenuation (%): '+str(att))
    print('absorption (%): '+str(ab))
    print('transmission (%): '+str(100-att))


if __name__ == "__main__":
    material = (sys.argv[1])
    x = (sys.argv[2])
    ephot = (sys.argv[3])
    _run(material, x, ephot)
