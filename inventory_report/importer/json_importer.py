from .importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith(".json"):
            with open(path) as file:
                products_list = json.load(file)
                return products_list
        else:
            raise ValueError("Arquivo inválido")
