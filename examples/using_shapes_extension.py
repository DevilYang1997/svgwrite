#!/usr/bin/env python
#coding:utf-8
# Author:  ya-induhvidual
# Purpose: svg shapes-extension example
# Modified
# Copyright (C) 2019, Christof Hanke
# License: MIT License
from __future__ import unicode_literals
import math

import svgwrite
from svgwrite.extensions.shapes import *

def main(name):
    """
    Some examples how to use the shpaes extension
    """
    dwg = svgwrite.Drawing(name + ".svg", (1000, 1000), debug=True)
    style = { "fill" : "none", "stroke" : "black", "stroke-width" : "1"}
    # create a list of points lying on the corners of an octagon
    octagon = list(ngon(8, 10))
    dwg.add(dwg.polygon(octagon, **style))
    # translate it
    octagon_translated = list(translate(octagon, 100, 100))
    dwg.add(dwg.polygon(octagon_translated, **style))
    # rotate it 
    octagon_rotated = list(rotate(translate(octagon_translated, 10, 10), math.pi/8))
    dwg.add(dwg.polygon(octagon_rotated, **style))
    # scale it
    # make sure first to scale it, then to translate it
    octagon_scaled = list(translate(scale(octagon, 10, 10), 500, 500))
    dwg.add(dwg.polygon(octagon_scaled, **style))
    dwg.save(pretty=True)

if __name__ == '__main__':
    name = "shapes_extension"
    main(name)