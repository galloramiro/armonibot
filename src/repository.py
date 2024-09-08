import json

from src.config import DATA_FOLDER
from src.dto import Harmonica, HarmonicaTones


class HarmonicaRepository:
    _DATA_FILE = f"{DATA_FOLDER}/harmonicas.json"

    def load_harmonica_by_american_tone(self, tone: str):
        with open(self._DATA_FILE) as file:
            harmonicas = json.load(file)
        expected_harmonica = list(filter(lambda x: x["tone"] == tone, harmonicas))

        if not expected_harmonica:
            raise ValueError(f"Harmonica with tone {tone} not found")

        return Harmonica(**expected_harmonica[0])
