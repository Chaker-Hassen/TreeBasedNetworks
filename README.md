# Projet TreeBasedNetworks

Bienvenue dans le projet TreeBasedNetworks ! Ce dépôt contient du code et des exemples liés aux modèles basés sur les arbres. Notre objectif est de fournir une plateforme où vous pouvez explorer et expérimenter avec différentes techniques de construction et d'optimisation de réseaux phylogénétiques à partir d'arbres

## Pour commencer

Pour commencer avec le projet, suivez ces étapes :
1. Clonez le dépôt. git clone `https://github.com/Chaker-Hassen/TreeBasedNetworks.git`
2. Installez les dépendances nécessaires.
3. Explorez les exemples dans le répertoire `examples` pour comprendre comment utiliser les fonctionnalités du projet.

Vous pouvez également exécuter les exemples directement en utilisant Google Colab.

## Dépendances
* [NetworkX](https://networkx.github.io/)
* [Matplotlib](https://matplotlib.org/)
* [AsymmeTree](https://github.com/david-schaller/AsymmeTree)
  
## Fichiers
* Données :
  * `output_algo2.pkl` : Fichier de sortie contenant le graphe résultant de l'algorithme 2.
  * `test1_small_matrix.pkl` : Fichier d'entrée contenant une petite matrice de test.
  * `test1_species_tree.pkl` : Fichier d'entrée contenant un arbre phylogénétique de test.
* Code source :
  * `treebasednetworks.py` : Le fichier de code source principal contenant les classes et fonctions du projet.

## Fonctionnalités
Notre projet offre plusieurs fonctionnalités pour construire, optimiser et analyser les réseaux phylogénétiques. Vous pouvez explorer différentes méthodes et algorithmes à travers nos exemples illustratifs.

## Exemples
Consultez le répertoire examples pour des démonstrations détaillées de la manière d'utiliser nos modèles dans différents scénarios:
1. **Scénario 1 - Construction d'un Tree-Based Network avec l'algorithme 2 :**
   - Fichier : `Tree_specific_Algorithme_2.py`
   - Description : Ce fichier illustre la manière de construire un réseau basé sur les arbres (Tree-Based Network) en utilisant l'algorithme 2. Il charge un arbre phylogénétique au format Newick, ajoute des attributs aux nœuds, effectue des transferts de caractères entre les nœuds, et sauvegarde le graphe résultant dans un fichier pickle.
2. **Scénario 2 - Génération d'un arbre aléatoire et application de l'algorithme 2 :**
   - Fichier : `Random_Tree_Algorithme_2.py`
   - Description : Ce fichier illustre comment générer un arbre phylogénétique aléatoire avec un nombre spécifié de feuilles, puis appliquer l'algorithme 2 pour construire un réseau basé sur les arbres (Tree-Based Network) en utilisant l'algorithme 2. Il démontre les étapes pour ajouter des attributs, effectuer des transferts de caractères entre les nœuds et sauvegarder le résultat dans un fichier pickle.
3. **Scenario 3 - Génération d'un graphe Non-PTN et Vérification avec l'algorithme 1 :**
   - Fichier : `Generation_NON-PTN_Test_Algo1.py`
   - Description : Ce fichier illustre comment générer un graphe Non-PTN à partir d'un arbre ainsi que la vérification que le graphe est effectivement Non-PTN (c'est-à-dire qu'aucun étiquetage possible n'est réalisable) en appliquant l'algorithme 1. Il expose les étapes requises pour construire un graphe Non-PTN en étiquetant les feuilles, en introduisant des transferts aléatoires et en entreprenant la recherche d'un étiquetage possible pour le réseau.
4. **Scenario 4 - Génération et Vérification d'un graphe PTN avec l'algorithme 1 :**
   - Fichier : `Generation_PTN_Test_Algo1.py`
   - Description : Ce fichier démontre la génération d'un graphe PTN (Tree-Based Network) à partir d'un arbre. Il présente les étapes pour construire un graphe PTN en ajoutant des branches de transfert, en étiquetant les feuilles et en vérifiant la possibilité d'étiquetage du réseau en utilisant l'algorithme 1.
5. **Scenario 5 - Test Complet avec Données Réelles :**
   - Fichier : `Complete_Test_Real_Data.py`
   - Description : Ce fichier représente un test complet utilisant des données réelles. Il charge des arbres d'espèces et des matrices à partir de fichiers pickle, puis effectue des opérations telles que l'initialisation de l'arbre, l'ajout de timestamp, l'étiquetage des feuilles, l'ajout de transferts à l'aide de l'algorithmes 2 et confirme que notre réseau se transforme en PTN en vérifiant la faisabilité de l'étiquetage grâce à l'algorithme 1. Ce scénario illustre comment utiliser l'ensemble des fonctionnalités de l'outil TreeBasedNetworks sur des données réelles.
6. **Scenario 6 - Méthode Heuristique pour Éliminer les Transferts :**
   - Fichier : `Heurostique.py`
   - Description : Ce fichier présente deux méthodes heuristiques pour traiter les transferts dans le réseau. La première méthode trie les transferts selon le timestamp, et la deuxième méthode effectue 10 itérations de transferts aléatoires pour atteindre la meilleur resultat possible. Ces méthodes illustrent diverses approches pour optimiser le réseau en éliminant les transferts superflus tout en préservant son caractère de Réseau Phylogénétique (PTN).

## Statut du projet
En développement actif.
