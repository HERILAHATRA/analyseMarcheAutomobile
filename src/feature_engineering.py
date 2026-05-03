import polars as pl


def ajouter_indicateurs(chemin_entree):
    """
    Lit le parquet nettoyé et ajoute des colonnes calculées.

    Enrichit le dataset avec des variables stratégiques pour l'analyse prédictive.

    Variables créées :
        - age_vehicule : Différence entre l'année de référence (2015) et l'année de fabrication.
        - marge_mmr : Écart entre le prix de vente réel et l'estimation du marché.
        - km_par_an : Intensité d'usage du véhicule.

    Args:
        chemin_parquet (str): Chemin vers le fichier Parquet nettoyé.

    Returns:
        pl.LazyFrame: Dataset enrichi prêt pour la modélisation ou le dashboard.

    """
    # 1. On part du Parquet (Mode Lazy pour l'optimisation)
    lazy_df = pl.scan_parquet(chemin_entree)

    # 2. Création des nouvelles colonnes (Features)
    plan = lazy_df.with_columns([
        # Calcul de l'âge : (Année de référence 2015 - année de fabrication)
        (2015 - pl.col("year")).alias("age_vehicule"),

        # Performance de la vente : (Prix de vente - Estimation MMR)
        (pl.col("sellingprice") - pl.col("mmr")).alias("marge_mmr"),

        # Kilométrage moyen par an (évite la division par zéro avec .max(1))
        (pl.col("odometer") / (2015 - pl.col("year")).clip(lower_bound=1)).alias("km_par_an")
    ])

    return plan




# --- EXÉCUTION ---
chemin_clean = 'D:/Analyse_car/data/cleaned/car_prices_clean.parquet'
plan_enrichi = ajouter_indicateurs(chemin_clean)

# On sauvegarde dans un NOUVEAU fichier pour garder une trace de chaque étape
plan_enrichi.sink_parquet('D:/Analyse_car/data/cleaned/car_prices_enriched.parquet')

print("Succès : Les nouvelles colonnes (Âge, Marge, Km/an) ont été créées !")