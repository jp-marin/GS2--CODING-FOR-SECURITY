
import requests

url = "http://127.0.0.1:5000/api/ocorrencias"

# POST - Cadastrar
dados = {
    "tipo": "Assédio verbal",
    "descricao": "Relato fictício para teste acadêmico.",
    "local": "Avenida Central",
    "municipio": "São Paulo",
    "estado": "SP",
    "dataOcorrencia": "2026-10-15"
}

resposta = requests.post(url, json=dados)

print("POST:", resposta.status_code)
print(resposta.text)

if resposta.status_code == 201:
    id = resposta.json().get("id")

    # GET - Consultar
    resposta = requests.get(f"{url}/{id}")
    print("\nGET:", resposta.status_code)
    print(resposta.text)

    # PUT - Atualizar
    dados["tipo"] = "Outro"
    dados["descricao"] = "Descrição atualizada."

    resposta = requests.put(f"{url}/{id}", json=dados)
    print("\nPUT:", resposta.status_code)
    print(resposta.text)

    # DELETE - Excluir
    resposta = requests.delete(f"{url}/{id}")
    print("\nDELETE:", resposta.status_code)
    print(resposta.text)

    # GET - Verificar exclusão
    resposta = requests.get(f"{url}/{id}")
    print("\nGET após DELETE:", resposta.status_code)
    print(resposta.text)

else:
    print("Não foi possível cadastrar. Verifique a resposta.")
