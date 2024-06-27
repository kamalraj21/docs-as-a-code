import furo

project = 'doc-as-a-code'
copyright = '2024, Kamal Raj'
author = 'Kamal Raj'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [

]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

# Theme settings
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#4A4A4A",
        "color-brand-content": "#4A4A4A",
    },
    "dark_css_variables": {
        "color-background-primary": "#2E2E2E",
        "color-background-secondary": "#353535",
        "color-foreground-primary": "#E0E0E0",
        "color-foreground-secondary": "#C0C0C0",
        "color-brand-primary": "#B0B0B0",
        "color-brand-content": "#B0B0B0",
    },
}

# Versions configuration
# versions_branch_name = 'main'
# versions_base_url = 'https://github.com/kamalraj21/docs-as-a-code'
# versions = ['v1.0', 'v2.0', 'v3.0']
