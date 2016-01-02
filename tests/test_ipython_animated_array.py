#!/usr/bin/env python

from ipython_animated_array import AnimateArray
from IPython.core.display import HTML
import numpy as np

def test_constructor():
    viz_list = [np.array([1,2,3])]
    aa = AnimateArray(viz_list)
    assert aa.cmap == 'cool'
    for html in aa.htmls:
        assert isinstance(html, str)
