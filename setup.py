#!/usr/bin/env python

import sys
from setuptools import setup, Extension, find_packages


VERSION = "0.4"
CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Science/Research",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
    "Programming Language :: C",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    "Topic :: Scientific/Engineering :: Bio-Informatics",
    "Topic :: Scientific/Engineering :: Chemistry",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: POSIX",
    "Operating System :: Unix",
    "Operating System :: MacOS",
]


# from MDAnalysis setup.py (http://www.mdanalysis.org/)
class NumpyExtension(Extension, object):
    """Derived class to cleanly handle setup-time (numpy) dependencies.
    """
    # The only setup-time numpy dependency comes when setting up its
    #  include dir.
    # The actual numpy import and call can be delayed until after pip
    #  has figured it must install numpy.
    # This is accomplished by passing the get_numpy_include function
    #  as one of the include_dirs. This derived Extension class takes
    #  care of calling it when needed.
    def __init__(self, *args, **kwargs):
        self._np_include_dirs = []
        super(NumpyExtension, self).__init__(*args, **kwargs)

    @property
    def include_dirs(self):
        if not self._np_include_dirs:
            for item in self._np_include_dir_args:
                try:
                    self._np_include_dirs.append(item())  # The numpy callable
                except TypeError:
                    self._np_include_dirs.append(item)
        return self._np_include_dirs

    @include_dirs.setter
    def include_dirs(self, val):
        self._np_include_dir_args = val


# from MDAnalysis setup.py (http://www.mdanalysis.org/)
def get_numpy_include():
    try:
        # Obtain the numpy include directory. This logic works across numpy
        # versions.
        # setuptools forgets to unset numpy's setup flag and we get a crippled
        # version of it unless we do it ourselves.
        try:
            import __builtin__  # py2
            __builtin__.__NUMPY_SETUP__ = False
        except:
            import builtins  # py3
            builtins.__NUMPY_SETUP__ = False
        import numpy as np
    except ImportError as e:
        print(e)
        print('*** package "numpy" not found ***')
        print('Simpletraj requires a version of NumPy, even for setup.')
        print('Please get it from http://numpy.scipy.org/ or install it through '
              'your package manager.')
        sys.exit(-1)
    try:
        numpy_include = np.get_include()
    except AttributeError:
        numpy_include = np.get_numpy_include()
    return numpy_include


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
        author_email = "alexander.rose@weirdbyte.de",
        description = "Lightweight coordinate-only trajectory reader based on code from GROMACS, MDAnalysis, VMD.",
        version = VERSION,
        classifiers = CLASSIFIERS,
        license = "GPL2",
        url = "https://github.com/arose/simpletraj",
        zip_safe = False,
        packages = find_packages(),
        ext_modules = [
            NumpyExtension(
                "simpletraj/xdrfile._libxdrfile2",
                sources = [
                    "simpletraj/xdrfile/libxdrfile2_wrap.c",
                    "simpletraj/xdrfile/xdrfile.c",
                    "simpletraj/xdrfile/xdrfile_trr.c",
                    "simpletraj/xdrfile/xdrfile_xtc.c"
                ],
                include_dirs = [ get_numpy_include ],
                define_macros = largefile_macros
            ),
            NumpyExtension(
                "simpletraj/dcd._dcdmodule",
                sources = [
                    "simpletraj/dcd/dcd.c"
                ],
                include_dirs = [ get_numpy_include, "simpletraj/dcd/include" ],
            ),
        ],
        requires = [ "numpy" ],
        setup_requires = [ "numpy" ],
        install_requires = [ "numpy" ],
        extras_require = {
            "netcdf": [ "netCDF4" ]
        }
    )
