import polars as pl


def calculer_kpis_vente(chemin_enriched):
    """
    Calcule les indicateurs clés pour le tableau de bord.
    """
    # 1. Chargement des données enrichies
    df = pl.read_parquet(chemin_enriched)

    # 2. Calcul des KPIs globaux
    kpis = df.select([
        pl.len().alias("total_vehicules"),
        pl.col("sellingprice").sum().alias("chiffre_affaires_total"),
        pl.col("sellingprice").mean().alias("prix_moyen_vente"),
        pl.col("marge_mmr").mean().alias("profitabilite_moyenne")
    ])

    # 3. Calcul par Marque (Top Performance)
    performance_marques = (
        df.group_by("make")
        .agg([
            pl.len().alias("nombre_ventes"),
            pl.col("sellingprice").mean().alias("prix_moyen")
        ])
        .sort("nombre_ventes", descending=True)
        .head(10)
    )

    return kpis, performance_marques


# --- EXÉCUTION ---
if __name__ == "__main__":
    PATH = 'D:/Analyse_car/data/cleaned/car_prices_enriched.parquet'
    stats_globales, top_10 = calculer_kpis_vente(PATH)

    print("--- INDICATEURS CLÉS ---")
    print(stats_globales)
    print("\n--- TOP 10 MARQUES ---")
    print(top_10)