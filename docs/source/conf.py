# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('../../'))

# Project information
project = 'personal-library-app'
copyright = '2026, 404NotFound-u'
author = '404NotFound-u'
release = '1.0.0'

# Extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]

napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True

# Theme
html_theme = 'sphinx_rtd_theme'

# Encoding
source_encoding = 'utf-8'

html_static_path = ['_static']
html_css_files = []
