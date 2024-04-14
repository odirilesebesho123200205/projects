# Orbits

This is a simple program that simulates the orbits of planets around a star.

## Usage

The program can be run from the command line with the following command:

```
./orbits.sh <input_file> <duration>
```

Where `<input_file>` is a text file that contains the initial conditions for the simulation. The file should be formatted as follows:

```
<star_mass>
<planet_mass_1> <planet_x_1> <planet_y_1> <planet_vx_1> <planet_vy_1>
<planet_mass_2> <planet_x_2> <planet_y_2> <planet_vx_2> <planet_vy_2>
...
```

Where `<star_mass>` is the mass of the star, `<planet_mass_i>` is the mass of planet i, `<planet_x_i>` and `<planet_y_i>` are the initial x and y positions of planet i, and `<planet_vx_i>` and `<planet_vy_i>` are the initial x and y velocities of planet i.

Masses are specified in units of solar masses, positions are specified in units of astronomical units (AU), velocities are specified in units of AU/day, and time is specified in units of Earth days.

The `<duration>` argument is the duration of the simulation in Earth days.

## Example

To run a simulation with the initial conditions specified in the file `input.txt` for a duration of 365 Earth days, you would run the following command:

```
./orbits.sh input.txt 365
```

This would output the positions of the planets at each time step to the terminal.

An important test case for this program is the solar system. The initial conditions for the solar system are provided here:

```
1.0
3.00348959633e-06 0.0 0.0 0.0 6.174e-03
3.285e-07 0.38709893 0.0 0.0 47.87
4.8675e-06 0.72333199 0.0 0.0 35.02
5.97219e-06 1.00000011 0.0 0.0 29.78
6.4185e-07 1.52366231 0.0 0.0 24.077
1.89813e-06 5.202603191 0.0 0.0 13.07
5.68319e-05 9.554909596 0.0 0.0 9.69
8.68103e-05 19.218446062 0.0 0.0 6.81
1.02413e-05 30.110386869 0.0 0.0 5.43
1.471e-05 39.48168677 0.0 0.0 4.74
2.4478383e-06 0.0 0.0 0.0 -4.627
```

(TODO: this is most likely incorrect, please find authoritative source)

## Iterations

### Iteration 1

- [ ] Correctly parse input file
- [ ] Correctly format output
- [ ] Handle errors gracefully
- [ ] Meet basic simulation precision requirements

### Iteration 2

- [ ] Meet advanced simulation precision requirements
- [ ] Implement visualization

### Iteration 3

- [ ] Implement 3d visualization
- [ ] Allow the user to interactively edit the system
