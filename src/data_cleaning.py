import polars as pl
import os


def charger_et_nettoyer(chemin_source, colonne_prix="sellingprice"):
    """
    Lit un fichier CSV brut et applique un premier niveau de nettoyage.

    Args:
        chemin_source (str): Chemin local vers le fichier CSV.
        colonne_prix (str): Nom de la colonne pour le filtrage (défaut: sellingprice).
    """
    return (
        pl.scan_csv(chemin_source, ignore_errors=True)
        .filter(pl.col(colonne_prix) > 0)
        .drop_nulls()
        .with_columns(pl.all().name.to_lowercase())
    )


def convertir_csv_vers_parquet(chemin_csv, chemin_parquet):
    """Automatise tout le processus de A à Z."""
    print(f"Début du traitement de : {chemin_csv}...")

    # Appel de la fonction de nettoyage (Lazy)
    plan = charger_et_nettoyer(chemin_csv)

    # Exécution de la sauvegarde (Sink)
    plan.sink_parquet(chemin_parquet)

    print(f"Terminé ! Fichier sauvegardé ici : {chemin_parquet}")


# --- POINT D'ENTRÉE DU SCRIPT ---
if __name__ == "__main__":
    # Configuration des chemins locaux (Disque D:)
    SOURCE = 'D:/Analyse_car/data/raw/car_prices.csv'
    DESTINATION = 'D:/Analyse_car/data/cleaned/car_prices_clean.parquet'

    # Lancement de l'automatisation
    convertir_csv_vers_parquet(SOURCE, DESTINATION)