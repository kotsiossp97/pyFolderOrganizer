"""Document configuration."""
#
# PyModbus documentation build configuration file,
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# pylint: skip-file
import os
import sys

from pyFolderOrganizer import VERSION as pyFOrg_version


parent_dir = os.path.abspath(os.pardir)
sys.path.insert(0, parent_dir)
sys.path.append(os.path.join(parent_dir, "examples"))
github_doc_root = "https://github.com/kotsiossp97/pyFolderOrganizer/tree/master/doc/"

# -- General configuration ------------------------------------------------
extensions = ["sphinx.ext.autodoc", "sphinx_rtd_theme", "sphinx.ext.autosectionlabel"]
source_suffix = [".rst"]
master_doc = "index"
project = "pyFolderOrganizer"
copyright = "See license"
author = "Konstantinos Andreou"
version = pyFOrg_version
release = pyFOrg_version
language = "en"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
pygments_style = "sphinx"
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------
html_theme = "sphinx_rtd_theme"
html_static_path = []
html_sidebars = {
    "**": [
        "relations.html",  # needs "show_related": True theme option to display
        "searchbox.html",
    ]
}