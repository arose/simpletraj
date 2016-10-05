
Lightweight coordinate-only trajectory reader based on code from [GROMACS](http://www.gromacs.org/), [MDAnalysis](http://www.mdanalysis.org/) and [VMD](http://www.ks.uiuc.edu/Research/vmd/).

Used for coordinate retrieval in [MDSrv](https://github.com/arose/mdsrv) and [nglview](https://github.com/arose/nglview).

Should work with Python 2 and 3. If you experience problems, please file an [issue](https://github.com/arose/simpletraj/issues).


Installation
============

From PyPI:

    pip install simpletraj


netCDF4
-------

For reading `.netcdf` trajectory files the `netCDF4` package is needed. As installing it can prove difficult, it is not a required package and must be installed separately.

If you use `conda` as your Python package manager:

    conda install netcdf4


To install the NetCDF libraries and its Python package on debian/ubuntu:

    sudo apt-get install libhdf5-serial-dev libnetcdf-dev
    pip install netCDF4


In case you get "ValueError: did not find HDF5 headers" try:

    sudo su
    find / -name "libhdf5*.so*"
    # use what the above 'find' suggests to set 'HDF5_DIR'
    export HDF5_DIR=/usr/lib/i386-linux-gnu/hdf5/serial/
    pip install netCDF4


Changelog
=========

Version 0.4
-----------

* FIX: Python 3 compatibility (iter/iteritems)


Version 0.3
-----------

* FIX: DCD Python 2 compatibility


Version 0.2
-----------

* ADD: package ready for PyPI
* CODE: Python 3 compatibility
* CODE: handle errors during offsets file reading/writing


Version 0.1
-----------

initial version (no release)


License
=======

Generally GPL2, see the LICENSE file for details.
