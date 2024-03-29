from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(cls, products_list):
        manufacturing_dates = [
            datetime.strptime(product["data_de_fabricacao"], "%Y-%m-%d").date()
            for product in products_list
        ]
        oldest_date = min(manufacturing_dates)

        expiration_dates = [
            datetime.strptime(product["data_de_validade"], "%Y-%m-%d").date()
            for product in products_list
        ]
        expiration_dates.sort(reverse=True)
        today_date = datetime.today().date()
        closest_date = None
        for date in expiration_dates:
            if date > today_date:
                closest_date = date

        company_names = [
            product["nome_da_empresa"] for product in products_list
        ]
        company_most_common, _ = Counter(company_names).most_common()[0]

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com mais produtos: {company_most_common}"
        )
