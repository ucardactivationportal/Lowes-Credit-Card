# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here.
# Example: sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Activate Lowe’s Card Online'
copyright = '2025, Lowe’s'
author = 'Lowe’s Credit Services'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- HTML output settings ----------------------------------------------------

# Title shown in the browser tab and top of HTML pages
html_title = "Why You Should Activate Your Lowe’s Card Online Instead of by Phone"

# Optional short title (e.g., for nav bar)
html_short_title = "Activate Lowe’s Card Online"

# Favicon (place favicon.ico in the root or _static folder)
html_favicon = 'favicon.ico'

# Uncomment and choose a theme (default is 'alabaster')
# html_theme = 'sphinx_rtd_theme'
# html_theme = 'alabaster'
# html_theme = 'furo'

# Hide "View page source" from top bar
html_show_sourcelink = False

# Allow raw HTML blocks in .rst files
html_allow_unsafe = True
raw_enabled = True

# Theme customization options
html_theme_options = {
    'show_powered_by': False,
}

# Paths to templates and static files
templates_path = ['_templates']
# html_static_path = ['_static']  # Uncomment if you have custom CSS, JS, or images

# Patterns to ignore when looking for source files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
