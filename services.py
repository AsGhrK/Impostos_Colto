
import requests


def consultar_cnpj(cnpj):
    url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None


def consultar_cambio():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return float(data['USDBRL']['bid'])
    else:
        return None
