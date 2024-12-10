# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MyCProject'
copyright = '2024, Jimmy Situ'
author = 'Jimmy Situ'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'breathe',
]

# Breathe configuration
breathe_projects = {
    "MyCProject": "../../doxygen/xml"
}

breathe_projects_source = {
    "MyCProject" : ( "../../src", ["main.c", "math_operation.c"] )
}

breathe_default_project = "MyCProject"

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
