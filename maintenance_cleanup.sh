#!/bin/bash

# Chemins des dossiers
DATA_DIR="01_SOFTWARE/Kinetic-RNG"
ARCHIVE_DIR="$DATA_DIR/archives"

# Création du dossier archive s'il n'existe pas
mkdir -p "$ARCHIVE_DIR"

# Déplacement des anciens fichiers CSV (ceux qui ne sont pas la session actuelle)
# On ajoute un horodatage au nom du fichier pour ne rien perdre
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

if [ -f "$DATA_DIR/pulse_history.csv" ]; then
    mv "$DATA_DIR/pulse_history.csv" "$ARCHIVE_DIR/pulse_history_$TIMESTAMP.csv"
    echo "📦 Session précédente archivée dans $ARCHIVE_DIR"
else
    echo "✨ Le dossier est déjà propre."
fi