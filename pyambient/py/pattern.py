import numpy as np
from typing import  Union


def generate_waves(x: Union[float, np.array], y:Union[float, np.array] = 0,
                   z: Union[float, np.array] = 0, t: Union[float, np.array] = 0,
                   frequency:float = 0.01, **kwargs) -> np.array:
    """
    Generate a wave pattern
    :param x,y,z,t The coordinates to get pattern from
    :param frequency:frequency of the generator
    :param kwargs:
    :return: np.array of pattern
    """
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
    return 1 - (np.min(dist_small), np.max(dist_large)) * 4
