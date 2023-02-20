# from math import prod
# import numpy as np
#
# from pyambient.py.noise import  generate_noise_arr
#
# def blue_noise(dimensions:tuple, filter_std_dev=10,  seed_frac=0.1):
#     """
#
#     :param dimensions:
#     :param filter_std_dev: s tandard deviation of the gaussian filter to apply during the
#         search for clusters and voids.
#     :param seed_frac:  The fraction of pixels to seed the algorithm with during the start
#     :return:
#     """
#     num_pixels = prod(dimensions)
#     num_seeds= np.floor(np.maximum(1, np.minimum((num_pixels - 1) / 2, num_pixels * seed_frac)));
#     seed_texture = generate_noise_arr(dimensions, noise_type='white')
#
#
#     seed_texture[] < - ifelse(order(seed_texture) <= n_seeds, 1, 0)
#     kernel < - create_kernel(dim, sd)
#     while (TRUE) {
#     tightest < - find_tightest_cluster(seed_texture, kernel)
#     seed_texture[tightest] < - 0
#     voidest < - find_voidest_cluster(seed_texture, kernel)
#     if (all(tightest == voidest)) {
#     seed_texture[tightest] < - 1
#     break
#     } else {
#     seed_texture[voidest] < - 1
#
# }
# }
# dither < - array(0, dim=dim)
# pattern < - seed_texture
# for (i in rev(seq_len(n_seeds)) - 1) {
#     tightest < - find_tightest_cluster(pattern, kernel)
# pattern[tightest] < - 0
# dither[tightest] < - i
# }
# pattern < - seed_texture
# for (i in seq(n_seeds, floor(n_pixels / 2) - 1)) {
# voidest < - find_voidest_cluster(pattern, kernel)
# pattern[voidest] < - 1
# dither[voidest] < - i
# }
# for (i in seq(floor(n_pixels / 2), n_pixels - 1)) {
# tightest < - find_tightest_cluster(pattern, kernel)
# pattern[tightest] < - 1
# dither[tightest] < - i
# }
# dither < - dither / (n_pixels - 1)
# if (length(dim) == 1) {
# as.vector(dither)
# } else if (length(dim) == 2) {
# as.matrix(dither)
# } else {
# dither
# }
# }