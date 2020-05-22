"""
This module is for functions which perform measurements
"""

import numpy as np

def calculate_distance(rA, rB):
    """
    Calculate the distance between two points.

    Parameters
    ----------
    rA, rB : np.ndarray
        The coordinates of each point.

    Returns
    -------
    distance : float
        The distance between the two points.

    Examples
    --------
    >>> r1 = np.array([0.0, 0.0, 0.0])
    >>> r2 = np.array([0.0, 0.0, 1.0])
    >>> calculate_distance(r1, r2)
    1.0
    """

    if not (isinstance(rA, np.ndarray) and isinstance(rB, np.ndarray)):
        raise TypeError('rA and rB must be numpy arrays')

    d=(rA-rB)
    dist=np.linalg.norm(d)
    if dist == 0.0:
        raise Exception('Two atoms are located at the same point.')
    return dist

def calculate_angle(rA, rB, rC, degrees=False):
    """
    Calculate the angle between three points. 

    Parameters
    ----------
    rA, rB, rC : np.ndarray
        The coordinates of each point.

    degrees : bool
        Answer is given in radians by default, but can be given in degrees by setting degrees=True

    Returns
    -------
    angle : float
        The angle between the three points.

    Examples
    --------
    >>> r1 = np.array([1.0, 0.0, 0.0])
    >>> r2 = np.array([0.0, 1.0, 0.0])
    >>> r3 = np.array([0.0, 0.0, 1.0])
    >>> calculate_angle(r1, r2, r3, degrees=True)
    60.00000000000001
    """
    
    AB = rB - rA
    BC = rB - rC
    theta=np.arccos(np.dot(AB, BC)/(np.linalg.norm(AB)*np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta
