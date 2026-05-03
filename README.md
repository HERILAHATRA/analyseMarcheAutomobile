# 🚗 Analyse du Marché Automobile

## Présentation du Projet
Ce projet, réalisé dans le cadre de mon **Master 2 en Data Science**, vise à transformer une masse de données brutes sur les ventes de voitures en **indicateurs stratégiques**. 

L'objectif est d'automatiser le nettoyage, l'enrichissement (Feature Engineering) et la visualisation pour extraire le "Signal" des données.

## Architecture du Projet (Modularité)
Le projet est structuré de manière professionnelle pour garantir la réutilisabilité du code :

- **`src/`** : Le moteur du projet (Scripts Python `.py`).
  - `data_cleaning.py` : Pipeline ETL pour convertir le CSV en Parquet.
  - `feature_engineering.py` : Création de colonnes (Âge du véhicule, Marge MMR).
  - `kpi_calculation.py` : Calcul des indicateurs de performance.
- **`notebooks/`** : Laboratoire d'analyse (`.ipynb`).
  - `01_exploration.ipynb` : Visualisation des tendances et corrélations.
- **`dashboard/`** : Rapport interactif Power BI connecté au fichier Parquet enrichi.
- **`data/`** : Dossiers `raw` (brut) et `cleaned` (traité).

## Technologies Utilisées
- **Polars** : Pour un traitement de données ultra-rapide (Lazy API).
- **Python** : Logique de programmation et automatisation.
- **Parquet** : Format de stockage optimisé pour la performance.
- **Power BI** : Data Visualization et Business Intelligence.

## Résultats Clés
- Extraction de la **dépréciation moyenne par âge** de véhicule.
- Analyse de la **marge MMR** (écart prix réel vs marché) par marque.
- Automatisation complète du flux de données (Raw -> Clean -> Enriched -> BI).

---
*Développé par **Herilahatra** - Spécialiste en Solutions de Données (Destiny Data)*
