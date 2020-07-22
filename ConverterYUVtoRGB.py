from __future__ import annotations
from typing import List


def YUVtoRGB(Y: int, U: int, V: int) -> List[float]:
    R = Y + 1.14 * V
    G = Y - 0.395 * U - 0.581 * V
    B = Y + 2.033 * U
    return [R, G, B]


def RGBtoYUV(R: float, G: float, B: float) -> List[float]:
    Y = R * .299000 + G * .587000 + B * .114000
    U = 0.492 * (B - Y)
    V = 0.877 * (R - Y)
    return [Y, U, V]
