# -*- coding: utf-8 -*-
"""Generation_NON-PTN_Test_Algo1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15KZ8Kine8qv5uJIZvMnNDyl4OwVjy_9k
"""

from google.colab import files

files.upload()  # <================= Veuillez importer le fichier 'treebasednetworks.py'

pip install asymmetree

from treebasednetworks import *

def main():
    # Définir le nombre de caractères
    nbrCaractere = 3

    # Appel de la fonction build_graph_from_newick pour Construire l'arbre G à partir de la chaîne au format Newick
    newick_string = "(((5,4)2,(6,7)3)8,((12,11)10,(13,14)9)15)1;"
    tree_builder = TreeBuilder()
    G, root_id = tree_builder.build_graph_from_newick(newick_string)

    # Initialisation du l'arbre G
    G = tree_builder.initialize_graph(G, nbrCaractere)

    # Ajouter des timestamps aux nœuds du G
    timestamp_manager = TimestampManager()
    G = timestamp_manager.add_timestamp(G, root_id)

    # Appel de la fonction label_leaves pour étiqueter les feuilles pour établir un Non-PTN
    labeler = LeafLabeler()
    G, node1, node2 = labeler.label_leaves_tree(G, nbrCaractere)

    # Affichage l'arbre G avec les étiquettes des feuilles
    tree_builder.drawGraph(G)

    # Ajoute des transferts aléatoires en respectant certaines conditions pour obtenir un graphe non PTN
    transfer_manager = TransferManager()
    G = transfer_manager.add_transfers_to_tree_Non_PTN(G, node1, node2)


    # Affiche les étiquettes des feuilles du graphe
    labeler.display_leaf_labels(G)

    attributes = labeler.set_leaf_attributes(G, nbrCaractere)

    print("\n-------------------------------------")
    print(attributes)
    print("\n-------------------------------------")
    # Liste des caractères à vérifier
    C = [f'c{i+1}' for i in range(nbrCaractere)]

    tree_networks = TreeBasedNetworks()
    # Appel de la fonction findLabeling pour chercher un étiquetage possible
    l = tree_networks.findLabeling(G, attributes, C)

    # Afficher les horodatages
    timestamp_manager.display_timestamps(G)

if __name__ == "__main__":
    main()