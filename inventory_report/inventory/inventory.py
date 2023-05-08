from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport
import csv


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):
        with open(path) as file:
            products_reader = csv.DictReader(file)
            products_list = [row for row in products_reader]

            if report_type == "simples":
                return SimpleReport().generate(products_list)
            if report_type == "completo":
                return CompleteReport().generate(products_list)
