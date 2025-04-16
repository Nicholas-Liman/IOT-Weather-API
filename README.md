
```markdown
# Clima Atual com ThingSpeak

Este projeto em Python acessa periodicamente a [API do OpenWeatherMap](https://openweathermap.org/current) para obter a **temperatura** e a **umidade** de uma cidade específica e envia esses dados para um canal no **ThingSpeak**, onde é possível gerar gráficos e visualizações em tempo real.

## 📦 Requisitos

- Python 3.x  
- Bibliotecas: `requests`

Instale as dependências com:

```bash
pip install requests
```

## ⚙️ Configuração

Antes de rodar o projeto, você precisa criar um arquivo chamado `secrets.json` com suas credenciais e a cidade desejada.

### Como obter as credenciais

1. Acesse: [https://openweathermap.org/](https://openweathermap.org/)
2. Crie uma conta e vá até **API keys** no seu perfil.
3. Copie a sua **chave de API**.

Agora, no [ThingSpeak](https://thingspeak.com):

1. Faça login ou crie uma conta.
2. Vá em **Channels** > **New Channel**
3. Adicione um nome e no mínimo 2 campos (Field1, Field2).
4. Copie:
   - **Channel ID**
   - **Write API Key**

### Estrutura do `secrets.json`

```json
{
  "city": "NOME_DA_CIDADE",
  "openweather_api_key": "SUA_CHAVE_OPENWEATHER",
  "channel_id": SEU_CHANNEL_ID,
  "write_api_key": "SUA_WRITE_API_KEY"
}
```

Mantenha este arquivo na **raiz do projeto**, junto com o script Python.

## ▶️ Executando

Com tudo configurado, execute o script com:

```bash
python clima.py
```

A cada 15 segundos, ele:
- Consulta a temperatura e a umidade da cidade definida.
- Exibe os dados no terminal.
- Envia para o ThingSpeak.

## 🛡️ Segurança

Nunca suba o `secrets.json` para o GitHub.  
Adicione ao seu `.gitignore`:

```
secrets.json
```

---

Feito por **Nicholas Lima** como caso de estudo
