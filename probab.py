import matplotlib as ml
import numpy as np
import pylab as pl
import random

plot_x = []
plot_y = []

points = [
    {
        'x' : 5,
        'y' : 5
    },
    {
        'x' : 15,
        'y' : 15
    },
    {
        'x' : 25,
        'y' : 5
    }
]

now = {
    'x' : 15,
    'y' : 15
}

for i in range(25000):
    val =  random.randint(1,6)
    if val in [1,2]:
        now['x'] = (now['x'] + points[0]['x'])/2.0
        now['y'] = (now['y'] + points[0]['y'])/2.0
        plot_x.append(now['x'])
        plot_y.append(now['y'])
    elif val in [3,4]:
        now['x'] = (now['x'] + points[1]['x'])/2.0
        now['y'] = (now['y'] + points[1]['y'])/2.0
        plot_x.append(now['x'])
        plot_y.append(now['y'])
    else:
        now['x'] = (now['x'] + points[2]['x'])/2.0
        now['y'] = (now['y'] + points[2]['y'])/2.0
        plot_x.append(now['x'])
        plot_y.append(now['y'])

pl.plot(plot_x,plot_y,'k+')
pl.show()
