"""
Olympic Games Data Analysis and Visualization
VSEC Mini Project - Exploratory Data Analysis (EDA)
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Configuration paths
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "athlete_events.csv"
OUTPUT_DIR = BASE_DIR / "outputs"


def _display_plot(show: bool = True) -> None:
    """Displays plot in interactive environments; safely closes in headless/Agg modes."""
    backend = plt.get_backend().lower()
    if show and "agg" not in backend:
        plt.show()
    else:
        plt.close()


def load_and_preprocess_data(filepath: Path) -> pd.DataFrame:
    """Load the Olympic dataset and perform data cleaning."""
    if not filepath.exists():
        raise FileNotFoundError(f"Dataset not found at: {filepath}")

    df = pd.read_csv(filepath)

    # 1. Remove duplicate entries
    df = df.drop_duplicates()

    # 2. Fill missing medal values with 'No Medal'
    df["Medal"] = df["Medal"].fillna("No Medal")

    return df


def display_basic_statistics(df: pd.DataFrame) -> dict:
    """Calculate and print primary summary statistics."""
    df_age = df.dropna(subset=["Age"])
    total_athletes = df["ID"].nunique()
    avg_age = df_age["Age"].mean()

    print("=" * 45)
    print("       OLYMPIC DATASET SUMMARY STATS         ")
    print("=" * 45)
    print(f"Total Unique Athletes : {total_athletes}")
    print(f"Average Athlete Age   : {avg_age:.2f} years")

    # Top 5 countries by medals (deduplicated per event)
    medals = df[df["Medal"] != "No Medal"].drop_duplicates(
        subset=["Year", "Season", "Event", "NOC", "Medal"]
    )
    top_countries = medals["NOC"].value_counts().head(5)

    print("\nTop 5 Countries by Medal Count:")
    print("-" * 35)
    for noc, count in top_countries.items():
        print(f"  {noc:<6} : {count} medals")
    print("=" * 45)

    return {
        "total_athletes": total_athletes,
        "avg_age": avg_age,
        "top_countries": top_countries,
    }


def plot_top_countries(top_countries: pd.Series, output_dir: Path, show: bool = True) -> None:
    """Graph 1: Bar chart of top 5 countries by medals."""
    plt.figure(figsize=(8, 5))
    top_countries.plot(kind="bar", color="steelblue", edgecolor="black")
    plt.title("Top 5 Countries by Medals", fontsize=14, fontweight="bold")
    plt.xlabel("Country (NOC)", fontsize=11)
    plt.ylabel("Number of Medals", fontsize=11)
    plt.xticks(rotation=0)
    plt.tight_layout()

    save_path = output_dir / "01_top_5_countries_medals.png"
    plt.savefig(save_path, dpi=300)
    print(f"[Saved] {save_path.name}")
    _display_plot(show)


def plot_age_distribution(df: pd.DataFrame, output_dir: Path, show: bool = True) -> None:
    """Graph 2: Histogram of athlete age distribution."""
    df_age = df.dropna(subset=["Age"])
    plt.figure(figsize=(8, 5))
    sns.histplot(df_age["Age"], bins=20, color="teal", kde=True, edgecolor="black")
    plt.title("Age Distribution of Athletes", fontsize=14, fontweight="bold")
    plt.xlabel("Age (years)", fontsize=11)
    plt.ylabel("Athlete Count", fontsize=11)
    plt.tight_layout()

    save_path = output_dir / "02_age_distribution.png"
    plt.savefig(save_path, dpi=300)
    print(f"[Saved] {save_path.name}")
    _display_plot(show)


def plot_height_vs_weight(df: pd.DataFrame, output_dir: Path, show: bool = True) -> None:
    """Graph 3: Scatter plot of height vs weight."""
    plt.figure(figsize=(8, 5))
    sns.scatterplot(
        data=df,
        x="Height",
        y="Weight",
        alpha=0.4,
        s=25,
        color="crimson",
        edgecolor="none",
    )
    plt.title("Height vs Weight of Athletes", fontsize=14, fontweight="bold")
    plt.xlabel("Height (cm)", fontsize=11)
    plt.ylabel("Weight (kg)", fontsize=11)
    plt.tight_layout()

    save_path = output_dir / "03_height_vs_weight.png"
    plt.savefig(save_path, dpi=300)
    print(f"[Saved] {save_path.name}")
    _display_plot(show)


def plot_athlete_participation(df: pd.DataFrame, output_dir: Path, show: bool = True) -> None:
    """Graph 4: Line plot of athlete participation over the years by season."""
    athletes = df.groupby(["Year", "Season"])["ID"].nunique().unstack()

    plt.figure(figsize=(9, 5))
    athletes.plot(kind="line", marker="o", ax=plt.gca(), linewidth=2)
    plt.title("Athlete Participation Over Years", fontsize=14, fontweight="bold")
    plt.xlabel("Year", fontsize=11)
    plt.ylabel("Number of Athletes", fontsize=11)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()

    save_path = output_dir / "04_athlete_participation_over_years.png"
    plt.savefig(save_path, dpi=300)
    print(f"[Saved] {save_path.name}")
    _display_plot(show)


def main(show_plots: bool = True) -> None:
    """Main execution pipeline."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("\nStarting Olympic Data Analysis...\n")
    df = load_and_preprocess_data(DATA_FILE)
    stats = display_basic_statistics(df)

    print("\nGenerating and saving visualizations...")
    plot_top_countries(stats["top_countries"], OUTPUT_DIR, show=show_plots)
    plot_age_distribution(df, OUTPUT_DIR, show=show_plots)
    plot_height_vs_weight(df, OUTPUT_DIR, show=show_plots)
    plot_athlete_participation(df, OUTPUT_DIR, show=show_plots)
    print("\nAnalysis and visualization complete!\n")


if __name__ == "__main__":
    main()
