import requests

# Conselhos
url = 'https://api.adviceslip.com/advice'

response = requests.get(url)

if response.status_code == 200:
    response_json = response.json()
    conselho = response_json['slip']['advice']
    print(f'Conselho do dia: {conselho}')
else:
    print(f'Erro de conexão: {response.status_code}')

# Tradução
traducao = input('Deseja traduzir o conselho? S/N ')
if traducao.upper() == 'S':
    idioma_destino = input('Digite o idioma para traduzir (por exemplo, "pt-br" para Português): ')
    if idioma_destino.lower():
        # Insira aqui sua chave da API
        google_translate_api = f'https://translation.googleapis.com/language/translate/v2?key=SUA_API_KEY'
        payload = {
            'q': conselho,
            'source': 'en',
            'target': idioma_destino,
            'format': 'text'
        }
        response = requests.post(google_translate_api, data=payload)

        if response.status_code == 200:
            traduzindo = response.json()
            conselho_traduzido = traduzindo['data']['translations'][0]['translatedText']
            print(f'Conselho traduzido: {conselho_traduzido}')
        else:
            print(f'Erro na tradução: {response.status_code}')
    else:
        print('Você não especificou um idioma de destino.')




