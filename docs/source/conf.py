import os
import sys
sys.path.insert(0, os.path.abspath('../'))

project = 'Interpolation-IITP'
copyright = '2025, Sofia Dorogova'
author = 'Sofia Dorogova'
release = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx_click',
    'myst_parser',  # Для поддержки Markdown в документации
]

templates_path = ['_templates']
exclude_patterns = []
html_theme = 'furo'  # Современная красивая тема Furo
html_static_path = ['_static', 'images']
intersphinx_mapping = {'python': ('https://docs.python.org/3/', None)}