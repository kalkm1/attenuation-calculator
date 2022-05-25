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

def inter_coeffs(en, coeffs, den, ephot):
    f = interp1d(np.log10(en),np.log10(coeffs*den))
    u = f(np.log10(ephot)) # need to use log(x) not x
    u = 10**u # convert log(y) to y
    return u

def get_l(u, x):
    l = (1/u)*10 # to mm
    att = (1 - np.exp(-u*x))*100
    return l, att

def main(material, x, ephot):

    # get attenuation coefficients
    df = get_data(material)

    # get density of material
    density = dens.density(material)

    # interpolate coefficients
    u_tot = inter_coeffs(df['keV'], df['tot(cm2/g)'], density, ephot)

    # get mean path length
    l_att, att = get_l(u_tot, x/10)

    # interpolate coefficients
    u_pe = inter_coeffs(df['keV'], df['photoelectric effect'], density, ephot)

    # get mean path length
    l_ab, ab = get_l(u_pe, x/10)

    print('material: '+str(material)+ ', thickness: '+str(x)+'mm, energy: '+str(ephot)+'keV')
    print('total linear attenuation coefficient (cm^-1): '+str(u_tot))
    print('total linear absorption coefficient (cm^-1): '+str(u_pe))
    print('mean path length until attenuation (mm): '+str(l_att))
    print('mean path length until absorbed (mm): '+str(l_ab))
    print('attenuation (%): '+str(att))
    print('absorption (%): '+str(ab))
    print('transmission (%): '+str(100-att))

if __name__ == "__main__":
    main(sys.argv[1].lower(), float(sys.argv[2]), float(sys.argv[3]))
