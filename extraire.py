import requests
from bs4 import BeautifulSoup
import sys


if len(sys.argv)<3:
    print('erreur add arg')
else:
    
    url = f'http://127.0.0.1:{str(sys.argv[2])}/vidal/'
    links = []
    substances = []
    fiche = open('subst.dic', 'w', encoding='utf-16 LE')
    fiche1 = open('infos1.txt', 'w', encoding='utf-8 ')
    fiche.write('\ufeff')
    fiche1.write('\ufeff')
    interval = sys.argv[1]
    lettres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    x = interval.split('-')
    deb = lettres.index(x[0])
    fin = lettres.index(x[1])

    for i in range(deb, fin+1):
        links.append(
            f'http://127.0.0.1:{str(sys.argv[2])}/vidal/vidal-Sommaires-Substances-{lettres[i]}.html')
        print(f'URL ==> {str( links[i])} \n') 
              
    c = 0
    s = 0
    for link in links:
        url = link
        reponse = requests.get(url)
        if reponse.ok:
            soup = BeautifulSoup(reponse.content, 'html.parser')
            uliste = soup.findAll(
                'ul', {'class': 'substances list_index has_children'})
            for ul in uliste:
                liste = ul.findAll('li')
                for li in liste:
                    a = li.findAll('a')
                    for i in a:
                        car = i.text
                        fiche.write(car+',.N+subst'+'\n')
                        c += 1
            fiche1.write(f'pour {lettres[deb]}:'+str(c)+'\n')
            deb += 1
            s += c
            c = 0

    fiche1.write(f'la somme est:'+str(s)+'\n')
    fiche1.close()
    fiche.close()
