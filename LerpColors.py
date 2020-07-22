from __future__ import annotations
from typing import List, Dict

def LerpColor(initialColor: List[float], targetColor: List[float], lerping_factor: float) -> List[float]:
    return [initialColor[i] + (targetColor[i] - initialColor[i]) * lerping_factor for i in range(len(initialColor))]

def LerpColorMultipleSteps(initialColor: List[float], targetColor: List[float], number_steps: int) -> List[List[float]]:
    return [LerpColor(initialColor, targetColor, i/number_steps) for i in range(number_steps + 1)]


