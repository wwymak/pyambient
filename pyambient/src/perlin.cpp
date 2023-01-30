#include "FastNoiseLite.h"
#include <Python.h>

// This line must be included before all numpy array imports
//#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
//#include <numpy/ndarrayobject.h>

//PyObject* ConvertImageToNumpy(const cv::Mat& image) {
//
//    // Let's represent our 2D image with 3 channels
//    npy_intp dimensions[3] = {image.rows, image.cols, image.channels()};
//
//    // 2 dimensions are for a 2D image, so let's add another dimension for channels
//    return PyArray_SimpleNewFromData(image.dims + 1, (npy_intp*)&dimensions, NPY_UINT8, image.data);
//
//}
using namespace std;

FastNoiseLite perlin_c(int seed, double freq, int fractal, int octaves,
    double lacunarity, double gain, int perturb, double domain_warp_amp) {
  FastNoiseLite noise_gen;
  noise_gen.SetNoiseType(FastNoiseLite::NoiseType_Perlin);
  noise_gen.SetSeed(seed);
  noise_gen.SetFrequency(freq);
//  noise_gen.SetInterp((FastNoiseLite::Interp) interp);
  if (perturb != 0) noise_gen.SetDomainWarpAmp(domain_warp_amp);
  if (fractal != 0) {
    noise_gen.SetFractalType((FastNoiseLite::FractalType) (fractal - 1));
    noise_gen.SetFractalOctaves(octaves);
    noise_gen.SetFractalLacunarity(lacunarity);
    noise_gen.SetFractalGain(gain);
  }

  return noise_gen;
}

//std::vector<std::vector<float>> perlin_2d_c(int height, int width, int seed, double freq, int fractal, int octaves, double lacunarity, double gain, int perturb, double domain_warp_amp) {
//  int i,j;
//  double new_i, new_j;
//
//  std::vector<std::vector<float>> noiseData(width, std::vector<float>(height, 0));
//
//  FastNoiseLite noise_gen = perlin_c(seed, freq, fractal, octaves, lacunarity, gain, perturb, domain_warp_amp);
//
//  for(int row=0;row<noiseData.size();row++){
//    for(int col=0;col<noiseData[row].size();col++){
//        noiseData[row][col]= noise_gen.GetNoise((float)row, (float)col);}
//    }
//
//
//  return noiseData;
//}


void* perlin_2d_c(int height, int width, int seed, double freq, int fractal, int octaves, double lacunarity, double gain, int perturb, double domain_warp_amp) {

    FastNoiseLite noise_gen = perlin_c(seed, freq, fractal, octaves, lacunarity, gain, perturb, domain_warp_amp);
    int idx = 0;
    int size = height * width;
    float* noise = (float*)malloc(sizeof(float)*size);
    for(int row=0;row<height;row++){
        for(int col=0;col<width;col++){
            noise[idx]= noise_gen.GetNoise((float)row, (float)col);
            idx++;
       }

    }
    return noise;
}

void* perlin_3d_c(int height, int width, int depth, int seed, double freq, int interp, int fractal, int octaves, double lacunarity, double gain, int perturb, double domain_warp_amp) {

    FastNoiseLite noise_gen = perlin_c(seed, freq, fractal, octaves, lacunarity, gain, perturb, domain_warp_amp);
    int idx = 0;
    int size = height * width * depth;
    float* noise = (float*)malloc(sizeof(float)*size);
    for(int row=0;row<height;row++){
        for(int col=0;col<width;col++){
            for (int d=0;d<depth;d++) {
                noise[idx]= noise_gen.GetNoise((float)row, (float)col, (float)d);
                idx++;
            }
       }

    }
    return noise;
}

//std::vector<float> perlin_3d_c(int height, int width, int depth, int seed, double freq, int interp, int fractal, int octaves, double lacunarity, double gain, int perturb, double perturb_amplitude) {
//
//  std::vector<float>  noise(height, width * depth);
//  int i,j,k;
//  double new_i, new_j, new_k;
//
//  FastNoise noise_gen = perlin_c(seed, freq, interp, fractal, octaves,
//   lacunarity, gain, perturb, perturb_amplitude);
//
//  for (k = 0; k < depth; ++k) {
//    for (i = 0; i < height; ++i) {
//      for (j = 0; j < width; ++j) {
//        new_i = (double) i;
//        new_j = (double) j;
//        new_k = (double) k;
//
//        if (perturb == 1) {
//          noise_gen.GradientPerturb(new_j, new_i, new_k);
//        } else if (perturb == 2) {
//          noise_gen.GradientPerturbFractal(new_j, new_i, new_k);
//        }
//        if (fractal == 0) {
//          noise(i, j + k * width) = noise_gen.GetPerlin(new_j, new_i, new_k);
//        } else {
//          noise(i, j + k * width) = noise_gen.GetPerlinFractal(new_j, new_i, new_k);
//        }
//      }
//    }
//  }
//
//  return noise;
//}

//std::vector<float> gen_perlin2d_c(double x, double y, double freq, int seed, int interp) {
//  std::vector<float>  noise(x.size());
//  FastNoise generator = perlin_c(seed, freq, interp, 0, 0, 0.0, 0.0, 0, 0.0);
//  for (int i = 0; i < x.size(); i++) {
//    noise[i] = generator.GetPerlin(x[i], y[i]);
//  }
//  return noise;
//}
//
//std::vector<float> gen_perlin3d_c(double x, double y, double z, double freq, int seed, int interp) {
//  std::vector<float> noise(x.size());
//  FastNoise generator = perlin_c(seed, freq, interp, 0, 0, 0.0, 0.0, 0, 0.0);
//  for (int i = 0; i < x.size(); i++) {
//    noise[i] = generator.GetPerlin(x[i], y[i], z[i]);
//  }
//  return noise;
//}