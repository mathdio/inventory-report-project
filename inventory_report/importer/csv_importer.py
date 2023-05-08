from .importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith(".csv"):
            with open(path) as file:
                products_reader = csv.DictReader(file)
                products_list = [row for row in products_reader]
                return products_list
        else:
            raise ValueError("Arquivo inválido")
