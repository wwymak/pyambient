#include "FastNoiseLite.h"

FastNoiseLite noise_c(int noise_type, int seed, double freq, int fractal, int octaves,
    double lacunarity, double gain, int perturb, double domain_warp_amp, int cellular_distance,
    int cellular_return_val, float jitter) {

  FastNoiseLite noise_gen;
  noise_gen.SetNoiseType((FastNoiseLite::NoiseType) noise_type);
  noise_gen.SetSeed(seed);
  noise_gen.SetFrequency(freq);

  if (cellular_distance != -1){

  noise_gen.SetCellularDistanceFunction((FastNoiseLite::CellularDistanceFunction) cellular_distance);
  noise_gen.SetCellularReturnType((FastNoiseLite::CellularReturnType) cellular_return_val);
  noise_gen.SetCellularJitter(jitter);
  }

  if (perturb != 0) noise_gen.SetDomainWarpAmp(domain_warp_amp);
  if (fractal != 0) {
    noise_gen.SetFractalType((FastNoiseLite::FractalType) (fractal));
    noise_gen.SetFractalOctaves(octaves);
    noise_gen.SetFractalLacunarity(lacunarity);
    noise_gen.SetFractalGain(gain);
  }

  return noise_gen;
}

void* noise_2d_c(int height, int width,int noise_type,  int seed, double freq,
    int fractal, int octaves, double lacunarity, double gain,
    int perturb, double domain_warp_amp, int cellular_distance,
    int cellular_return_val, float jitter) {

    FastNoiseLite noise_gen = noise_c(noise_type,seed, freq, fractal, octaves, lacunarity,
        gain, perturb, domain_warp_amp, cellular_distance, cellular_return_val, jitter);
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

void* noise_3d_c(int height, int width, int depth, int noise_type, int seed, double freq,
    int fractal, int octaves, double lacunarity, double gain, int perturb,
    double domain_warp_amp, int cellular_distance,
    int cellular_return_val, float jitter) {

    FastNoiseLite noise_gen = noise_c(noise_type,seed, freq, fractal, octaves,
        lacunarity, gain, perturb, domain_warp_amp, cellular_distance, cellular_return_val, jitter);
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

float single_noise_2d(float x, float y, int noise_type,int seed, double freq,
    int fractal, int octaves, double lacunarity, double gain,
    int perturb, double domain_warp_amp, int cellular_distance,
    int cellular_return_val, float jitter) {

    FastNoiseLite noise_gen = noise_c(noise_type,seed, freq, fractal, octaves, lacunarity,
        gain, perturb, domain_warp_amp, cellular_distance, cellular_return_val, jitter);
    return noise_gen.GetNoise((float)x, (float)y);
}

float single_noise_3d(float x, float y, float z,  int noise_type, int seed, double freq,
    int fractal, int octaves, double lacunarity, double gain,
    int perturb, double domain_warp_amp, int cellular_distance,
    int cellular_return_val, float jitter) {

    FastNoiseLite noise_gen = noise_c(noise_type, seed, freq, fractal, octaves, lacunarity,
        gain, perturb, domain_warp_amp, cellular_distance, cellular_return_val, jitter);
    return noise_gen.GetNoise((float)x, (float)y, (float)z);
}
