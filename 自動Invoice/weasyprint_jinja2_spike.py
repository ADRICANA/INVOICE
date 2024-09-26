#!venv/bin/python

# Script requires:
# - virtualenv in venv dir (virtualenv venv)
# - XQuartz-2.7.5 (MacOSX only, installed separately from https://xquartz.macosforge.org/landing/)
# - cairo pango gdk-pixbuf libxmllibxslt libffi (brew install cairo pango gdk-pixbuf libxmllibxslt libffi)
# - WeasyPrint (pip install WeasyPrint)
# - Jinja2 (pip install Jinja2)

from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader

# load template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('invoice.html')

# render template
rendered = template.render(messages=['Hello','World'])

# write to PDF
HTML(string=rendered).write_pdf('weasyprint_jinja2_spike_output.pdf')