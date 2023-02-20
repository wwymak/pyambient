import numpy as np
from typing import  Union
from enum import Enum

class PatternType(Enum):
    wave = 0
    sphere = 1
    checkerboard = 2


def generate_pattern_array(
    dimensions:tuple, pattern,
    frequency:float = 0.01, **kwargs) -> np.array:

    x = dimensions[0]
    y = dimensions[1] if len(dimensions) > 1 else None
    z = dimensions[2] if len(dimensions) > 2 else None
    t = dimensions[3] if len(dimensions) > 3 else None
    if pattern == PatternType.wave:
        return generate_waves(x, y, z, t, frequency)
    if pattern == PatternType.sphere:
        return generate_spheres(x, y, z, t, frequency)
    if pattern == PatternType.checkerboard:
        return generate_checkerboard(x, y, z, t, frequency)


def generate_waves(x: np.array, y:np.array = None,
                   z: np.array= None, t: np.array= None,
                   frequency:float = 0.01, **kwargs) -> np.array:
    """
    Generate a wave pattern
    :param x,y,z,t The coordinates to get pattern from
    :param frequency:frequency of the generator
    :param kwargs:
    :return: np.array of pattern
    """

    if not y:
        y = np.zeros(len(x))
    if not z:
        z = np.zeros(len(x))
    if not t:
        t = np.zeros(len(x))

    dist_sq = ((x * frequency)**2 +
               (y * frequency)**2 +
               (z * frequency)**2 +
               (t * frequency)**2 )

    distance = np.sqrt(dist_sq)
    return np.cos(distance * np.pi * 2)


def generate_spheres(x: np.array, y:np.array = None,
                   z: np.array= None, t: np.array= None,
                   frequency:float = 0.01, **kwargs) -> np.array:
    """
    Generate a  pattern of concentric circles centered at 0. The output value
    is the shortest distance to the nearest sphere normalised to be
    between -1 and 1. The frequency
    determines the radius multiplier for each unit sphere.
    :param x,y,z,t The coordinates to get pattern from
    :param frequency:frequency of the generator
    :param kwargs:
    :return: np.array of pattern
    """
    if not y:
        y = np.zeros(len(x))
    if not z:
        z = np.zeros(len(x))
    if not t:
        t = np.zeros(len(x))
    dist_sq = ((x * frequency)**2 +
               (y * frequency)**2 +
               (z * frequency)**2 +
               (t * frequency)**2 )

    distance = np.sqrt(dist_sq)
    dist_small = distance - np.floor(distance)
    dist_large = 1 - dist_small
    return 1 - np.minimum(dist_small, dist_large) * 4


def generate_checkerboard(x: np.array, y:np.array = None,
                   z: np.array= None, t: np.array= None,
                   frequency:float = 0.01, **kwargs) -> np.array:
    if not y:
        y = np.zeros(len(x))
    if not z:
        z = np.zeros(len(x))
    if not t:
        t = np.zeros(len(x))

    output = (np.floor(x * frequency) +
              np.floor(y * frequency) +
              np.floor(z * frequency) +
              np.floor(t * frequency) )

    return (output == 0).astype(int)
