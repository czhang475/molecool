"""
Module for functions associated with a molecule
"""

from .measure import calculate_distance

def build_bond_list(coordinates, max_bond=1.5, min_bond=0):
	"""
	Find the bonds in a molecule (set of coordinates) based on distance criteria.

    Parameters
    ----------
    coordinates : np.ndarray
        The coordinates of each atom in the molecule

    max_bond : float
        Maximum bond length

    min_bond : float
        Minimum bond length

    Returns
    -------
    bonds : dictionary
        Dictionary of bond distances, with keys as the pair of corresponding atom indices

    Examples
    --------
    >>> coordinates = np.array([1.0, 2.0, 3.0], [3.0, 2.0, 1.0], [2.0, 3.0, 1.0])
    >>> build_bond_list(coordinates, max_bond=3.0)
    {(0, 1): 2.8284271247461903, (0, 2): 2.449489742783178, (1, 2): 1.4142135623730951}
	"""
	if min_bond < 0:
		raise ValueError('Please make sure min_bond is set to a value greater than or equal to 0.')

	bonds = {}
	num_atoms = len(coordinates)
	for atom1 in range(num_atoms):
		for atom2 in range(atom1 + 1, num_atoms):
			distance = calculate_distance(coordinates[atom1], coordinates[atom2])
			if distance > min_bond and distance < max_bond:
				bonds[(atom1, atom2)] = distance

	return bonds
