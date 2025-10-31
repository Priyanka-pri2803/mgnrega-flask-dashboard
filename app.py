from flask import Flask, render_template, request
import pandas as pd
import plotly.express as px
import os

app = Flask(__name__)

# ---------- LOAD DATA ----------
csv_file = os.path.join("data", "mgnrega_data.csv")
data = pd.read_csv(csv_file)

# Normalize columns
data.columns = [c.strip().replace(" ", "_") for c in data.columns]

# Month order
month_order = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

@app.route("/", methods=["GET", "POST"])
def index():
    districts = sorted(data["District"].unique())
    selected_district = request.form.get("district", "Bangalore")

    df = data[data["District"] == selected_district].copy()

    # Ensure numeric
    for col in ["Total_Persondays", "Women_Participation_Percent", "Households_Completed", "Average_Days_Of_Employment"]:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    # Sort by Month
    df["Month"] = pd.Categorical(df["Month"], categories=month_order, ordered=True)
    df = df.sort_values("Month")

    # BAR CHART: Total Persondays
    persondays_fig = px.bar(
        df,
        x="Month",
        y="Total_Persondays",
        color="Month",
        text=df["Total_Persondays"].apply(lambda x: f"{int(x):,}"),
        title=f"📊 Total Persondays per Month - {selected_district}",
        category_orders={"Month": month_order},
        color_discrete_sequence=px.colors.qualitative.Bold
    )

    # Stronger visibility
    persondays_fig.update_traces(
        textposition="outside",
        textfont=dict(size=13, color="black"),
        marker=dict(line=dict(color="black", width=1.5)),
        opacity=0.95
    )

    # Layout tuning
    persondays_fig.update_layout(
        template="plotly_white",
        yaxis_title="Total Persondays",
        xaxis_title="Month",
        height=500,
        bargap=0.25,
        plot_bgcolor="white",
        paper_bgcolor="white",
        yaxis=dict(range=[0, df["Total_Persondays"].max() * 1.3])
    )

    #  LINE CHART: Women Participation
    women_fig = px.line(
        df,
        x="Month",
        y="Women_Participation_Percent",
        markers=True,
        text=df["Women_Participation_Percent"].apply(lambda x: f"{x:.1f}%"),
        title=f" Women Participation Trend - {selected_district}",
        category_orders={"Month": month_order},
        color_discrete_sequence=["#1f77b4"]
    )
    women_fig.update_traces(textposition="top center", line_width=3)
    women_fig.update_layout(
        template="plotly_white",
        yaxis_title="Participation (%)",
        xaxis_title="Month",
        height=450
    )

    # Metrics
    metrics = {
        "Households Completed": int(df["Households_Completed"].sum()),
        "Total Persondays": int(df["Total_Persondays"].sum()),
        "Women Participation (%)": f"{df['Women_Participation_Percent'].mean():.1f}",
        "Avg. Days of Employment": f"{df['Average_Days_Of_Employment'].mean():.1f}",
    }

    return render_template(
        "index.html",
        districts=districts,
        selected_district=selected_district,
        metrics=metrics,
        persondays_graph=persondays_fig.to_json(),
        women_graph=women_fig.to_json(),
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080)) 
    app.run(host="0.0.0.0", port=port)










