from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport
import csv
import json
import xml.etree.ElementTree as ET


class Inventory:
    def read_file_csv(path):
        with open(path) as file:
            products_reader = csv.DictReader(file)
            products_list = [row for row in products_reader]
            return products_list

    def read_file_json(path):
        with open(path) as file:
            products_list = json.load(file)
            return products_list

    def read_file_xml(path):
        with open(path) as file:
            tree = ET.parse(file)
            root = tree.getroot()
            products_list = [
                {elem.tag: elem.text for elem in record}
                for record in root.findall("record")
            ]
            return products_list

    @classmethod
    def path_reader(cls, path):
        if path.endswith(".csv"):
            return Inventory.read_file_csv(path)
        elif path.endswith(".json"):
            return Inventory.read_file_json(path)
        elif path.endswith(".xml"):
            return Inventory.read_file_xml(path)
        else:
            raise ValueError("Invalid file format")

    @classmethod
    def import_data(cls, path, report_type):
        file = Inventory.path_reader(path)

        if report_type == "simples":
            return SimpleReport().generate(file)
        if report_type == "completo":
            return CompleteReport().generate(file)
