#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import unidecode

src_adherents = 'data-test/import_adherents_2017.csv'
src_relations = 'data-test/import_relations_2017.csv'

def findId(adherents, adherent):
    id = False
    nom = adherent['nom']
    prenom = adherent['prenom']
    if nom in adherents:
        if prenom in adherents[nom]:
            id = adherents[nom][prenom]
    return id

def simplifyStr(str):
    return unidecode.unidecode(str.lower().strip())

adherents = {}
with open(src_adherents, encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        id = int(row['id_adh'])
        nom = simplifyStr(row['nom_adh'])
        prenom = simplifyStr(row['prenom_adh'])
        # ajout nom ?
        if not nom in adherents:
            adherents[nom] = {}
        if not prenom in adherents[nom]:
            adherents[nom][prenom] = id

relations = []
with open(src_relations, encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        relation = {
            'parrain': {
                'nom': simplifyStr(row['nom_p']),
                'prenom': simplifyStr(row['prenom_p'])
            },
            'fillot': {
                'nom': simplifyStr(row['nom_f']),
                'prenom': simplifyStr(row['prenom_f'])
            }
        }
        relations.append(relation)

insert_sql = "INSERT INTO `galette_aae_visage_relation`(`parrain`, `fillot`) VALUES ({0}, {1})"
erreur_fillot = "-- {0} {1}, {2} {3}; fillot introuvable"
erreur_parrain = "-- {0} {1}, {2} {3}; parrain introuvable"
erreur_couple = "-- {0} {1}, {2} {3}; aucun trouvable"

total = 0
ok = 0

for relation in relations:
    total += 1
    id_parrain = findId(adherents, relation['parrain'])
    id_fillot = findId(adherents, relation['fillot'])

    if id_parrain and id_fillot:
        ok += 1
        print(insert_sql.format(id_parrain, id_fillot))
    else:
        if id_parrain:
            print(erreur_fillot.format(relation['parrain']['prenom'], relation['parrain']['nom'], relation['fillot']['prenom'], relation['fillot']['nom']))
        elif id_fillot:
            print(erreur_parrain.format(relation['parrain']['prenom'], relation['parrain']['nom'], relation['fillot']['prenom'], relation['fillot']['nom']))
        else:
            print(erreur_couple.format(relation['parrain']['prenom'], relation['parrain']['nom'], relation['fillot']['prenom'], relation['fillot']['nom']))

print("-- {0} / {1}".format(ok, total))
