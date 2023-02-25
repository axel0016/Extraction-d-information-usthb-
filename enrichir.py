import sys
import re

if len(sys.argv) < 2:
    print('erreur add arg')
else:
    extra=[]
    lettres='abcdeéfghijklmnopqrstuvwxyz'
    f1 = open(str(sys.argv[1]), 'r', encoding='UTF-8')

    x=f1.readlines()

    for i in x:
        reg = re.search(r'''
        ^[-*Ø]?\s?  
        (\w+)      
        \s:?\s?     
        (\d+|,|\d+.\d)+
        \s?:?   
        (\s(mg\s|MG|UI|ml|mcg|amp|iu|flacon|g|sachet|un\s|1/j|/j)(.+|\n)|(g|/j)\n|(mg)\s.+)
        ''', i, re.VERBOSE | re.I)    
        if reg :
                if  reg.group(1).lower() != 'vichy' \
                        and reg.group(1).lower() != 'mdz' \
                        and reg.group(1).lower() != 'vvp' \
                        and reg.group(1).lower() != 'hémoglobine' \
                        and reg.group(1).lower() != 'aspegic'  \
                        and reg.group(1).lower() != 'kt' \
                        and reg.group(1).lower() != 'le' \
                        and reg.group(1).lower() != 'puis':
                    extra.append(reg.group(1).lower()+',.N+subst'+'\n')
    for i in x:
        reg=re.search('((vitamine|VITAMINE|Vitamine) [A-Za-b](\d| \d)*)',i)
        if reg:
            extra.append(reg.group(1).lower()+',.N+subst'+'\n')

    f1.close()
    p=open('subst_corpus.dic','w',encoding='UTF-16 LE') 
    p.write('\ufeff')  
    for i in extra:
        p.write(i)
    extra = sorted(list(set(extra)))

    s = 0
    c = 0

    f3 = open('infos2.txt', 'w', encoding='UTF-8')

    for lettre in lettres:
        for ext in extra:
            if ext[0] == lettre:
                f3.write(ext)
                c += 1
        f3.write('-'*100+'\n')
        f3.write(f'total de {lettre}:{str(c)} \n')
        f3.write('-'*100+'\n')
        s += c
        c = 0
     
    f3.write(f'le nombre total de médicaments issus du corpus:{s} \n')
    f3.close()

    f=open('subst.dic','r',encoding='utf-16')
    inf3=open('infos3.txt','w',encoding='UTF-8')

    sub=f.readlines()

    sub=sorted(list(set(sub)))
    s=0
    for let in lettres:
        for r in extra:
            if r[0]==let:
                if r not in sub:
                    inf3.write(r)
                    c+=1
        inf3.write('-'*100+'\n')
        inf3.write(f'pour {let}:{str(c)}\n')
        inf3.write('-'*100+'\n')
        s+=c
        c=0   

    inf3.write(f'nombre total de médicaments conservés pour l’enrichissement:{s}')

    f3 = open('subst.dic', 'r', encoding='utf-16')
    x = f3.readlines()

    for i in x:
        if i not in extra:
            extra.append(i)

    extra = sorted(list(set(extra)))
    f3.close()
    f3 = open('subst.dic', 'w', encoding='utf-16')
    f3.write('\ufeff')
    for e in extra:
        f3.write(e)
    f3.close()
