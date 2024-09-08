from typing import Dict

from src.dto import Harmonica


class HarmonicaDrawer:
    tone: str
    hole_1: Dict
    hole_2: Dict
    hole_3: Dict
    hole_4: Dict
    hole_5: Dict
    hole_6: Dict
    hole_7: Dict
    hole_8: Dict
    hole_9: Dict
    hole_10: Dict
    _overblow_2: str
    _overblow_1: str
    _blow: str
    _hole_number: str
    _draw: str
    _bending_1: str
    _bending_2: str
    _bending_3: str

    def __init__(self, harmonica: Harmonica):
        self.tone = harmonica.tone
        self.hole_1 = harmonica.hole_01
        self.hole_2 = harmonica.hole_02
        self.hole_3 = harmonica.hole_03
        self.hole_4 = harmonica.hole_04
        self.hole_5 = harmonica.hole_05
        self.hole_6 = harmonica.hole_06
        self.hole_7 = harmonica.hole_07
        self.hole_8 = harmonica.hole_08
        self.hole_9 = harmonica.hole_09
        self.hole_10 = harmonica.hole_10
        self._draw_layers()

    def _draw_layers(self):
        layers_order = [
            "overblow_2",
            "overblow_1",
            "blow",
            "draw",
            "bending_1",
            "bending_2",
            "bending_3",
        ]
        parsed_layers = []
        for layer in layers_order:
            string_layer = ""
            holes = [
                self.hole_1,
                self.hole_2,
                self.hole_3,
                self.hole_4,
                self.hole_5,
                self.hole_6,
                self.hole_7,
                self.hole_8,
                self.hole_9,
                self.hole_10,
            ]
            for hole in holes:
                note = hole.get(layer)
                if note:
                    if len(note) == 1:
                        string_layer += f"| {note} "
                    else:
                        string_layer += f"|{note} "
                else:
                    string_layer += "    "
            string_layer += "\n"
            parsed_layers.append(string_layer)
        number_string = "| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |10\n"
        self._overblow_2 = parsed_layers[0]
        self._overblow_1 = parsed_layers[1]
        self._blow = parsed_layers[2]
        self._hole_number = number_string
        self._draw = parsed_layers[3]
        self._bending_1 = parsed_layers[4]
        self._bending_2 = parsed_layers[5]
        self._bending_3 = parsed_layers[6]

    def __str__(self):
        return f"TONE: {self.tone}\n_______\n{self._overblow_2}{self._overblow_1}{self._blow}{self._hole_number}{self._draw}{self._bending_1}{self._bending_2}{self._bending_3}"
