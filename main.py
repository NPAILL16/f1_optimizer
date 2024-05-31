from convertisseur_matrice import lire_matrice_distances
from algorithme_glouton import glouton
from score_temperature import ajuster_distances_avec_temperature

def main():
    # Lire la matrice d'adjacence des distances depuis le fichier CSV
    fichier = './fichier_matrice_adjacente.csv'
    distance_matrix = lire_matrice_distances(fichier)
    
    # Lire les températures depuis le fichier CSV
    fichier = './fichier_matrice_adjacente.csv' # Ici même fichier
    distances_ajustees = ajuster_distances_avec_temperature(distance_matrix, fichier)

    # Résoudre le problème TSP avec l'algorithme glouton avancé
    meilleur_chemin = glouton(distances_ajustees)

    # Afficher le chemin optimal : EUREKA
    print("Ordre de course optimal:")
    for indice_ville in meilleur_chemin:
        print(f"Ville {indice_ville + 1}")  # Ajouter 1 pour les indices des villes (base 1)

if __name__ == "__main__":
    main()
