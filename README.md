[![Code Health](https://landscape.io/github/mayou36/raredecay/master/landscape.svg?style=flat)](https://landscape.io/github/mayou36/raredecay/master)
[![Build Status](https://travis-ci.org/mayou36/raredecay.svg?branch=master)](https://travis-ci.org/mayou36/raredecay)
[![PyPI version](https://badge.fury.io/py/raredecay.svg)](https://badge.fury.io/py/raredecay)
[![Dependency Status](https://www.versioneye.com/user/projects/58273f1df09d22004f5914f9/badge.svg?style=flat-square)](https://www.versioneye.com/user/projects/58273f1df09d22004f5914f9)


# raredecay #

This package consists of several tools for the event selection of particle decays, mostly built on machine learning techniques.
It contains:

- a **data-container** holding data, weights, labels and more and implemented root-to-python data conversion as well as plots and KFold-data splitting
- **reweighting** tools from the hep_ml-repository wrapped in a KFolding structure and with metrics to evaluate the reweighting quality
- **classifier optimization** tools for hyper-parameters as well as feature selection involving a backward-elimination
- an **output handler** which makes it easy to add text as well as figures into your code and automatically save them to a file
- ... and more

## HowTo examples ##

To get an idea of the package, have a look at the howto notebooks:
[HTML version](http://mayou36.bitbucket.org/raredecay/howto/) or the 
[IPython Notebooks](https://github.com/mayou36/raredecay/tree/master/howto)

## Getting started right now ##

If you want it the easy, fast way, have a look at the
[Ready-to-use scripts](https://github.com/mayou36/raredecay/tree/master/scripts_readyToUse).  
All you need to do is to have a look at every "TODO" task and probably change them. Then you can run the script without the need of coding at all.

## Documentation and API ##

The API as well as the documentation:
[Documentation](http://mayou36.bitbucket.org/raredecay/docs/)

## Setup and installation ##

The package, in its current state, requires root_numpy as well as rootpy (and therefore a ROOT installation with python-bindings) to be installed on your system. If that is not the case, some functions won't work and you should install it with the --no-dependencies flag and install the other requirements by hand.

PIP package will may be uploaded in the future. Until then, use the following.
First install the very newest version of REP  
(the -U can be omitted, but is recommended to have the newest dependencies, on the other hand may crashes REPs reproducibility):
```
pip install -U https://github.com/yandex/rep/archive/stratifiedkfold.zip
```
Then, install the raredecay package via (assuming, *git* is installed. Otherwise, download the package as zip and install)
```
pip install raredecay
```
As it is a young package still under developement, it may receive regular updates and improvements and it is probably a good idea to regularly download the newest package.


[pandas.DataFrame]: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html
[LabeledDataStorage]: http://yandex.github.io/rep/data.html#module-rep.data.storage
[numpy.array]: http://docs.scipy.org/doc/numpy-1.10.1/user/basics.rec.html
[rootTree]: https://root.cern.ch/doc/v606/classTTree.html
