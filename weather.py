import requests
import time
import json

# Lê as credenciais do arquivo secrets.json
with open("secrets.json", "r", encoding="utf-8") as file:
    secrets = json.load(file)

CITY = secrets["city"]
OPENWEATHER_API_KEY = secrets["openweather_api_key"]
CHANNEL_ID = secrets["channel_id"]
WRITE_API_KEY = secrets["write_api_key"]
THINGSPEAK_URL = "https://api.thingspeak.com/update"

# URL da API de clima
API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={OPENWEATHER_API_KEY}&units=metric&lang=pt_br"

# Função que organiza os dados recebidos da API
def enviar_para_thingspeak(temp, umidade):
    payload = {
        "api_key": WRITE_API_KEY,
        "field1": temp,
        "field2": umidade
    }
    # Espera a resposta do HTTP e responde conforme o código recebido
    response = requests.get(THINGSPEAK_URL, params=payload)
    if response.status_code == 200 and response.text != "0":
        print("Sucesso ao enviar")
    else:
        print(f"Erro ao enviar: {response.status_code} | Resposta: {response.text}")

# Roda o código indefinadamente ou até encontrar um erro
while True:
    try:
        # Se a resposta da conexão for 200, salva e envia para o ThingSpeak
        resposta = requests.get(API_URL)
        if resposta.status_code == 200:
            dados = resposta.json()
            temperatura = dados["main"]["temp"]
            umidade = dados["main"]["humidity"]

            enviar_para_thingspeak(temperatura, umidade)
        
        # Se o código HTTP não for de sucesso, avisa o erro e faz um relatório sobre qual foi o erro
        else:
            print("Erro ao obter dados da API:", resposta.status_code)
    
    # Se qualquer erro acontecer na execução, ele é relatado aqui.
    except Exception as e:
        print("Erro ao tentar executar:", e)

    time.sleep(15)
