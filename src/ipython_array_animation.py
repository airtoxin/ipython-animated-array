#!/usr/bin/env python

from IPython.display import HTML, display
from jinja2 import Environment, FileSystemLoader

class AnimateArray(object):
    def __init__(self):
        super(AnimateArray, self).__init__()
        self.env = Environment(loader=FileSystemLoader('./template/', encoding='utf8'))

    def show(self):
        template = self.env.get_template('animatetag.tpl.html')
        display(HTML(template.render()))
