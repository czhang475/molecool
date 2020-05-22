"""
Files for manipulating .xyz files
"""

import os
import numpy as np

def open_xyz(file_location):
    """
    Opens an .xyz file and returns symbols and coordinates.

    Parameters
    ----------
    file_location : str
        File path to .xyz file

    Returns
    -------
    symbols, coordinates : np.ndarray
        Numpy arrays of the atomic symbols (str) and coordinates (float) of all atoms in the file

    Example
    -------
    >>> symb, coords = open_xyz('water.xyz')
    >>> symb
    ['H', 'H', 'O']
    >>> coords
    array([[ 9.626,  6.787, 12.673],
           [ 9.626,  8.42 , 12.673],
           [10.203,  7.604, 12.673]])
    """

    xyz_file = np.genfromtxt(fname=file_location, skip_header=2, dtype='unicode')
    symbols = xyz_file[:,0]
    coords = (xyz_file[:,1:])
    coords = coords.astype(np.float)
    return symbols, coords

def write_xyz(file_location, symbols, coordinates):
    """
    Write an .xyz file given a file location, symbols, and coordinates.

    Parameters
    ----------
    file_location : str
        Path to save the generated .xyz file

    symbols : np.ndarray
        Numpy array of strings of each atom symbol

    coordinates : np.ndarray
        Numpy array of the coordinates of each atom

    Returns
    -------
    

    Example
    -------
    >>> symb = np.array(['H', 'H', 'O'])
    >>> coords = np.array([[ 9.626,  6.787, 12.673], [ 9.626,  8.42 , 12.673], [10.203,  7.604, 12.673]])
    >>> write_xyz('water.xyz', symb, coords)
    """
    
    num_atoms = len(symbols)
    with open(file_location, 'w+') as f:
        f.write('{}\n'.format(num_atoms))
        f.write('XYZ file\n')
        for i in range(num_atoms):
            f.write('{}\t{}\t{}\t{}\n'.format(symbols[i], coordinates[i,0], coordinates[i,1], coordinates[i,2]))
