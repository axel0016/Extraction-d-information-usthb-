
import sqlite3
from bs4 import BeautifulSoup
i = open('corpus-medical_snt\\concord.html', 'r', encoding='utf-8').read()
soup = BeautifulSoup(i, features="html.parser")
a = soup.findAll('a')
tab=[]
for i in a:
    v = i.text 
    tab.append(v)

conct = sqlite3.connect('extraction.db')
cur = conct.cursor()
cur.execute("DROP TABLE IF EXISTS extraction")
cur.execute("create table if not exists extraction ( ID INTEGER PRIMARY KEY, Posologie TEXT )")
cur.executemany("INSERT INTO extraction(Posologie) VALUES(?)",
                [(x,) for x in tab])
cur.execute('select * from extraction')
print(cur.fetchall())

conct.commit()
cur.close()
conct.close()
