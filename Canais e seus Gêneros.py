#pip install lxml + html5lib + beautifulsoup4
#Retorna os canais e seus gêneros correspondentes 


def canaisPorGeneros():
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
    print("Canais por Gêneros\n\n")
    for i in generosPorCanais:
        print(i+" -> "+str(generosPorCanais[i])+"\n")
    return generosPorCanais #retorna o dicionario de cada canal correspondente ao seu genero



def generosParaCadaCanal():#coloca cada canal canal da lista m3u em um gênero específico
    dicio = canaisPorGeneros()
    f = open('listaNova.txt','r') #Lista geral de canais IPTV ao Vivo

    vet = []

    for line in f:
        vet.append(line)
    f.close()


    aux=[]
    while(len(vet)!=0):
        flag=False
        for i in dicio:#i é o gênero
            if(flag):
                break
            for k in dicio[i]:#cada canal
                if(vet[0].lower().find(k.lower())!=-1):#se encontrar o canal em um determinado genero
                    flag=True
                    aux.append(vet[0][:10]+" "+"group-title=\""+i+"\""+vet[0][10:])
                    break
        if not flag:
            aux.append(vet[0])
        del(vet[0])


    f = open('listaNovaGenero.txt','w')#retorna a lista com canais e seus gêneros correspondentes
    for line in aux:
        f.write(line)
    f.close()


canaisPorGeneros()
