import json
from datetime import datetime, timedelta
from urllib.error import HTTPError, URLError
from urllib.request import urlopen


def buscar_cotacao_dolar():
    url_base = (
        "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
        "CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data}'"
        "&$top=1&$format=json"
    )
    data_consulta = datetime.now()

    for _ in range(7):
        data_formatada = data_consulta.strftime("%m-%d-%Y")
        url = url_base.format(data=data_formatada)

        try:
            with urlopen(url) as resposta:
                dados = json.load(resposta)
        except (HTTPError, URLError) as erro:
            raise RuntimeError(
                "Nao foi possivel consultar a cotacao oficial do Banco Central."
            ) from erro

        valores = dados.get("value", [])
        if valores:
            cotacao = valores[0]
            return cotacao["cotacaoVenda"], cotacao["dataHoraCotacao"]

        data_consulta -= timedelta(days=1)

    raise RuntimeError("Nao foi encontrada uma cotacao disponivel nos ultimos 7 dias.")


valor_real = float(input("Digite o valor em reais: R$ "))
cotacao_dolar, data_hora_cotacao = buscar_cotacao_dolar()
valor_dolar = valor_real / cotacao_dolar

print(f"Valor informado em reais: R$ {valor_real:.2f}")
print(f"Cotacao oficial do dolar (venda): R$ {cotacao_dolar:.4f}")
print(f"Data da cotacao utilizada: {data_hora_cotacao}")
print(f"Valor em dolares: US$ {valor_dolar:.2f}")
