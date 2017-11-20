# bright
[![Licence](http://img.shields.io/badge/license-GPLv3-blue.svg?style=flat)](http://www.gnu.org/licenses/gpl-3.0.html)
[![arXiv](http://img.shields.io/badge/arXiv-1708.07462-blue.svg?style=flat)](http://arxiv.org/abs/1708.07462)

### Pipeline for halo photometry

Authors: Benjamin Pope, Tim White

This repo links to the main halo photometry pipeline [halophot](github.com/hvidy/), maintained by Tim White. 

Using the notebooks in this repo, you can implement a halo + k2sc pipeline:

- get_names.ipynb - the MAST listings just give you EPICs; this will find common names for the stars. (This is of somewhat general, if minor, use.)

- make_scripts.ipynb - this will tell you the commands to run halo and k2sc. You should have a directory structure with folders raw/, reduced/, reduced/dummy/ and reduced/final.

- inspect.ipynb - just download one MAST lightcurve and inspect it to determine where to put splits. 

- halo_copy_c14.py - copy the data from halo outputs into the MAST lightcurves. A bit of a laborious workaround.