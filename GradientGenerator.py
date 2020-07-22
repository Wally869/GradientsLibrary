from __future__ import annotations
from typing import List, Dict

from LerpColors import *
from ConverterYUVtoRGB import YUVtoRGB

import imageio

import argparse


def GenerateGradient(startColor: List[float], targetColor: List[float], width: int = 2, height: int = 1) -> List[List[float]]:
    lineGradient = LerpColorMultipleSteps(startColor, targetColor, width)
    return [lineGradient for i in range(height)]


def Main(yuv1: List[float], yuv2: List[float], width: int, height: int) -> List[float]:
    gradientYUV = GenerateGradient(yuv1, yuv2, width, height)
    gradientRGB = [
        [
            YUVtoRGB(*col) for col in arr
        ] for arr in gradientYUV
    ]

    return gradientRGB


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c1", help="string, Color in YUV colorspace, with values seperated by underscores (e.g. 0.4_-0.1_0.2", type=str)
    parser.add_argument("-c2", help="string, Color in YUV colorspace, with values seperated by underscores (e.g. 0.4_-0.1_0.2", type=str)
    parser.add_argument("-o", help="string, output filepath")
    parser.add_argument("-width", help="int, Width of generated gradient image", type=int, default=150)
    parser.add_argument("-height", help="int, Height of generated gradient image", type=int, default=50)

    args = parser.parse_args()
    startColor = [float(val) for val in args.c1.split("_")]
    targetColor = [float(val) for val in args.c2.split("_")]
    print(startColor)
    print(targetColor)

    gradient = GenerateGradient(startColor, targetColor, args.width, args.height)
    #imageio.imwrite("{}___{}.jpg".format(args.c1, args.c2), gradient)
    imageio.imwrite(args.o, gradient)

