# Optimisation du Calendrier de la F1 avec un Algorithme Glouton

## Introduction

Ce projet propose une méthode pour optimiser le calendrier des courses de Formule 1 en minimisant les distances parcourues entre les villes hôtes. L'objectif est de réduire les coûts et les émissions de carbone associés aux déplacements entre les différentes courses en . Nous utilisons pour cela un algorithme glouton, qui fournit une solution rapide et efficace ainsi quun système de score et d'écart sur la température pour pondérer les, mais non optimale.

## Structure du Projet

Le projet est structuré comme suit :

```
f1_optimizer/
|-- main.py
|-- convertisseur_matrice.py
|-- algorithme_glouton.py
|-- score_temperature.py
|-- fichier_matrice_adjacente.csv
```

- `main.py` : Script principal qui coordonne la lecture des données, l'exécution de l'algorithme TSP, et l'affichage des résultats.
- `convertisseur_matrice.py` : Module pour lire la matrice des distances à partir d'un fichier CSV.
- `algorithme_glouton.py` : Module contenant l'algorithme glouton pour résoudre le problème du voyageur de commerce.
- `score_temperature.py` : Module pour ajuster les distances en fonction de la température, en appliquant des bonus et des malus.
- `fichier_matrice_adjacente.csv` : Fichier contenant la matrice d'adjacence des distances entre les villes, la moyenne des temppératures et leurs écart.
  
## Utilisation

1. Assurez-vous que les fichiers `fichier_matrice_adjacente.csv` formatés et placés dans le même dossier que les scripts Python.
2. Exécutez le script principal :

```bash
python main.py
```

Ce script va :
- Lire les distances, les températures et les écarts.
- Ajuster les distances en fonction des températures.
- Utiliser un algorithme glouton pour déterminer l'ordre optimal des courses.

## Algorithme Glouton

Un algorithme glouton est une méthode qui fait des choix locaux optimaux à chaque étape avec l'espoir de trouver une solution globale optimale. Dans ce projet, l'algorithme glouton choisit à chaque étape la ville non visitée la plus proche comme prochaine destination.

### Limites de l'Algorithme Glouton

Bien que l'algorithme glouton soit rapide et efficace, il n'est pas garanti de fournir la solution optimale pour le problème du voyageur de commerce (TSP). Il peut produire des résultats satisfaisants pour des problèmes de petite à moyenne taille, mais pour des solutions plus précises, d'autres méthodes sont nécessaires.

## Perspectives d'Amélioration

Pour obtenir des solutions plus précises, on pourrait envisager des approches plus sophistiquées telles que :
- **Algorithmes génétiques** : Ces algorithmes s'inspirent des processus de la sélection naturelle pour explorer un large espace de solutions et converger vers des solutions optimales.
- **Apprentissage automatique (Machine Learning)** : Entraîner des modèles sur de grandes quantités de données pour prédire des solutions optimales ou presque optimales.
- **Optimisation exacte** : Utilisation d'algorithmes exacts comme la programmation linéaire, bien que cela puisse nécessiter des ressources computationnelles considérables pour de grands ensembles de données.

Ces méthodes nécessitent généralement une grande puissance de calcul et une quantité importante de données pour fonctionner efficacement, mais elles peuvent considérablement améliorer la qualité des solutions obtenues.

## Conclusion

Ce projet propose une solution simple et rapide pour optimiser le calendrier des courses de Formule 1 en utilisant un algorithme glouton. Bien que cette approche ne soit pas optimale, elle fournit une base solide pour des optimisations plus avancées utilisant des techniques telles que les algorithmes génétiques ou l'apprentissage automatique.
