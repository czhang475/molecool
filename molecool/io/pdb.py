"""
Functions for manipulating .pdb files
"""

import os
import numpy as np

def open_pdb(f_loc):
    """
    This function reads in a .pdb file and returns the atom names and coordinates.

    Parameters
    ----------
    f_loc : str
        File path to .pdb file

    Returns
    -------
    symbols, coordinates : np.ndarray
        Numpy arrays of the atomic symbols (str) and coordinates (float) of all atoms in the file

    Example
    -------
    >>> symb, coords = open_pdb('water.pdb')
    >>> symb
    ['H', 'H', 'O']
    >>> coords
    array([[ 9.626,  6.787, 12.673],
           [ 9.626,  8.42 , 12.673],
           [10.203,  7.604, 12.673]])
    """
    with open(f_loc) as f:
        data = f.readlines()
    c = []
    sym = []
    for l in data:
        if 'ATOM' in l[0:6] or 'HETATM' in l[0:6]:
            sym.append(l[76:79].strip())
            try:
                c2 = [float(x) for x in l[30:55].split()]
            except not c2:
                print('Please make sure .pdb file is properly formatted.')
                break
            c.append(c2)
    coords = np.array(c)

    return sym, coords
