# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import glob
import os

project = 'Aprende Django'
description = 'Aprende Django'
copyright = 'Sergio Delgado Quintero'
author = 'Sergio Delgado Quintero'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'extra_roles',
    'sphinxext.opengraph',
    'sphinx.ext.autosectionlabel',
]

autosectionlabel_prefix_document = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'prolog.rst']

rst_prolog = open('prolog.rst').read()

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_show_sourcelink = False
html_css_files = ['css/custom.css']
STATIC_DIR = f'{html_static_path[0]}/'
html_css_files = [
    p.replace(STATIC_DIR, '') for p in glob.glob(os.path.join(STATIC_DIR, 'css/*.css'))
]
html_js_files = [p.replace(STATIC_DIR, '') for p in glob.glob(os.path.join(STATIC_DIR, 'js/*.js'))]
html_logo = '_static/img/aprendedjango-logo.svg'
html_theme_options = {
    'sidebar_hide_name': True,
}
html_favicon = 'favicon.png'
html_show_sourcelink = False
html_title = 'Aprende Django'

# -- Options for Open Graph -------------------------------------------------
# https://sphinxext-opengraph.readthedocs.io/en/latest/

ogp_site_url = 'https://aprendedjango.es/'
ogp_image = 'https://raw.githubusercontent.com/sdelquin/aprendedjango/main/_static/img/aprendedjango-logo.png'
