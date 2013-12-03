# -*- coding: utf-8 -*-
#
# posterior documentation build configuration file, created by
# sphinx-quickstart on Mon Feb  2 15:33:13 2009.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# The contents of this file are pickled, so don't put values in the namespace
# that aren't pickleable (module imports are okay, they're removed automatically).

import sys, os

sys.path.append(os.path.abspath('../'))

# General configuration
# ---------------------

extensions = ['sphinx.ext.autodoc']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'contents'
project = u'posterior'
copyright = u'2013, H W Tovetjärn'
version = '0.1'
release = '0.1.0pre'
exclude_trees = ['_build']
pygments_style = 'sphinx'


# Options for HTML output
# -----------------------

html_style = 'default.css'
html_static_path = ['_static']
htmlhelp_basename = 'posteriordoc'
