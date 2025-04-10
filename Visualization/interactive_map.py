import os
import yaml
import plotly.express as px
import plotly.graph_objects as go

def generate_interactive_map(output_file="map.html"):
    with open("./Visualization/output.yaml", "r") as file:
        country_data = yaml.safe_load(file)

    parent_dir = os.path.dirname(os.path.dirname(__file__))
    criteria_path = os.path.join(parent_dir, "./Visualization/current_criteria_weights.yaml")
    with open(criteria_path, "r") as file:
        criteria_data = yaml.safe_load(file)

    country_codes = list(country_data.keys())
    indices = list(country_data.values())

    fig = px.choropleth(
        locations=country_codes,
        locationmode="ISO-3",
        color=indices,
        color_continuous_scale="RdYlGn",
    )

    fig.update_layout(
        geo=dict(
            showframe=False,
            showcoastlines=True,
            projection_type="miller",
            landcolor="lightgray",
            oceancolor="lightblue",
            showocean=True,
        )
    )

    fig.update_layout(
        title={
            "text": "Carte pour choisir le lieu d'implantation d'un nouveau DC dans le Monde",
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top",
            "font": {"size": 24, "family": "Nunito", "color": "black"}
        },
        geo=dict(showframe=False, showcoastlines=True, projection_type="equirectangular"),
        coloraxis_colorbar=dict(title="Indice de priorité")
    )

    fig.update_layout(
        dragmode="zoom",
        geo=dict(
            showframe=False,
            showcoastlines=True,
            projection_type="equirectangular",
        )
    )

    fig.update_layout(
        geo=dict(
            showframe=False,
            showcoastlines=True,
            projection_type="orthographic",
            landcolor="lightgray",
            oceancolor="lightblue",
            showocean=True,
            resolution=50,
        ),
        uirevision="constant",
    )

    most_important = criteria_data.get("most_important_criteria", {})
    least_important = criteria_data.get("least_important_criteria", {})

    most_important_text = "<br>".join([f"{key}: {value}" for key, value in most_important.items()])
    least_important_text = "<br>".join([f"{key}: {value}" for key, value in least_important.items()])

    criteria_text = (
        f"<b>Rappel des critères de choix :</b><br><br>"
        f"<b>Critères les plus importants :</b><br>{most_important_text}<br><br>"
        f"<b>Critères les moins importants :</b><br>{least_important_text}"
    )

    fig.add_annotation(
        text=criteria_text,
        xref="paper", yref="paper",
        x=0, y=0.5,
        showarrow=False,
        align="left",
        font=dict(size=14, family="Nunito", color="black"),
        bgcolor="rgba(255, 255, 255, 0.8)",
        bordercolor="black",
        borderwidth=1
    )

    script_dir = os.path.dirname(__file__)
    output_path = os.path.join(script_dir, output_file)

    fig.write_html(output_path, include_plotlyjs="cdn")
    print(f"Fichier HTML généré : {output_path}")

    fig.show()

if __name__ == "__main__":
    generate_interactive_map()
