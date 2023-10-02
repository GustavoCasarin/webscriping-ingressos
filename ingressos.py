import requests
from bs4 import BeautifulSoup

def fazer_web_scraping(url):
    resposta = requests.get(url)
    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.content, 'html.parser')
        return soup
    else:
        print(f"Erro {resposta.status_code} ao acessar a página: {url}")
        return None

def extrair_informacoes_eventos(soup):
    informacoes_eventos = []
    if soup:
        for evento_div in soup.find_all('div', class_='conteudo-card'):
            nome = evento_div.find('h4', class_='mb-2.5').text.strip()
            dia = evento_div.find('p', class_='font-14 txt-color-alert mb-1').text.strip()
            informacoes_eventos.append({'nome': nome, 'dia': dia})
    return informacoes_eventos

url_minhaentrada = 'https://minhaentrada.com.br/'

url_poa_comedy_club = 'https://minhaentrada.com.br/PoaComedyClub'


soup_minhaentrada = fazer_web_scraping(url_minhaentrada)

soup_poa_comedy_club = fazer_web_scraping(url_poa_comedy_club)


informacoes_eventos_minhaentrada = extrair_informacoes_eventos(soup_minhaentrada)
informacoes_eventos_poa_comedy_club = extrair_informacoes_eventos(soup_poa_comedy_club)


def titulo(msg, traco="-"):
    print()
    print(msg)
    print(traco * 50)

def lista_pel(eventos_pelotas):
    titulo("Eventos de Pelotas")
    print("Nome do Evento........................: Data do Evento")
    for evento in eventos_pelotas:
        print(f"{evento['nome']:40s}   {evento['dia']}")

def lista_poa_comedy(eventos_poa_comedy):
    titulo("Eventos do Poa Comedy Club")
    print("Nome do Evento........................: Data do Evento")
    for evento in eventos_poa_comedy:
        print(f"{evento['nome']:40s}   {evento['dia']}")

def lista_todos_eventos(eventos):
    titulo("Todos os Eventos")
    print("Nome do Evento........................: Data do Evento")
    for evento in eventos:
        print(f"{evento['nome']:40s}   {evento['dia']}")

def apenas_pel():
    
    informacoes_pelotas = extrair_informacoes_eventos(soup_minhaentrada)
    informacoes_poa = extrair_informacoes_eventos(soup_poa_comedy_club)

    set_pel = set(evento['nome'] for evento in informacoes_pelotas)
    set_poa = set(evento['nome'] for evento in informacoes_poa)

    eventos_pelotas = set_pel.difference(set_poa)

    titulo("Eventos em Cartas: Apenas em Pelotas")

    if len(eventos_pelotas) == 0:
        print("Obs.: * Não há eventos em cartas apenas em Pelotas")
    else:
        for evento in informacoes_pelotas:
            if evento['nome'] in eventos_pelotas:
                print(f"{evento['nome']:40s}   {evento['dia']}")

def apenas_poa():
    informacoes_pelotas = extrair_informacoes_eventos(soup_minhaentrada)
    informacoes_poa = extrair_informacoes_eventos(soup_poa_comedy_club)

    set_pel = set(evento['nome'] for evento in informacoes_pelotas)
    set_poa = set(evento['nome'] for evento in informacoes_poa)

    eventos_poa = set_poa.difference(set_pel)

    titulo("Eventos em Cartas: Apenas em Poa")

    if len(eventos_poa) == 0:
        print("Obs.: * Não há eventos em cartas apenas em Poa")
    else:
        for evento in informacoes_poa:
            if evento['nome'] in eventos_poa:
                print(f"{evento['nome']:40s}   {evento['dia']}")

def eventos_comuns():
    informacoes_pelotas = extrair_informacoes_eventos(soup_minhaentrada)
    informacoes_poa = extrair_informacoes_eventos(soup_poa_comedy_club)

    set_pel = set(evento['nome'] for evento in informacoes_pelotas)
    set_poa = set(evento['nome'] for evento in informacoes_poa)

    eventos_comuns = set_pel.intersection(set_poa)

    titulo("Eventos em Cartas: Comuns entre Pelotas e Poa")

    if len(eventos_comuns) == 0:
        print("Obs.: * Não há eventos em cartas comuns entre Pelotas e Poa")
    else:
        for evento in informacoes_pelotas + informacoes_poa:
            if evento['nome'] in eventos_comuns:
                print(f"{evento['nome']:40s}   {evento['dia']}")

def listar_eventos_ordenados():
    informacoes_pelotas = extrair_informacoes_eventos(soup_minhaentrada)
    informacoes_poa = extrair_informacoes_eventos(soup_poa_comedy_club)

    todos_eventos = informacoes_pelotas + informacoes_poa
    todos_eventos.sort(key=lambda evento: evento['nome'])

    titulo("Eventos em Cartas: Todos (Ordenados)")

    if len(todos_eventos) == 0:
        print("Obs.: * Não há eventos em cartas em Pelotas e Poa")
    else:
        print("Nome do Evento........................: Data do Evento")
        for evento in todos_eventos:
            print(f"{evento['nome']:40s}   {evento['dia']}")

def totalizar_eventos():
    informacoes_pelotas = extrair_informacoes_eventos(soup_minhaentrada)
    informacoes_poa = extrair_informacoes_eventos(soup_poa_comedy_club)

    total_pelotas = len(informacoes_pelotas)
    total_poa = len(informacoes_poa)
    total_geral = total_pelotas + total_poa

    titulo("Total de Eventos")
    print(f"Total de Eventos em Pelotas: {total_pelotas}")
    print(f"Total de Eventos em Poa: {total_poa}")
    print(f"Total Geral de Eventos: {total_geral}")

def pesquisar_evento_por_nome(nome_evento):
    eventos_encontrados_pelotas = []
    eventos_encontrados_poa = []

    for evento in informacoes_eventos_minhaentrada:
        if nome_evento.lower() in evento['nome'].lower():
            eventos_encontrados_pelotas.append(evento)

    for evento in informacoes_eventos_poa_comedy_club:
        if nome_evento.lower() in evento['nome'].lower():
            eventos_encontrados_poa.append(evento)

    titulo("Eventos encontrados em Pelotas:")
    if len(eventos_encontrados_pelotas) > 0:
        for evento in eventos_encontrados_pelotas:
            print(f"{evento['nome']}   {evento['dia']}")
    else:
        print("Nenhum evento encontrado em Pelotas.")

    titulo("Eventos encontrados em Poa Comedy Club:")
    if len(eventos_encontrados_poa) > 0:
        for evento in eventos_encontrados_poa:
            print(f"{evento['nome']}   {evento['dia']}")
    else:
        print("Nenhum evento encontrado em Poa Comedy Club.")

#def agrupar_eventos_por_dia_semana(eventos):
 #   eventos_agrupados = {}
  #  for evento in eventos:
   #     dia_semana = evento['dia']
    #    if dia_semana not in eventos_agrupados:
     #       eventos_agrupados[dia_semana] = []
      #  eventos_agrupados[dia_semana].append(evento['nome'])

 #   return eventos_agrupados

    

def listar_eventos():
    print("1. Listar Eventos de Pelotas")
    print("2. Listar Eventos do Poa Comedy Club")
    print("3. Listar Todos os Eventos")
    print("4. Apenas em Pelotas")
    print("5. Apenas em Poa")
    print("6. Eventos comuns nas duas cidades")
    print("7. Listar eventos em ordem")
    print("8. Total de Eventos")
    print("9. Pesquisar Evento pelo nome")
    print("10. Agrupar Eventos por dia da semana")
    print("11. Sair")


while True:
    titulo("Eventos em Cartas - Minha Entrada")
    listar_eventos()
    opcao = int(input("Opção: "))

    if opcao == 1:
        lista_pel(informacoes_eventos_minhaentrada)
    elif opcao == 2:
        lista_poa_comedy(informacoes_eventos_poa_comedy_club)
    elif opcao == 3:
        lista_todos_eventos(informacoes_eventos_minhaentrada + informacoes_eventos_poa_comedy_club)
    elif opcao == 4:
        apenas_pel()
    elif opcao == 5:
        apenas_poa()
    elif opcao == 6:
        eventos_comuns()
    elif opcao == 7:
        listar_eventos_ordenados()
    elif opcao == 8:
        totalizar_eventos()
    elif opcao == 9:
        nome_evento = input("Digite o nome do evento a pesquisar: ")
        pesquisar_evento_por_nome(nome_evento)
    #elif opcao == 10:
       #()
    elif opcao == 11:
        print("Saindo do programa.")
        break

