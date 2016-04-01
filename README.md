# pyparticle
Inspired by Grant Kot's various fluid simulators he's made over the years.
I originally made a version of this in C# using XNA Game Studio Express. This one is less efficient, but much cleaner.
Right now there's basic particle bounds checking and velocity. Eventually I'd like to enable the use of force to be able to apply a force equal to the function of a damped sine wave. The idea is to be repulsive at short distances and attractive at long distances, making the fluid seem viscous.
