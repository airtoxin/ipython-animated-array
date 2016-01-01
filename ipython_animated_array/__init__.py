#!/usr/bin/env python

from os import path
from IPython.display import HTML, display
from jinja2 import Environment, PackageLoader
from vizarray import vizarray

class AnimateArray(object):
    def __init__(self, viz_list, cmap='cool'):
        super(AnimateArray, self).__init__()
        self.env = Environment(loader=PackageLoader('ipython_animated_array', 'template', encoding='utf8'))
        self.cmap = cmap
        self.htmls = self.get_htmls(viz_list)

    def get_htmls(self, viz_list):
        return [
            vizarray(viz, cmap=self.cmap)._repr_html_()
            for viz in viz_list
        ]

    def show(self):
        template = self.env.get_template('animatetag.tpl.html')
        display(HTML(template.render({
            'htmls': self.htmls,
            'id': id(self.htmls)
        })))
