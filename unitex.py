import os
from os import path
if path.exists("corpus-medical_snt"):
    os.system("rd /s corpus-medical_snt")
os.mkdir("corpus-medical_snt")
os.system("UnitexToolLogger Normalize corpus-medical.txt -r Norm.txt")
os.system("UnitexToolLogger Tokenize corpus-medical.snt")
os.system("UnitexToolLogger Dico -t corpus-medical.snt Dela_fr.bin")
os.system("UnitexToolLogger Dico -t corpus-medical.snt Dela_fr.inf")
os.system("UnitexToolLogger Dico -t corpus-medical.snt subst.dic")
os.system("UnitexToolLogger Dico -t corpus-medical.snt subst.bin")
os.system("UnitexToolLogger Normalize -t corpus-medical.snt Alphabet.txt -r ")
os.system("UnitexToolLogger Grf2Fst2 posologie.grf")
os.system("UnitexToolLogger Locate -t corpus-medical.snt posologie.fst2 -L -I --all")
os.system("UnitexToolLogger Concord corpus-medical_snt/concord.ind -f \"Courrier new\" -s 12 -l 40 -r 55")

"""
"Alphabet.txt" est utilisé dans le script "unitex.py" de deux manières :

1.Lors de la tokenisation du fichier "corpus-medical.snt" avec la commande "Tokenize",
il est utilisé pour déterminer l'ensemble de caractères qui seront considérés comme des tokens individuels lors de la tokenisation.
Par exemple, si "Alphabet.txt" contient les lettres "a" à "z" et les chiffres de 0 à 9,
tous les mots composés uniquement de ces caractères seront traités comme des tokens lors de la tokenisation.

2.Lors de la création du dictionnaire à partir de "corpus-medical.snt" et de "subst.bin" avec la commande "Dico",
il est utilisé pour définir l'alphabet de caractères utilisé dans le fichier.
Cet alphabet est utilisé pour créer des automates de reconnaissance de mots à partir des tokens de "corpus-medical.snt" et du dictionnaire compressé "subst.bin".
Ces automates permettent de reconnaître les mots dans le texte et de les associer à leur forme normale,
ce qui peut être utile pour une analyse syntaxique ou sémantique ultérieure du texte.
"""