from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport
import csv
import json


class Inventory:
    @classmethod
    def read_file_csv(cls, path):
        with open(path) as file:
            products_reader = csv.DictReader(file)
            products_list = [row for row in products_reader]
            return products_list

    @classmethod
    def read_file_json(cls, path):
        with open(path) as file:
            products_list = json.load(file)
            return products_list

    @classmethod
    def import_data(cls, path, report_type):
        file = None
        if path.endswith(".csv"):
            file = Inventory.read_file_csv(path)
        elif path.endswith(".json"):
            file = Inventory.read_file_json(path)
        if report_type == "simples":
            return SimpleReport().generate(file)
        if report_type == "completo":
            return CompleteReport().generate(file)
