from enum import Enum
from typing import Dict
from dataclasses import dataclass


class HarmonicaTones(Enum):
    A = ("A", "LA")
    B = ("B", "SI")
    C = ("C", "DO")
    D = ("D", "RE")
    E = ("E", "MI")
    F = ("F", "FA")
    G = ("G", "SOL")


@dataclass
class Harmonica:
    tone = HarmonicaTones
    hole_01: Dict[str, str]
    hole_02: Dict[str, str]
    hole_03: Dict[str, str]
    hole_04: Dict[str, str]
    hole_05: Dict[str, str]
    hole_06: Dict[str, str]
    hole_07: Dict[str, str]
    hole_08: Dict[str, str]
    hole_09: Dict[str, str]
    hole_10: Dict[str, str]
