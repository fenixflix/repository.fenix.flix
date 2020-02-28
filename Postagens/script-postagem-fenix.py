# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
# -*- Copyright © 2018-2020 ☫ Fênix Flix -*-
# -*- https://www.fenixflix.ml -*-

import requests
from bs4 import BeautifulSoup
import re

ids = input('Digite o codigo do Filme do TMDB e de Enter: ')
ids2 = str(ids)
#link = input('Digite o Link do Filme: ')

headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
url = "https://www.themoviedb.org/movie/"+ids2+"?language=pt-BR"

pagina_de_busca2 = requests.get(url,headers=headers)
soup = BeautifulSoup(pagina_de_busca2.text, "html.parser")
page = str(soup)

nome = soup.find_all('meta', attrs={'property': 'og:title'})
nome2 = str(nome)
sinopse = soup.find_all('meta', attrs={'property': 'og:description'})
sinopse2 =str(sinopse)
thumb = soup.find_all('meta', attrs={'property': 'og:image'})
thumb2 =str(thumb)
fanart = soup.find_all('div', attrs={'class': 'backdrop'})
fanart2 = str(fanart)
fanart3 = re.search('data-src(.*)',fanart2).group(0)
fanart4 = re.sub('" data-srcset=(.*)',r'',fanart3)

t1 = nome2.replace('[<meta content="','').replace('" property="og:title"/>]','')
t2 = sinopse2.replace('[<meta content="','').replace('" property="og:description"/>]','')
t3 = thumb2.replace('[<meta content="','').replace('" property="og:image"/>]','').replace('" property="og:image"/>, <meta content="','\n').replace('','')
t4 = fanart4.replace('data-src="','')

print("\n")
print("<item>")
print("<title>[B]"+t1+" l [COLOR orange]IMDb XX[/COLOR] l[/B]</title>")
print("<link>plugin://plugin.video.youtube/play/?video_id=$texto=Trailer</link>")
print("<link>plugin://plugin.video.gdrive?mode=streamURL&amp;url=https://drive.google.com/open?id=$texto=Filme</link>")
print("<thumbnail>"+t3+"</thumbnail>")
print("<fanart>"+t4+"</fanart>")
print("<info>[B][COLOR firebrick]l[/COLOR][/B] "+t2+" [B][COLOR firebrick]l[/COLOR][/B]</info>")
print("<genre>""</genre>")
print("</item>")
print("\n")
