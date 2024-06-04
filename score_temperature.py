import pandas as pd

def ajuster_distances_avec_temperature(matrice, fichier):
    # Lire les températures depuis le fichier CSV
    df_temp = pd.read_csv(fichier, index_col=27)
    
    # Parcourir la matrice et ajuster les distances en fonction de la température
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if i != j:
                temperature = df_temp.iloc[i, j]
                
                # Appliquer un bonus ou un malus selon la température
                if 15 <= temperature <= 22.5:
                    matrice[i][j] *= 0.9  # Bonus pour les températures entre 10 et 20 degrés
                elif temperature < 18.8 or temperature > 18.8: 
                    ecart_temperature = abs(temperature - 15)
                    matrice[i][j] *= 1 + (ecart_temperature / 100)  # Malus proportionnel à l'écart 

    return matrice


# 20 degrés et 15 degrés sont choisis arbitrairement pour l'essai, a changer en fonction de la température idéale pour une F1.