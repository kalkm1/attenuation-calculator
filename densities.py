def density(material):
    '''returns density of material in g/cm^3'''

    den = {'cdte': 5.85,
           'w': 19.3,
           'al': 2.7,
           'mo': 10.28,
           'ag': 10.49,
           'cu': 8.96,
           'v': 5.8,
           'zn': 7.13,
           'nb': 8.6,
           'pd': 11.9,
           'ge': 5.323,
           'cr': 7.19,
           'au': 19.32,
           'mg': 1.738,
           'mn': 7.43,
           'cdznte': 5.8,
           'pb': 11.34,
           'pt': 21.45,
           'perspex': 1.19,
           'air': 0.001225,
           'ag': 10.49
           }

    return den[material]
