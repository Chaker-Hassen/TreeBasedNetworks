# -*- coding: utf-8 -*-
"""Complete_Test_Real_Data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1diqDQnFMXhIha37rlpIdUxxUxu-DDf3g
"""

from google.colab import files

files.upload()     # <================= Veuillez importer le fichier 'treebasednetworks.py'

pip install asymmetree

files.upload() # <================= Veuillez importer le fichier 'test1_species_tree.pkl'

import pickle as pkl

# Ouverture du fichier pickle 'test1_species_tree.pkl' en mode lecture binaire
file1 = open('/content/test1_species_tree.pkl', 'rb')

# Chargement des données du fichier pickle dans la variable 'species'
species = pkl.load(file1)

# Impression du contenu des données chargées (informations sur notre arbre)
print(species)

"""La variable 'species' qui est censée représenter notre arbre phylogénétique."""

files.upload() # <================= Veuillez importer le fichier 'test1_small_matrix.pkl'

# Ouverture du fichier pickle 'test1_small_matrix.pkl' en mode lecture binaire
file2 = open('/content/test1_small_matrix.pkl', 'rb')

# Chargement des données du fichier pickle dans la variable 'dic' (qui représente un dictionnaire)
dic = pkl.load(file2)

# Impression du contenu du dictionnaire chargé
print(dic)

# Calcul et impression du nombre d'éléments dans le dictionnaire ( en principe egale au nbr des feuilles de notre arbre species)
len(dic)

from treebasednetworks import *


# Définir le nombre de caractères
nbrCaractere= 23

# Initialisation du l'arbre species
tree_builder = TreeBuilder()
species=tree_builder.initialize_graph(species, nbrCaractere)

# Trouver le nœud racine (source) de l'arbre
root_id = [node for node in species.nodes() if species.in_degree(node) == 0]

# Ajouter des timestamps aux nœuds du species
timestamp_manager = TimestampManager()
species=timestamp_manager.add_timestamp(species,root_id[0])

# Affichage l'arbre species
tree_builder.drawGraph(species)

# Etiquettage des feuilles de l'arbre species depuis dic.pkl
labeler = LeafLabeler()
species= labeler.label_tree_leaves_species(species, nbrCaractere, dic)
labeler.display_leaf_labels(species)

#attributes = labeling_internal_nodes(species, attributes)

# Définition des attributs pour chaque nœud
attributes = labeler.set_leaf_attributes(species, nbrCaractere)

# ---------------------- Appeler la fonction TransferAdditionGreedy ----------------------
# Ajouter des transferts aux nœuds de l'arbre en fonction des attributs des nœuds afin de construire un Tree-Based Network PTN.
tree_networks = TreeBasedNetworks()
species, attributes = tree_networks.TransferAdditionGreedy(species, attributes)

# Affichage des attributs mis à jour après l'application des transferts
print(attributes)
# Affichage du notre TBN species avec les nouvelles arêtes
tree_builder.drawGraph(species)

# Affichage des timestamps des tous les nœuds du graphe
timestamp_manager.display_timestamps(species)

# Sauvegarde du notre TBN species dans un fichier pickle
file2= open('output_algo2.pkl','wb')
pkl.dump(species,file2)

"""
**Valider les résultats de l'algorithme 2 en utilisant l'algorithme 1.**"""

# Définition des attributs pour chaque nœud
attributes = labeler.set_leaf_attributes(species,nbrCaractere)

print("\n-------------------------------------")
print(attributes)
print("\n-------------------------------------")
# Liste des caractères à vérifier
C = [f'c{i+1}' for i in range(nbrCaractere)]

# Appel de la fonction findLabeling (Algo1)
tree_networks = TreeBasedNetworks()
l = tree_networks.findLabeling(species, attributes, C)

# Affichage le dictionnaire des attributs final
print("\n----------------- Attributs final --------------------")
print(attributes)
print("\n-------------------------------------")

# Affichage des timestamps des tous les nœuds du graphe
timestamp_manager.display_timestamps(species)

# G est le graphe mis à jour après l'ajout des transferts
transfer_manager = TransferManager()
transfers = transfer_manager.determine_transfers(species)

# Affichage des résultats
for transfer, source_leaves, target_leaves in transfers:
    source_node, target_node = transfer
    print(f"Transfert ({species.nodes[source_node]['number']}, {species.nodes[target_node]['number']}) ajputer caractere N°: {species.edges[source_node,target_node]['character']} :")
    print("  Feuilles atteignables par le nœud de départ :", {species.nodes[node]['number'] for node in source_leaves})
    print("  Feuilles atteignables par le nœud d'arrivée :", {species.nodes[node]['number'] for node in target_leaves})