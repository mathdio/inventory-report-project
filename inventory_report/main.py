import sys
from .inventory.inventory_refactor import InventoryRefactor
from .importer.csv_importer import CsvImporter
from .importer.json_importer import JsonImporter
from .importer.xml_importer import XmlImporter


def file_extension(path):
    if path.endswith(".csv"):
        return CsvImporter()
    elif path.endswith(".json"):
        return JsonImporter()
    elif path.endswith(".xml"):
        return XmlImporter()
    else:
        raise ValueError("Invalid file extension!")


def main():
    try:
        module, path, type = sys.argv
        importer = file_extension(path)

        report = InventoryRefactor(importer).import_data(path, type)
        sys.stdout.write(report)
    except ValueError:
        sys.stderr.write("Verifique os argumentos\n")


if __name__ == "__main__":
    main()
