# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import plotly.io as pio
from plotly.io._sg_scraper import plotly_sg_scraper

pio.renderers.default = 'sphinx_gallery_png'
# -- Project information -----------------------------------------------------

project = 'gallery-boilerplate'
copyright = '2022, Shiv S. Dayal'
author = 'Shiv S. Dayal'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # by itself sphinx_gallery is not able to work with jupyter notebooks
    # but nbsphinx extension is able to use some of it functionality to create
    # thumbnail galleries. Link to the doc - https://nbsphinx.readthedocs.io/en/0.8.7/subdir/gallery.html
    #
    'sphinx_gallery.load_style',
    #
    'sphinx_gallery.gen_gallery',
    'numpydoc',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx_copybutton',
]

imgmath_image_format = 'svg'
sphinx_gallery_conf = {
    "examples_dirs": [
        "plot",
    ],  # path to your example scripts
    "gallery_dirs": [
        "plot/examples",
    ], # path to where to save gallery generated output
    "image_scrapers": (
        plotly_sg_scraper,
    ),
    "pypandoc": True,
}
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']