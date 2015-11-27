#!/usr/bin/python2.7

import math
import matplotlib.pyplot as plt

x = []
y = []
A = 1
decay_const = 7
offset = 500
angular_frequency = 1
phase_angle = 1
desired_max_dist = 28
bounding_dist = .75*(desired_max_dist)

#X generator
x_count = 200
x_diff = float(bounding_dist) / float(x_count)
print x_diff


for j in range(x_count):
    sink = j*x_diff
    x.append(sink)

for l in x:
    mink = l * 1/desired_max_dist
    soon = math.e**(-(mink))*math.cos(2 * math.pi * mink)
    y.append(soon)

plt.plot(x,y)
plt.ylabel('Repulsion Coefficient')
plt.xlabel('Distance')
plt.show()
