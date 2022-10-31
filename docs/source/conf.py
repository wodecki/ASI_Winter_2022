# Configuration file for the Sphinx documentation builder.
from pathlib import Path
from sphinx.application import Sphinx

# -- Project information

project = 'ASI Winter 2022'
copyright = '2022, Andrzej Wodecki'
author = 'Graziella'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
here = Path(__file__).parent.absolute()

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {"collapse_navigation": False, "style_external_links": True}

# Removes, from all docs, the copyright footer.
html_show_copyright = False


# -- Options for EPUB output
epub_show_urls = 'footnote'

def setup(app):
    app.add_css_file("css/qb1-sphinx-rtd.css")
    # fix a bug with table wraps in Read the Docs Sphinx theme:
    # https://rackerlabs.github.io/docs-rackspace/tools/rtd-tables.html
    app.add_css_file("css/theme-overrides.css")