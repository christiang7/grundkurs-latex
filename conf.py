import os
import sys

sys.path.append(os.path.abspath('_exts'))

extensions = [
    # 'matplotlib.sphinxext.mathmpl',
    # 'matplotlib.sphinxext.only_directives',
    # 'matplotlib.sphinxext.plot_directive',
    # "sphinxcontrib.blockdiag",
    # "sphinxcontrib.seqdiag",
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.imgmath',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
]

# 'ipython_console_highlighting',
# 'inheritance_diagram',
# 'numpydoc', 'lily',

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'Grundkurs LaTeX'
htmlhelp_basename = 'Grundkurs LaTeX'
html_short_title = 'Grundkurs LaTeX'

version = '0.1.0c'
release = '0.1.0c'
copyright = '2015-2018, Bernhard Grotz'
language = 'de'
spelling_lang = 'de_DE'
pygments_style = 'sphinx'
html_theme = 'sphinxdoc'

html_favicon = "favicon.ico"
html_logo = 'logo.png'
latex_logo = 'logo_print.png'

html_static_path = ['_static']
html_last_updated_fmt = '%d.%m.%Y'
html_additional_pages = {'home': 'home.html'}
html_domain_indices = False
html_use_index = True

html_show_sourcelink = True
html_show_sphinx = False
html_show_copyright = False
html_search_language = 'en'
html_search_options = {'type': 'default'}

today_fmt = '%d.%m.%Y'
exclude_patterns = [
    "notes.rst",
    "*/notes.rst",
    "**/notes.rst",
    "todos.rst",
    "README.rst"
]


# latex_logo = "logo.png"

latex_preamble = r'''
\usepackage[T1]{fontenc}
\usepackage[version=3]{mhchem}
\usepackage{amsmath, units, cancel,soul}
\usepackage{amsfonts, mathrsfs, amssymb, xcolor}
\usepackage{nicefrac,marvosym,mathtools,wasysym,textcomp,gensymb}
\usepackage{fancybox,shadow}
\usepackage{multicol}
\setcounter{secnumdepth}{-1}
\setlength{\headheight}{15pt}
\setcounter{tocdepth}{2}
\sloppy
\clubpenalty  = 10000 % Disable single lines at the start of a page (Schusterjungen)
\widowpenalty = 10000 % Disable single lines at the end   of a page (Hurenkinder)
\displaywidowpenalty = 10000
\usepackage{hyperref,url}
\hypersetup{
pdftitle={Grundkurs LaTeX},
pdfsubject={Eine Einführung in das Textsatzungssystem LaTeX},
pdfauthor={Bernhard Grotz},
pdfkeywords={LaTeX} {Textsatzung} {Tutorial} {Einführung} {Howto},
}
'''

imgmath_latex_preamble = latex_preamble

latex_elements = {
    "preamble": latex_preamble,
    "babel": "\\usepackage[ngerman]{babel}",
    "classoptions": 'oneside,openany,',
    "papersize": 'a4paper,',
    "pointsize": '12pt',
    "fontpkg": '',
    "fncychap": ''
}

latex_domain_indices = False


# latex_show_pagerefs    = True


latex_documents = [
   ('index', 'grundkurs-latex.tex', 'Grundkurs LaTeX',
   'Bernhard Grotz', 'manual'),
]

intersphinx_mapping = {
    'gw':('http://grund-wissen.de/', None),
    'gwm':('http://grund-wissen.de/mathematik/', None),
    'gwp':('http://grund-wissen.de/physik/', None),
    'gwe':('http://grund-wissen.de/elektronik/', None),
    'gwl': ('http://grund-wissen.de/linux/', None),
    'gwic':('http://grund-wissen.de/informatik/c/', None),
    'gwip':('http://grund-wissen.de/informatik/python/', None),
}

