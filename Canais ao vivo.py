#transformar primeiramente lista m3u em txt!
f = open('listaM3U.txt','r') #Lista geral de canais IPTV com filmes/series/canais 24H/ mineração apenas para canais ao vivo

vet = []

with open('listaM3U.txt', encoding='utf-8') as f:#converter antes a lista m3u em txt!
    for line in f:
        vet.append(line)
f.close()

vetaux=[]
flag24=False
for i in vet:
    if i=='\n':
        break
    if flag24:
        del(vetaux[-1])
        flag24=False
    if not i.find("[24H]") == -1:
        print(i)
        flag24 = True
    elif i.find('.mp4') == -1 and i.find('.avi') == -1 and i.find('.mkv') == -1:#retira todos canais de filmes/series da lista
        vetaux.append(i)
    else:
        del(vetaux[-1])


f = open('listaNova.txt','w') #retorna a lista em txt dps tem que converter novamente para m3u

for line in vetaux:
    f.write(line)
f.close()
