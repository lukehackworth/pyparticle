# pyparticle
Inspired by Grant Kot's various fluid simulators he's made over the years.
I originally made a version of this in C# using XNA Game Studio Express. This one is less efficient, but much cleaner.
In each frame and for each particle, an average force is calculated, which will be a summation of all the forces applied to a particle. The particle's location will change according to the average force, then bounds will be checked.
The force applied to an individual particle will be a function of a damped sine wave. The idea is to have both a repulsive force and attractive force, with the repulsive force being much stronger. The attractive force will(hopefully) create a viscous effect.
