"""
molecool
A Python package for reading .pdb and .xyz files
"""

# Add imports here
from .FirstMod import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
