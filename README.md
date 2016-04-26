# ipython-animated-array

[![PyPi version](https://img.shields.io/pypi/v/ipython-animated-array.svg)](https://pypi.python.org/pypi/ipython-animated-array)
[![PyPi downloads](https://img.shields.io/pypi/dm/ipython-animated-array.svg)](https://pypi.python.org/pypi/ipython-animated-array)
[![Build Status](https://travis-ci.org/airtoxin/ipython-animated-array.svg?branch=master)](https://travis-ci.org/airtoxin/ipython-animated-array)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/airtoxin/ipython-animated-array/master/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/airtoxin/ipython-animated-array.svg)](https://github.com/airtoxin/ipython-animated-array/stargazers)

render animated array on ipython-notebook (jupyter)

[![https://gyazo.com/170088a47a42390bb62460d913d3d4b3](https://i.gyazo.com/170088a47a42390bb62460d913d3d4b3.gif)](https://gyazo.com/170088a47a42390bb62460d913d3d4b3)

[![https://gyazo.com/5e0f68746ce124a0891749903b6c8a3c](https://i.gyazo.com/5e0f68746ce124a0891749903b6c8a3c.gif)](https://gyazo.com/5e0f68746ce124a0891749903b6c8a3c)


## Install

`pip install ipython-animated-array`


## Document

### _Module_ `ipython_animated_array`

#### _Class_ `ipython_animated_array.AnimateArray`

##### _constructor_ `__init__(viz_list, cmap='cool')`

__viz\_list__: list of animating array(1d or 2d).

__cmap='cool'__: [color map name](http://matplotlib.org/users/colormaps.html)

##### _AnimateArray Instance Method_ `animate_array.show(refresh=1000)`

Show animate array.

__refresh=1000__ `refresh animation duration(ms).`


## Example

open [example directory](https://github.com/airtoxin/ipython-animated-array/tree/master/example) via your ipython-notebook (or jupyter-notebook).

## License

MIT
