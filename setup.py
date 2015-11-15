#!/usr/bin/env python

"""
Setup script for trajectory file reading modules.

A working installation of NumPy <http://numpy.scipy.org> is required.

For a basic installation just type the command::

    python setup.py build_ext --inplace

Based on setup.py from MDAnalysis:

    http://www.mdanalysis.org/
"""


from setuptools import setup, Extension

import numpy
try:
    numpy_include = numpy.get_include()
except AttributeError:
    numpy_include = numpy.get_numpy_include()
include_dirs = [ numpy_include ]


# Needed for large-file seeking under 32bit systems (for xtc/trr indexing and access).
largefile_macros = [
    ( "_LARGEFILE_SOURCE", None ),
    ( "_LARGEFILE64_SOURCE", None ),
    ( "_FILE_OFFSET_BITS","64" )
]

if __name__ == '__main__':
    setup(
        name = "simpletraj",
        author = "Alexander S. Rose",
        description = "Simple coordinate-only trajectory reader based on code from GROMACS, MDAnalysis, VMD.",
        version = "0.1",
        license = "GPL2",
        url = "https://github.com/arose/simpletraj",
        packages = [ "simpletraj", "simpletraj.xdrfile", "simpletraj.dcd" ],
        ext_modules = [
            Extension(
                "simpletraj/xdrfile._libxdrfile2",
                sources = [
                    "simpletraj/xdrfile/libxdrfile2_wrap.c",
                    "simpletraj/xdrfile/xdrfile.c",
                    "simpletraj/xdrfile/xdrfile_trr.c",
                    "simpletraj/xdrfile/xdrfile_xtc.c"
                ],
                include_dirs = include_dirs,
                define_macros = largefile_macros
            ),
            Extension(
                "simpletraj/dcd._dcdmodule",
                sources = [
                    "simpletraj/dcd/dcd.c"
                ],
                include_dirs = include_dirs + [ "simpletraj/dcd/include" ],
            ),
        ],
        setup_requires = [ "numpy" ],
        install_requires = [ "numpy", "netCDF4" ],
    )
