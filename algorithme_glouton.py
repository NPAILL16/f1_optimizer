def glouton(matrice):
    n = len(matrice)
    visitees = [False] * n
    chemin = [0]
    visitees[0] = True
    distance_totale = 0

    ville_actuelle = 0
    for _ in range(n - 1): # On doit visiter toutes les villes
        prochaine_ville = None
        distance_min = float('inf')
        for ville in range(n): # On cherche la ville la plus proche
            if not visitees[ville] and 0 < matrice[ville_actuelle][ville] < distance_min: # On ne visite pas les villes déjà visitées
                distance_min = matrice[ville_actuelle][ville]
                prochaine_ville = ville
        chemin.append(prochaine_ville) # On ajoute la ville à la liste des villes visitées
        visitees[prochaine_ville] = True
        distance_totale += distance_min
        ville_actuelle = prochaine_ville

    # Retourner à la ville de départ
    distance_totale += matrice[ville_actuelle][0] # On ajoute la distance pour revenir à la ville de départ
    chemin.append(0) # On revient à la ville de départ

    return chemin, distance_totale
