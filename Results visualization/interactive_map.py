import os
import yaml
import plotly.express as px
import plotly.graph_objects as go

# Charger le fichier YAML pour les pays
with open("output.yaml", "r") as file:
    country_data = yaml.safe_load(file)

# Charger les critères depuis le fichier YAML
parent_dir = os.path.dirname(os.path.dirname(__file__))  # Dossier parent
criteria_path = os.path.join(parent_dir, "criteria_weights.yaml")
with open(criteria_path, "r") as file:
    criteria_data = yaml.safe_load(file)

# Convertir les données en listes pour Plotly
country_codes = list(country_data.keys())
indices = list(country_data.values())

# Créer une carte choroplèthe avec Plotly
fig = px.choropleth(
    locations=country_codes,  # Codes des pays (ISO Alpha-3)
    locationmode="ISO-3",     # Mode de localisation (ISO Alpha-3)
    color=indices,            # Valeurs des indices
    color_continuous_scale="RdYlGn",  # Échelle de couleurs (Rouge -> Jaune -> Vert)
)

# Ajouter des styles à la carte
fig.update_layout(
    geo=dict(
        showframe=False,
        showcoastlines=True,
        projection_type="miller",  # Style de projection (exemple : "natural earth")
        landcolor="lightgray",  # Couleur des terres
        oceancolor="lightblue",  # Couleur des océans
        showocean=True,  # Afficher les océans
    )
)

# Ajouter des labels, ajuster la mise en page et personnaliser le titre
fig.update_layout(
    title={
        "text": "Carte pour choisir le lieu d'implantation d'un nouveau DC dans le Monde",  # Titre
        "x": 0.5,  # Centrer le titre (0 = gauche, 1 = droite)
        "xanchor": "center",  # Ancrage horizontal
        "yanchor": "top",  # Ancrage vertical
        "font": {"size": 24, "family": "Nunito", "color": "black"}  # Police, taille et couleur
    },
    geo=dict(showframe=False, showcoastlines=True, projection_type="equirectangular"),
    coloraxis_colorbar=dict(title="Indice de priorité")
)

# Activer le zoom interactif avec rectangle de sélection
fig.update_layout(
    dragmode="zoom",  # Permet de dessiner un rectangle pour zoomer
    geo=dict(
        showframe=False,
        showcoastlines=True,
        projection_type="equirectangular",  # Projection par défaut
    )
)

# Mettre à jour la projection de la carte en mode globe 3D avec rotation
fig.update_layout(
    geo=dict(
        showframe=False,
        showcoastlines=True,
        projection_type="orthographic",  # Globe 3D
        landcolor="lightgray",  # Couleur des terres
        oceancolor="lightblue",  # Couleur des océans
        showocean=True,  # Afficher les océans
        resolution=50,  # Résolution des frontières
    ),
    uirevision="constant",  # Permet de conserver l'état interactif (rotation)
)

# Récupérer les critères les plus et les moins importants
most_important = criteria_data.get("most_important_criteria", {})
least_important = criteria_data.get("least_important_criteria", {})

# Formater les critères pour l'affichage
most_important_text = "<br>".join([f"{key}: {value}" for key, value in most_important.items()])
least_important_text = "<br>".join([f"{key}: {value}" for key, value in least_important.items()])

# Texte final pour l'annotation avec un titre
criteria_text = (
    f"<b>Rappel des critères de choix :</b><br><br>"  # Titre ajouté
    f"<b>Critères les plus importants :</b><br>{most_important_text}<br><br>"
    f"<b>Critères les moins importants :</b><br>{least_important_text}"
)

# Ajouter un rappel des critères à gauche de la carte
fig.add_annotation(
    text=criteria_text,
    xref="paper", yref="paper",
    x=0, y=0.5,  # Position à gauche
    showarrow=False,
    align="left",
    font=dict(size=14, family="Nunito", color="black"),
    bgcolor="rgba(255, 255, 255, 0.8)",  # Fond blanc semi-transparent
    bordercolor="black",
    borderwidth=1
)

# Déterminer le chemin absolu pour enregistrer le fichier HTML
script_dir = os.path.dirname(__file__)  # Répertoire du script actuel
output_path = os.path.join(script_dir, "map.html")  # Chemin complet pour map.html

# Ajouter un lien vers Google Fonts pour Nunito
fig.write_html(output_path, include_plotlyjs="cdn")
print(f"Fichier HTML généré : {output_path}")

# Afficher la carte
fig.show()