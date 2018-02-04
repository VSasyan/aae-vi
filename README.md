# Importation des relations Visage


## Fichier des adhérents

Fichier CSV à exporter de la base en CSV.

Doit contenir une *en-tête* et au moins les colonnes :
* `id_adh` : identifiant adhérent ;
* `nom_adh` : nom adhérent ;
* `prenom_adh` : prénom adhérent.

Exemple : [data-test/import_adherents_2017.csv](test-data/import_adherents_2017.csv)


## Fichier des adhérents

Fichier CSV contenant les relations à ajouter. A écrire.

Doit contenir une *en-tête* et les 4 colonnes :
* `nom_p` : nom du parrain ;
* `prenom_p` : prénom du parrain ;
* `nom_f` : nom du fillot ;
* `prenom_f` : prénom du fillot.

Exemple : [data-test/import_relations_2017.csv](test-data/import_relations_2017.csv)


## Utilisation

Il faut modifier dans le script les adresses vers les fichiers à traiter, puis lancer :

```sh
python3 vi.py
```

## Sortie du test

Voici la sortie attendue avec les fichiers de test :

```
INSERT INTO `galette_aae_visage_relation`(`parrain`, `fillot`) VALUES (1, 2)
-- parrainprenom parrainnom, erreur1 erreur; fillot introuvable
-- erreur2 erreur, fillotprenom fillotnom; parrain introuvable
-- erreur3 albert, erreur4 marie; aucun trouvable
-- 1 / 4
```


## TODO

Passer les adresses des fichiers en paramètre...
