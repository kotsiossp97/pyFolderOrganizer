# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


# -- Project information --
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


project = 'pyFolderOrganizer'
copyright = '2023, Konstantinos Andreou'
author = 'Konstantinos Andreou'

# -- General configuration --
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
]

# templates_path = ['_templates']
exclude_patterns = ['.venv', '_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output --
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Options for intersphinx extension --
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#configuration
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

# -- Options for todo extension --
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#configuration
todo_include_todos = True