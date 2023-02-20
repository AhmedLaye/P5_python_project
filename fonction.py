import csv

import re

from fonction import *
with open('data.csv','r') as file:

        data = csv.DictReader(file)
        data_dict=list(data)
from datetime import date, time, datetime
valid=[]
invalid=[]


invalid_date=[]


invalid_classe=[]

valid_numero=[]
invalid_numero=[]
invalid_pnom=[]
invalid_nom=[]
invalid_note=[]
ligne_vide=[]


    

def remove_esp(data_dict):
    for eleve in data_dict:
        if len(eleve)==0:
            data_dict.remove(eleve)

class_list=['6','5','4','3','A','B']    
def info_valid(eleve):
    if teste_num(eleve['Numero'])==True and teste_nom(eleve['Nom'])==True and teste_pnom(eleve['Prénom'])==True and        is_valid_date(eleve['Date de naissance'])==True and teste_note(eleve['Note']) == True and teste_classe(eleve['Classe'])==True:
        return True

def teste_nom(nom):
    if len(nom)<2 or nom.isalpha()==False:
        return False
    else:
        return True


def teste_pnom(pnom):

    if len(pnom) <3 and pnom.isalpha()==False:
        return False

    else:
        return True

def changer_format_date(data_dict):
    for eleve in range(len(data_dict)):
        date=data_dict[eleve]['Date de naissance']
        for item in date:
            if item.isnumeric()==False:
                date=date.replace(item,'-')
            data_dict[eleve].update({'Date de naissance':date})


def is_valid_date(dat):
    from datetime import date, time, datetime
    try:
        date_obj = datetime.strptime(dat, '%d-%m-%y')
        return True
    except ValueError:
        pass
    try:
        date_obj = datetime.strptime(dat, '%d-%m-%Y')
        return True
    except:
        return False


def format_class(data_dict):    
    for eleves in data_dict:
        if len(eleves):
            for key,value in eleves.items():
                if len(eleves['Classe'])>1:
                    eleves['Classe']=eleves['Classe'].replace(' ','')
                    eleves.update({'Classe': eleves['Classe'][0]+eleves['Classe'][len(eleves['Classe'])-1]})
                elif len(eleves['Classe'])==2:
                    pass


def teste_classe(classe):
    if len(classe)==2:
        if classe[0] in class_list and classe[1] in class_list :
            return True
        else:
            return False
    else:
        return False  

def teste_num(num):
        if len(num) ==7 and num.isalnum()==True and num.isupper()==True:
            return True
        else:
            return False

def par_note(data_dict):
    for eleve in range(len(data_dict)):
        matiere=data_dict[eleve]['Note']
        matiere=matiere.replace(' ','')
        matiere=matiere.replace('"', '')
        matiere=matiere.split("#")
        for i in matiere:
            if i=='':
                matiere.remove(i)
        matiere_dict={}
        for i in range(len(matiere)):
            note_m=''
            for j in matiere[i].capitalize().split("["):
                matiere_dict[j]=[]
                for k in matiere[i].split("[")[1]:
                    if k.isnumeric() or k==',' or k=='.' and k!='':
                        note_m+=k
                    else:
                        matiere_dict[j].append(note_m)
                        note_m=''
                break
        data_dict[eleve].update({'Note':matiere_dict})

def teste_note(note):
    if len(note) !=6:
        return False
    else:
        return True

def premier_tri(data_dict):
    for eleve in data_dict:
        if teste_num(eleve['Numero'])==True and teste_nom(eleve['Nom'])==True and teste_pnom(eleve['Prénom'])==True and is_valid_date(eleve['Date de naissance'])==True and teste_note(eleve['Note']) == True and teste_classe(eleve['Classe'])==True:
            valid.append(eleve)
        else:
            invalid.append(eleve)
    

def affiche_valid():
    print("|{:<15}|{:<15}|{:<15}|{:<10}|{:<15}|{:<15}".format("CODE", "Numero", "Prénom", "Nom", "Date de naissance", "Classe"))
    print("|{:-<15}|{:-<15}|{:-<15}|{:-<10}|{:-<15}|{:-<10}|".format("", "", "", "", "", "", ""))
    for eleve in valid:
        print("|{:<15}|{:<15}|{:<15}|{:<10}|{:<15}|{:<10}|".format(eleve["CODE"], eleve["Numero"], eleve["Prénom"], eleve["Nom"], eleve["Date de naissance"], eleve["Classe"]))


# In[1297]:

def affiche_invalid():
    print("|{:<15}|{:<15}|{:<15}|{:<10}|{:<15}|{:<15}".format("CODE", "Numero", "Prénom", "Nom", "Date de naissance", "Classe"))
    print("|{:-<15}|{:-<15}|{:-<15}|{:-<10}|{:-<15}|{:-<10}|".format("", "", "", "", "", "", ""))
    for eleve in invalid:
        print("|{:<15}|{:<15}|{:<15}|{:<10}|{:<15}|{:<10}|".format(eleve["CODE"], eleve["Numero"],           
eleve["Prénom"], eleve["Nom"], eleve["Date de naissance"], eleve["Classe"]))


# In[1298]:



# In[1299]:

def trier_invalid(invalid):
    for eleve in invalid:
        if teste_num(eleve['Numero'])==False and teste_nom(eleve['Nom'])==True and teste_pnom(eleve['Prénom'])==True and is_valid_date(eleve['Date de naissance'])==True and teste_note(eleve['Note']) == True and teste_classe(eleve['Classe'])==True:
            invalid_numero.append(eleve)
        if teste_num(eleve['Numero'])==True and teste_nom(eleve['Nom'])==False and teste_pnom(eleve['Prénom'])==True and is_valid_date(eleve['Date de naissance'])==True and teste_note(eleve['Note']) == True and teste_classe(eleve['Classe'])==True:
            invalid_nom.append(eleve)
        if teste_num(eleve['Numero'])==True and teste_nom(eleve['Nom'])==True and teste_pnom(eleve['Prénom'])==False and  is_valid_date(eleve['Date de naissance'])==True and teste_note(eleve['Note']) == True and teste_classe(eleve['Classe'])==True:
            invalid_pnom.append(eleve)
        if teste_num(eleve['Numero'])==True and teste_nom(eleve['Nom'])==True and teste_pnom(eleve['Prénom'])==True and not is_valid_date(eleve['Date de naissance'])==True and teste_note(eleve['Note']) == True and teste_classe(eleve['Classe'])==True:
            invalid_date.append(eleve)
        if teste_num(eleve['Numero'])==True and teste_nom(eleve['Nom'])==True and teste_pnom(eleve['Prénom'])==True and is_valid_date(eleve['Date de naissance'])==True and teste_note(eleve['Note']) == False and teste_classe(eleve['Classe'])==True:
            invalid_note.append(eleve)
        if teste_num(eleve['Numero'])==True and teste_nom(eleve['Nom'])==True and teste_pnom(eleve['Prénom'])==True and is_valid_date(eleve['Date de naissance'])==True and teste_note(eleve['Note']) == True and teste_classe(eleve['Classe'])==False:
            invalid_classe.append(eleve)
        if len(eleve)==0:
            ligne_vide.append(eleve)


def invalid_numero():
    print("|{:<15}|{:<15}|{:<15}|{:<10}|{:<15}|{:<15}".format("CODE", "Numero", "Prénom", "Nom", "Date de naissance", "Classe"))
    print("|{:-<15}|{:-<15}|{:-<15}|{:-<10}|{:-<15}|{:-<10}|".format("", "", "", "", "", "", ""))
    for eleve in invalid_numero:
        print("|{:<15}|{:<15}|{:<15}|{:<10}|{:<15}|{:<10}|".format(eleve["CODE"], eleve["Numero"], eleve["Prénom"], eleve["Nom"], eleve["Date de naissance"], eleve["Classe"]))


# In[1301]:

def invalid_date():
    print("|{:<15}|{:<15}|{:<15}|{:<10}|{:<15}|{:<15}".format("CODE", "Numero", "Prénom", "Nom", "Date de naissance", "Classe"))
    print("|{:-<15}|{:-<15}|{:-<15}|{:-<10}|{:-<15}|{:-<10}|".format("", "", "", "", "", "", ""))
    for eleve in invalid_date:
        print("|{:<15}|{:<15}|{:<15}|{:<10}|{:<15}|{:<10}|".format(eleve["CODE"], eleve["Numero"], eleve["Prénom"], eleve["Nom"], eleve["Date de naissance"], eleve["Classe"]))


# In[1302]:

def invalid_classe():
    print("|{:<15}|{:<15}|{:<15}|{:<10}|{:<15}|{:<15}".format("CODE", "Numero", "Prénom", "Nom", "Date de naissance", "Classe"))
    print("|{:-<15}|{:-<15}|{:-<15}|{:-<10}|{:-<15}|{:-<10}|".format("", "", "", "", "", "", ""))
    for eleve in invalid_classe:
        print("|{:<15}|{:<15}|{:<15}|{:<10}|{:<15}|{:<10}|".format(eleve["CODE"], eleve["Numero"], eleve["Prénom"], eleve["Nom"], eleve["Date de naissance"], eleve["Classe"]))


# In[1303]:

def invalid_note():
    print("|{:<15}|{:<15}|{:<15}|{:<10}|{:<15}|{:<15}".format("CODE", "Numero", "Prénom", "Nom", "Date de naissance", "Classe"))
    print("|{:-<15}|{:-<15}|{:-<15}|{:-<10}|{:-<15}|{:-<10}|".format("", "", "", "", "", "", ""))
    for eleve in invalid_note:
        print("|{:<15}|{:<15}|{:<15}|{:<10}|{:<15}|{:<10}|".format(eleve["CODE"], eleve["Numero"], eleve["Prénom"], eleve["Nom"], eleve["Date de naissance"], eleve["Classe"]))


# In[1307]:

def ligne_vide():
    print("|{:<15}|{:<15}|{:<15}|{:<10}|{:<15}|{:<15}".format("CODE", "Numero", "Prénom", "Nom", "Date de naissance", "Classe"))
    print("|{:-<15}|{:-<15}|{:-<15}|{:-<10}|{:-<15}|{:-<10}|".format("", "", "", "", "", "", ""))
    for eleve in ligne_vide:
        print("|{:<15}|{:<15}|{:<15}|{:<10}|{:<15}|{:<10}|".format(eleve["CODE"], eleve["Numero"], eleve["Prénom"], eleve["Nom"], eleve["Date de naissance"], eleve["Classe"]))

def rechercher(invalid):
    modifier=''
    recherche = input("entrer le numero de l'eleve à rechercher: ")
    for eleve in invalid:
        if recherche in eleve.values():
            
            print("|{:<15}|{:<15}|{:<15}|{:<10}|{:<15}|{:<15}".format("CODE", "Numero", "Prénom", "Nom", "Date de naissance", "Classe"))
            print("|{:-<15}|{:-<15}|{:-<15}|{:-<10}|{:-<15}|{:-<10}|".format("", "", "", "", "", "", ""))
            print("|{:<15}|{:<15}|{:<15}|{:<10}|{:<15}|{:<10}|".format(eleve["CODE"], eleve["Numero"], eleve["Prénom"],                     eleve["Nom"], eleve["Date de naissance"], eleve["Classe"]))
            modifier=input("voulez vous modifiez 'o/n'")
            if modifier=='o':
                print("modification")
#                 eleve.update({eleve["CODE"]:input("entrer le code ")})
                eleve.update({eleve["Numero"]:input("entrer le numero")})
                eleve.update({eleve["Prénom"]:input("entrer le prénom")})
                eleve.update({eleve["Nom"]:input("entrer le nom")})
                eleve.update({eleve["Date de naissance"]:input("entrer la date de naissance")})
                eleve.update({eleve["Classe"]:input("Entrer la classe ")})
            if teste_num(eleve['Numero'])==True and teste_nom(eleve['Nom'])==True and teste_pnom(eleve['Prénom'])==True and is_valid_date(eleve['Date de naissance'])==True and teste_note(eleve['Note']) == True and teste_classe(eleve['Classe'])==True:
                valid.append(eleve)
                print("|{:<15}|{:<15}|{:<15}|{:<10}|{:<15}|{:<15}".format("CODE", "Numero", "Prénom", "Nom", "Date de naissance", "Classe"))
                print("|{:-<15}|{:-<15}|{:-<15}|{:-<10}|{:-<15}|{:-<10}|".format("", "", "", "", "", "", ""))
                print("|{:<15}|{:<15}|{:<15}|{:<10}|{:<15}|{:<10}|".format(eleve["CODE"], eleve["Numero"], eleve["Prénom"],                     eleve["Nom"], eleve["Date de naissance"], eleve["Classe"]))
            else:
                print("des infos semblent rester invalide")

 
        
format_class(data_dict)
changer_format_date(data_dict)
changer_format_date(data_dict)
par_note(data_dict)
premier_tri(data_dict)

def menu():
    
        
        print("""
         ----------------------------------------------------------------
        |⏩ ⏩ ⏩ ⏩ ⏩ ⏩ ⏩ ⏩ ⏩  MENU ⏩ ⏩ ⏩ ⏩ ⏩ ⏩ ⏩ ⏩ ⏩ ⏩ |
         ----------------------------------------------------------------
         1️⃣: Afficher les Infos taper "V ou I" pour afficher
         2️⃣: Afficher les Infos d'un eleve
         3️⃣: Afficher les Cinq Premier
         4️⃣: Ajouter un infos
         5️⃣: Modifier des informations Invalide
         ----------------------------------------------------------------
        """)
        choix=input("entrer votre Choix ")
        print("\n")
        if choix=="v" or choix=="V":
            print("""
         ----------------------------------------------------------------
        |⏩ ⏩ ⏩ ⏩ ⏩ ⏩ ⏩⏩  LIST VALID  ⏩ ⏩ ⏩ ⏩ ⏩ ⏩ ⏩ |
         ---------------------------------------------------------------
        """)
            affiche_valid()
        elif choix=="i" or choix=="I":
            print("""
         ----------------------------------------------------------------
        |⏩ ⏩ ⏩ ⏩ ⏩ ⏩ ⏩⏩  LIST INVALID  ⏩ ⏩ ⏩ ⏩ ⏩ ⏩ ⏩ |
         ----------------------------------------------------------------
        """)
            print("|{:<15}|{:<15}|{:<15}|{:<10}|{:<15}|{:<15}".format("CODE", "Numero", "Prénom", "Nom", "Date de naissance", "Classe"))
            print("|{:-<15}|{:-<15}|{:-<15}|{:-<10}|{:-<15}|{:-<10}|".format("", "", "", "", "", "", ""))
            for eleve in invalid:
                print("|{:<15}|{:<15}|{:<15}|{:<10}|{:<15}|{:<10}|".format(eleve["CODE"], eleve["Numero"], eleve["Prénom"], eleve["Nom"], eleve["Date de naissance"], eleve["Classe"]))
        if choix =="2":
            print("""
         ----------------------------------------------------------------
        |⏩ ⏩ ⏩ ⏩ ⏩ ⏩ ⏩⏩  LIST INVALID NUMERO ⏩ ⏩ ⏩ ⏩ ⏩ ⏩ ⏩ |
         ----------------------------------------------------------------
        """)
            print("|{:<15}|{:<15}|{:<15}|{:<10}|{:<15}|{:<15}".format("CODE", "Numero", "Prénom", "Nom", "Date de naissance", "Classe"))
            print("|{:-<15}|{:-<15}|{:-<15}|{:-<10}|{:-<15}|{:-<10}|".format("", "", "", "", "", "", "",""))
            for eleve in data_dict:
                print("|{:<15}|{:<15}|{:<15}|{:<10}|{:<15}|{:<10}|".format(eleve["CODE"], eleve["Numero"], eleve["Prénom"], eleve["Nom"], eleve["Date de naissance"], eleve["Classe"]))
        if choix =="3":
            print("""
         ----------------------------------------------------------------
        |⏩ ⏩ ⏩ ⏩ ⏩ ⏩ ⏩⏩  LIST 5 PREMIERS INFOS ⏩ ⏩ ⏩ ⏩ ⏩ ⏩ ⏩ |
         ----------------------------------------------------------------
        """)
            print("|{:<15}|{:<15}|{:<15}|{:<10}|{:<15}|{:<15}".format("CODE", "Numero", "Prénom", "Nom", "Date de naissance", "Classe"))
            print("|{:-<15}|{:-<15}|{:-<15}|{:-<10}|{:-<15}|{:-<10}|".format("", "", "", "", "", "", ""))
            for eleve in data_dict[:5]:
                print("|{:<15}|{:<15}|{:<15}|{:<10}|{:<15}|{:<10}|".format(eleve["CODE"], eleve["Numero"], eleve["Prénom"], eleve["Nom"], eleve["Date de naissance"], eleve["Classe"]))

        if choix == "4":
            valider=''
            new_eleve={}

            new_eleve["CODE"]=input("entrer le code ")
            new_eleve["Numero"]=input("entrer le numero")
            new_eleve["Prénom"]=input("entrer le prénom")
            new_eleve["Nom"]=input("entrer le nom")
            new_eleve["Date de Naissance"]=input("entrer la date de naissance")
            new_eleve["Classe"]=input("Entrer la classe ")
            
#             if info_valid(new_eleve)==True:
            valider=input("verifier puis 'o' pour ajouter er 'n' pour annuler")
            print("|{:<15}|{:<15}|{:<15}|{:<10}|{:<15}|{:<15}".format("CODE", "Numero", "Prénom", "Nom", "Date de naissance", "Classe"))
            print("|{:-<15}|{:-<15}|{:-<15}|{:-<10}|{:-<15}|{:-<10}|".format("", "", "", "", "", "", ""))
            print("|{:<15}|{:<15}|{:<15}|{:<10}|{:<15}|{:<10}|".format(eleve["CODE"], eleve["Numero"], eleve["Prénom"],                     eleve["Nom"], eleve["Date de naissance"], eleve["Classe"]))
            if valider =='o':
                valid.append(eleve)
            else:
                pass

        if choix == "5":
            rechercher(invalid)
            
        
        menu()
        