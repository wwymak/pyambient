
from enum import Enum
from math import prod
import numpy as np

from pyambient.src import cppyy

# _perlin_2d = cppyy.gbl.perlin_2d_c
# _perlin_3d = cppyy.gbl.perlin_3d_c
# _simplex_2d = cppyy.gbl.simplex_2d_c
# _simplex_3d = cppyy.gbl.simplex_3d_c
# _simplex_4d = cppyy.gbl.simplex_4d_c
_noise_2d = cppyy.gbl.noise_2d_c
_noise_3d = cppyy.gbl.noise_3d_c

class NoiseType(Enum):
    open_simplex2=0
    open_simplex2S=1
    cellular=2
    perlin=3
    value_cubic=4
    value=5

class FractalType(Enum):
    none = 0
    fbm = 1
    ridged = 2
    pingpong = 3
    domain_warp_progressive = 4
    domain_warp_independent = 5


class RotationType3D(Enum):
    none = 0
    improve_xy_planes = 1
    improve_xz_planes = 2


class CellularDistanceFunction(Enum):
    euclidean = 0
    euclidean_square = 1
    manhattan = 2
    hybrid=3


class CellularReturnType(Enum):

    cell_value=0
    distance=1
    distance2=2
    distance2_add=3
    distance2_sub=4
    distance2_mul=5
    distance2_div=6


class DomainWarpType(Enum):
    open_simplex2=0
    open_simplex2_reduced=1
    basic_grid=2


def generate_noise_arr(dimensions:tuple, noise_type='perlin', frequency:float = 0.01,
                   fractal = 'fbm', octaves:int = 3, lacunarity:int = 2,
                    gain:float = 0.5, cellular_distance_fn=-1, cellular_return_type=0,
                       domain_warp_type=0, jitter=0,
                   perturb = 0, domain_warp_amp = 1, seed: int = None) :
    fractal_type = FractalType[fractal].value
    noise_type = NoiseType[noise_type].value
    common_args = dict(
        noise_type= noise_type,
        seed=np.random.randint(0, 1000) if not seed else seed,
        freq=frequency,
        fractal=fractal_type,
        octaves=octaves,
        lacunarity=lacunarity,
        gain=gain,
        perturb=perturb,
        domain_warp_amp=domain_warp_amp,
        cellular_distance=cellular_distance_fn,
        cellular_return_val=cellular_return_type, jitter=jitter
    )
    if len(dimensions) == 2:
        noise = _noise_2d(
            height=dimensions[0],
            width=dimensions[1],
            **common_args)

    elif len(dimensions) == 3:
        noise = _noise_3d(
            height=dimensions[0],
            width=dimensions[1],
            depth=dimensions[2],
            **common_args)

    else:
        raise Exception("number of dimensions not supported")

    noise_np = np.frombuffer(noise, dtype=np.float32, count=prod(dimensions))
    return noise_np.reshape(dimensions)

def generate_perlin(dimensions:tuple, frequency:float = 0.01,
                   fractal = 'fbm', octaves:int = 3, lacunarity:int = 2,
                    gain:float = 0.5,
                   perturb = 0, domain_warp_amp = 1, seed: int = None) :
    fractal_type = FractalType[fractal].value
    common_args = dict(
        seed=np.random.randint(0, 1000) if not seed else seed,
        freq=frequency,
        fractal=fractal_type,
        octaves=octaves,
        lacunarity=lacunarity,
        gain=gain,
        perturb=perturb,
        domain_warp_amp=domain_warp_amp,
    )
    if len(dimensions) == 2:
        noise = _perlin_2d(
            height=dimensions[0],
            width=dimensions[1],
            **common_args)

    elif len(dimensions) == 3:
        noise = _perlin_3d(
            height=dimensions[0],
            width=dimensions[1],
            depth=dimensions[2],
            **common_args)

    else:
        raise Exception("number of dimensions not supported")

    noise_np = np.frombuffer(noise, dtype=np.float32, count=prod(dimensions))
    return noise_np.reshape(dimensions)


def generate_simplex(dimensions:tuple, frequency:float = 0.01,
                   fractal = 'fbm', octaves:int = 3, lacunarity:int = 2,
                    gain:float = 0.5,
                   perturb = 0, domain_warp_amp = 1, seed: int = None) :
    fractal_type = FractalType[fractal].value
    common_args = dict(
        seed=np.random.randint(0, 1000) if not seed else seed,
        freq=frequency,
        fractal=fractal_type,
        octaves=octaves,
        lacunarity=lacunarity,
        gain=gain,
        perturb=perturb,
        domain_warp_amp=domain_warp_amp,
    )
    if len(dimensions) == 2:
        noise = _simplex_2d(
            height=dimensions[0],
            width=dimensions[1],
            **common_args)

    elif len(dimensions) == 3:
        noise = _simplex_3d(
            height=dimensions[0],
            width=dimensions[1],
            depth=dimensions[2],
            **common_args)

    else:
        raise Exception("number of dimensions not supported")

    noise_np = np.frombuffer(noise, dtype=np.float32, count=prod(dimensions))
    return noise_np.reshape(dimensions)

