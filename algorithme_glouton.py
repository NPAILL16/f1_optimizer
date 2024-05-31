def glouton(matrice):
    nombre_villes = len(matrice)
    visitees = [False] * nombre_villes
    chemin = [0]  # Commencer depuis la première ville (indice 0)

    visitees[0] = True

    for _ in range(nombre_villes - 1):
        derniere_visitee = chemin[-1]
        distance_minimale = float('inf')
        ville_la_plus_proche = -1

        for ville in range(nombre_villes):
            if not visitees[ville]:
                # Si la ville n'est pas visitée et la distance est plus courte
                if matrice[derniere_visitee][ville] < distance_minimale:
                    distance_minimale = matrice[derniere_visitee][ville]
                    ville_la_plus_proche = ville

        chemin.append(ville_la_plus_proche)
        visitees[ville_la_plus_proche] = True

    # Retourner à la ville de départ pour compléter le circuit
    chemin.append(0)
    return chemin
