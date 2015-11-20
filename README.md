

Lightweight coordinate-only trajectory reader based on code from [GROMACS](http://www.gromacs.org/), [MDAnalysis](http://www.mdanalysis.org/) and [VMD](http://www.ks.uiuc.edu/Research/vmd/).

Used for coordinate retrieval in [MDSrv](https://github.com/arose/mdsrv) and [nglview](https://github.com/arose/nglview).


Installation
============


Some libraries need to be installed. First, make sure you have the Python development files installed, e.g.

    sudo apt-get install python-dev python-numpy


Then install the NetCDF libraries and its Python package

    sudo apt-get install libhdf5-serial-dev libnetcdf-dev
    sudo pip install netCDF4


In case you get "ValueError: did not find HDF5 headers" try:

    sudo su
    find / -name "libhdf5*.so*"
    # use what the above 'find' suggests to set 'HDF5_DIR'
    export HDF5_DIR=/usr/lib/i386-linux-gnu/hdf5/serial/
    pip install netCDF4


Finally install simpletraj itself:

    sudo python setup.py install


Changelog
=========

Version 0.2dev
--------------

* WIP: preparing packaging
* CODE: Python 3 compatibility
* CODE: handle errors during offsets file reading/writing


Version 0.1
-----------

initial version (no release)


License
=======

Generally GPL2, see the LICENSE file for details.
