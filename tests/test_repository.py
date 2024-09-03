from src.dto import HarmonicaTones, Harmonica
from src.repository import HarmonicaRepository


def test_load_harmonica_by_american_tone():
    harmonica = HarmonicaRepository().load_harmonica_by_american_tone(HarmonicaTones.A)
    expected_harmonica = Harmonica(
        tone=HarmonicaTones.A.name,
        hole_01={"draw": "B", "blow": "A", "bending_1":"A#"},
        hole_02={"draw": "E", "blow": "C#", "bending_1":"D#", "bending_2":"D"},
        hole_03={"draw": "G#", "blow": "E", "bending_1":"G", "bending_2":"F#", "bending_3":"F"},
        hole_04={"draw": "B","blow": "A", "bending_1":"A#"},
        hole_05={"draw": "D", "blow": "C#"},
        hole_06={"draw": "F#", "blow": "E", "bending_1":"F"},
        hole_07={"draw": "G#", "blow": "A"},
        hole_08={"draw": "B", "blow": "C#", "overblow_1": "C"},
        hole_09={"draw": "D", "blow": "E", "overblow_1": "D#"},
        hole_10={"draw": "F#", "blow": "A", "overblow_1": "G#", "overblow_2": "G"},
    )

    assert harmonica == expected_harmonica