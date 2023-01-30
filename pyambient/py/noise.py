

from math import prod
import numpy as np

from pyambient.src import cppyy

_perlin_2d = cppyy.gbl.perlin_2d_c
_perlin_3d = cppyy.gbl.perlin_3d_c


def generate_perlin(dimensions:tuple, frequency:float = 0.01,
                   fractal = 'fbm', octaves:int = 3, lacunarity:int = 2,
                    gain:float = 0.5,
                   perturb = 0, domain_warp_amp = 1) :
    if len(dimensions) == 2:
        noise = _perlin_2d(
            height=dimensions[0],
            width=dimensions[1],
            seed = np.random.randint(0, 1000),
            freq = frequency,
            fractal = 1,
            octaves = octaves,
            lacunarity = lacunarity,
            gain = gain,
            perturb =perturb,
            domain_warp_amp = domain_warp_amp,)

    elif len(dimensions) == 3:
        noise = _perlin_3d(
            height=dimensions[0],
            width=dimensions[1],
            depth=dimensions[2],
            seed = np.random.randint(0, 1000),
            freq = frequency,
            fractal = 1,
            octaves = octaves,
            lacunarity = lacunarity,
            gain = gain,
            perturb = octaves,
            domain_warp_amp = domain_warp_amp,)

    else:
        raise Exception("number of dimensions not supported")

    noise_np = np.frombuffer(noise, dtype=np.float32, count=prod(dimensions))
    return noise_np.reshape(dimensions)