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


# -- Project information -----------------------------------------------------

project = "Disnake Guide"
copyright = "2021, Disnake Developers"
author = "Disnake Developers"

# The full version, including alpha/beta/rc tags
release = ""
version = ""

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.extlinks",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_panels",
    "sphinxext.opengraph",
    "notfound.extension",
]

notfound_urls_prefix = "/guide/"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_logo = html_favicon = "assets/disnake-logo-small.png"
html_title = project
html_short_title = project


html_theme = "furo"

html_theme_options = {
    "light_css_variables": {
        "tabs-color-label-active": "#376f9f",
        "tabs-color-label-inactive": "#254b6c84",
        "color-brand-primary": "#376f9f",
        "color-brand-content": "#376f9f",
        "color-background-primary": "#fdfdfd",
    },
    "dark_css_variables": {
        "color-brand-primary": "#f2c63c",
        "color-brand-content": "#ffd140",
        "color-background-primary": "#38383d",
        "color-background-secondary": "#38383d",
        "tabs-color-label-active": "#f2c63cdd",
        "tabs-color-label-inactive": "#51a6ed99",
    },
}

# panels_css_variables = {
#     "tabs-color-label-active": "#f2c63c",
#     # "tabs-color-label-inactive": "rgba(178, 206, 245, 0.62)",
#     # "tabs-color-overline": "rgb(207, 236, 238)",
#     # "tabs-color-underline": "rgb(207, 236, 238)",
#     # "tabs-size-label": "1rem",
# }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


html_js_files = ["js/external.js"]
html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
]


html_last_updated_fmt = ""
html_permalinks = True
html_use_index = True
# html_split_index = True
html_use_opensearch = "http://localhost:8005/"
html_show_sphinx = False
html_baseurl = "http://localhost:8005/"


### OGP Config
# this controls media embeds when linking on other websites
ogp_site_url = "https://onerandomusername.github.io/guide"
ogp_description_length = 0
ogp_site_name = "Disnake Guide"
ogp_image = (
    "https://raw.githubusercontent.com/DisnakeDev/guide/main/docs/assets/disnake-thin-banner.png"
)
ogp_image_alt = "Disnake Guide banner image"
ogp_use_first_image = False
ogp_type = "website"
ogp_custom_meta_tags = [
    '<meta property="og:description" content="A guide for disnake, a Discord API wrapper written for Python." />',
    # <!-- Primary Meta Tags -->
    f'<meta name="title" content="{ogp_site_name}" />',
    '<meta name="description" content="A guide for disnake, a Discord API wrapper written in Python." />',
    # <!-- Open Graph / Facebook -->
    '<meta property="og:type" content="website" />',
    f'<meta property="og:url" content="{ogp_site_url}" />',
    f'<meta property="og:title" content="{ogp_site_name}" />',
    '<meta property="og:description" content="A guide for disnake, a Discord API wrapper written in Python." />'
    f'<meta property="og:image" content="{ogp_image}" />,',
    # <!-- Twitter -->
    '<meta property="twitter:card" content="summary_large_image" />'
    f'<meta property="twitter:url" content="{ogp_site_url}" />'
    f'<meta property="twitter:title" content="{ogp_site_name}" />'
    '<meta property="twitter:description" content="A guide for disnake, a Discord API wrapper written in Python." />'
    f'<meta property="twitter:image" content="{ogp_image}" />',
]
# -- MyST parser --------------------------------------------------------------
# This allows us to use markdown files to create sphinx documentation
# extensions
myst_enable_extensions = [
    "colon_fence",
    "replacements",
    "substitution",
    "html_image",
]

myst_url_schemes = ["http", "https", "mailto"]
# -- Intersphinx Config ------------------------------------------------------
# provides mapping capabilites between disnake and the guide
# config here is what inventories to use and their names
intersphinx_cache_limit = 5
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", "https://docs.python.org/3/objects.inv"),
    "disnake": (
        "https://docs.disnake.dev/en/latest",
        "https://docs.disnake.dev/en/latest/objects.inv",
    ),
}

# -- Extlinks ----------------------------------------------------------------
# allow linking to other locations by using a role
extlinks = {
    "disnake": ("https://docs.disnake.dev/en/latest%s", None),
    "pypi": ("https://pypi.org/project/%s", "%s"),
    "disdocs": ("https://discord.com/developers/docs%s", "%s"),
    "dpydocs": ("https://discordpy.readthedocs.io/en/master", None),
}


pygments_style = "default"
pygments_dark_style = "monokai"
