from src.dto import HarmonicaTones
from src.harmonica_drawer import HarmonicaDrawer
from src.repository import HarmonicaRepository


def test_blue():
    harmonica = HarmonicaRepository().load_harmonica_by_american_tone(HarmonicaTones.A.name)
    assert HarmonicaDrawer(harmonica)
