"""
Module containing functions for visualization of molecules
"""

import numpy as np
import matplotlib.pyplot as plt
from .atom_data import *

def draw_molecule(coordinates, symbols, draw_bonds=None, save_location=None, dpi=300):
    """
    Draws a picture of a molecule using matplotlib.

    Parameters
    ----------
    coordinates : np.ndarray
        The coordinates of each atom in the molecule

    symbols : np.ndarray
        The string of each atom's elemental symbol

    draw_bonds : dictionary
        Dictionary of bond distances, with keys as the pair of corresponding atom indices

    save_location : str
        File path to save the outputted figure

    dpi : int
        Specify the dots per inch (resolution) of the outputted figure

    Returns
    -------
    ax : matplotlib.axes._subplots.Axes3DSubplot
        Matplotlib axes object of the molecule

    Examples
    --------
    >>> coordinates = np.array([[1.0, 2.0, 3.0], [3.0, 2.0, 1.0], [2.0, 3.0, 1.0]])
    >>> symbols = np.array(['C', 'C', 'C'])
    >>> draw_bonds = build_bond_list(coordinates, max_bond=3.0)
    >>> draw_molecule(coordinates, symbols, draw_bond, save_location='molecule.png')
    <matplotlib.axes._subplots.Axes3DSubplot object at 0x121f57550>
    """

    if len(coordinates) != len(symbols):
        raise Exception("Make sure coordinates and symbols reference the same number of atoms")

    # Create figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Get colors - based on atom name
    colors = []
    for atom in symbols:
        colors.append(atom_colors[atom])
    size = np.array(plt.rcParams['lines.markersize'] ** 2)*200/(len(coordinates))

    ax.scatter(coordinates[:,0], coordinates[:,1], coordinates[:,2], marker="o",
               edgecolors='k', facecolors=colors, alpha=1, s=size)

    # Draw bonds
    if draw_bonds:
        for atoms, bond_length in draw_bonds.items():
            atom1 = atoms[0]
            atom2 = atoms[1]

            ax.plot(coordinates[[atom1,atom2], 0], coordinates[[atom1,atom2], 1],
                    coordinates[[atom1,atom2], 2], color='k')

    # Save figure
    if save_location:
        plt.savefig(save_location, dpi=dpi, graph_min=0, graph_max=2)

    return ax


def bond_histogram(bond_list, save_location=None, dpi=300, graph_min=0, graph_max=2):
    """
    Draws a histogram of bond lengths based on a bond list (output from build_bond_list function)

    Parameters
    ----------
    bond_list : dictionary
        Dictionary of bond distances, with keys as the pair of corresponding atom indices

    save_location : str
        File path to save the outputted figure

    dpi : int
        Specify the dots per inch (resolution) of the outputted figure

    graph_min : float
        Lower bound of bond lengths shown in the outputted histogram

    graph_max : float
        Upper bound of bond lengths show in the outputted histogram

    Returns
    -------
    hist : matplotlib.axes._subplots.AxesSubplot
        Matplotlib axes object of the histogram

    Examples
    --------
    >>> coordinates = np.array([[1.0, 2.0, 3.0], [3.0, 2.0, 1.0], [2.0, 3.0, 1.0]])
    >>> bond_list = build_bond_list(coordinates, max_bond=3.0)
    >>> bond_histogram(bond_list, save_location='hist.png', graph_min=0.0, graph_max=4.0)
    <matplotlib.axes._subplots.AxesSubplot at 0x11c877a58>
    """

    lengths = []
    for atoms, bond_length in bond_list.items():
        lengths.append(bond_length)

    bins = np.linspace(graph_min, graph_max)
    fig = plt.figure()
    ax = fig.add_subplot(111)

    plt.xlabel('Bond Length (angstrom)')
    plt.ylabel('Number of Bonds')


    ax.hist(lengths, bins=bins)

    # Save figure
    if save_location:
        plt.savefig(save_location, dpi=dpi)

    return ax
