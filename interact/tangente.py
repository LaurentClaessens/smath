#! /usr/bin/sage -python
# -*- coding: utf8 -*-

from sage.all import *

def error_msg(msg):
    print '<html><p style="font-family:Arial, sans-serif;color:#000"><span style="color:red;font-weight:bold">Error</span>: %s</p></html>' % msg

@interact
def interactive_2d_plotter(expression=input_box('sin(x)', 'Expression', str), x_range=range_slider(-10,10,1,(0,10), label='X Range'), square=checkbox(True, 'Square'), axes=checkbox(False, 'Show Axes')):
    if expression:
        try:
            expression = SR(expression) # turn string into a Sage expression
        except TypeError:
            print error_msg('This is not an expression.')
            return
        try:
                xmin, xmax = x_range
                if square or not axes:
                    print "var('%s')\nplot(%s).show(%s%s%s)" % (expression.variables()[0], repr(expression), 'aspect_ratio=1' if square else '', ', ' if square and not axes else '', 'axes=False' if not axes else '')
                    if square:
                        plot(expression, xmin, xmax).show(aspect_ratio=1, axes=axes)
                    else:
                        plot(expression, xmin, xmax).show(axes=axes)
                else:
                    print "var('%s')\nplot(%s)" % (expression.variables()[0], repr(expression))
                    plot(expression, xmin, xmax).show(axes=axes)
        except ValueError:
            print error_msg('This expression has more than one variable.')
            return
        except TypeError:
            print error_msg("This expression contains an unknown function.")
            return

interactive_2d_plotter()
