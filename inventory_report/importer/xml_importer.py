from .importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith(".xml"):
            with open(path) as file:
                tree = ET.parse(file)
                root = tree.getroot()
                products_list = [
                    {elem.tag: elem.text for elem in record}
                    for record in root.findall("record")
                ]
                return products_list
        else:
            raise ValueError("Arquivo inválido")
