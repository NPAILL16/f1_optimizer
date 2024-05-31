import pandas as pd

def lire_matrice_distances(fichier):
    # Lire le fichier CSV en utilisant pandas, en définissant la première colonne comme index
    df = pd.read_csv(fichier, index_col=1)
    
    # Remplacer les valeurs manquantes par l'infini (pour les villes qui ne sont pas connectées) car l'algorithme glouton ne peut pas sinon 
    df.fillna(float('inf'), inplace=True)
    
    # Convertir le DataFrame en une liste de listes (matrice d'adjacence)
    matrice = df.values.tolist()
    return matrice
