# Gallery-boilerplate

This boilerplate repository is to facilitate implementation of a sphinx gallery
plot.

## Installtion

### Clone the repository:

`git clone https://github.com/deepchecks/gallery-boilerplate.git`

### Create virtualenv

You will need python 3

`cd gallery-boilerplate && virtualenv venv`

### Install required packages

`pip install -r requirements.txt`

If you use other libraries to generate a plot you can add those to this file.
For example, since we are using `deepchecks` then install that using

`pip install deepchecks` then you will be able to plot using deepchecks.


## Writing plot

Edit `source/plot/plot_test.py`

## Generate plot

`make html`

## Copy files to webserver

If you have `nginx` or `apache` running with root `/var/www` then do

`cp -r build/html/* /var/www` and hit http://localhost/ you will see gallery thumbnail.