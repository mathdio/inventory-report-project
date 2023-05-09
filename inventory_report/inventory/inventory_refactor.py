from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport
from .inventory_iterator import InventoryIterator
from collections.abc import Iterable


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path, report_type):
        data = self.importer.import_data(path)
        self.data += data

        if report_type == "simples":
            return SimpleReport().generate(self.data)
        elif report_type == "completo":
            return CompleteReport().generate(self.data)
        else:
            raise ValueError("Invalid report type!")

    def __iter__(self):
        return InventoryIterator(self.data)
