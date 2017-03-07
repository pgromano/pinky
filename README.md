# Generate Random Numbers from a 2D Discrete Distribution

The `pinky` package is a Python implementation of Tristan Ursell's [matlab codes](https://www.mathworks.com/matlabcentral/fileexchange/35797-generate-random-numbers-from-a-2d-discrete-distribution/content/pinky.m), which simply given any real `N x M` probability matrix, can accurately sample the distribution.

### Basic Examples
```
import pinky

p = pinky.Pinky()

# Generate a single modal normal distribution
p.Gaussian()

# Generate 1000 samples along the distribution
sampled_points = p.sample(1000)
```
