#pip install lxml + html5lib + beautifulsoup4
#Retorna os canais e seus gêneros correspondentes 

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://pt.wikipedia.org/wiki/Lista_de_canais_dispon%C3%ADveis_na_televis%C3%A3o_por_assinatura_do_Brasil")
res = BeautifulSoup(html.read(),"html5lib");
tags = res.findAll("span",{"class":"mw-headline"})#filtrar todos os elementos span cuja classe é “mw-headline”

del(tags[0])
tags = tags[:-10]#Pega somente os canais por Gênero

generos = []

for tag in tags:
    generos.append(tag.getText())#a função getText  é usada para imprimir apenas o conteúdo interno da tag

html = urlopen("https://raw.githubusercontent.com/joaomota59/IPTV/main/canais%20por%20g%C3%AAnero.txt")
res = BeautifulSoup(html.read(),"html5lib");
todos = res.getText().split('\n')

generosPorCanais = {}#dicionario com canais por seus gêneros
nomeGenero = ""

for i in todos:
    try:
        generos.index(i)
        nomeGenero = i
    except:#se não encontrar gera exceção
        try:
            generosPorCanais[nomeGenero].append(i)
        except:#se não houver nenhum canal adicionado ainda para aquele genero
            generosPorCanais[nomeGenero] = [i]

print("Canais Classificados por gêneros\n\n")

for i in generosPorCanais:
    print(i+" -> "+str(generosPorCanais[i])+"\n")

