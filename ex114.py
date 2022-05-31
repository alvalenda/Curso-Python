# ex 114: aula 23
import urllib.request
import urllib.error
import requests
# utilizando urllib.request
url = "http://www.pudim.com.br"
# url = "http://roladentro.com"
try:
    requerimento = urllib.request.Request(url)
except Exception as er:
    print(f'\033[1;31m ERRO: {er}\033[m')
else:
    print(f'{url}\t{requerimento}')
    try:
        resposta = urllib.request.urlopen(requerimento)
    except urllib.error.HTTPError as httpError:
        print(f'\033[1;31m O servidor não conseguiu moisés...\n Código do Erro: {httpError} \033[m')
    except urllib.error.URLError as urlError:
        print(f'\033[1;31m Falha ao alcalçar o servidor.\n Motivo: {urlError} \033[m')
    else:
        print(f'{url}\t{resposta}')
        print(f'\033[1;32m O WEBSITE ESTÁ FUNCIONANDOW SHOW!\033[m')

# Utilizando requests
url = "https://www.google.com"
try:
    page = requests.get(url)
except requests.exceptions.ConnectionError:
    print(f"URL {url} not reachable")
else:
    print(f'{url}\t{page.status_code}')
    print(f'\033[1;32m O WEBSITE ESTÁ FUNCIONANDOW SHOW!\033[m')
