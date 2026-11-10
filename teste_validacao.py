
import requests

url = "http://127.0.0.1:5000/api/ocorrencias"

dados = {
    "tipo": "",
    "descricao": "",
    "local": "",
    "municipio": "",
    "estado": "",
    "dataOcorrencia": ""
}

resposta = requests.post(url, json=dados)

print("Status:", resposta.status_code)
print("Resposta:", resposta.text)
