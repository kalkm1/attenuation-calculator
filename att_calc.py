# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 09:59:52 2018

Description: calculate attenuation and absorption efficiencies through material

Use: python att_calc.py material thickness(mm) energy(keV)
Output: results output to terminal...

@author: kalkm1
"""
import numpy as np
import pandas as pd
import sys
from scipy.interpolate import interp1d
import densities as dens

def get_data(material):
    try:
        df = pd.read_csv('materials/%s_absorptioncoe_all.csv' % material)
    except FileNotFoundError:
        df = np.loadtxt('materials/%s_absorptioncoe_all.txt' % material, skiprows=2)
        df[:,0] = df[:,0] * 1000 # convert MeV to keV
        df = pd.DataFrame(df,columns=['keV', 'coherent','incoherent','photoelectric effect','tot(cm2/g)'])

    return df

def main(material, x, ephot):

    # get attenuation coefficients
    df = get_data(material)

    # get density of material
    density = dens.density(material)

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
    main(sys.argv[1].lower(), sys.argv[2], sys.argv[3])
