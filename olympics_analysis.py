import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Olympic dataset
df = pd.read_csv("athlete_events.csv")

# Data cleaning
df = df.drop_duplicates()
df = df.dropna(subset=["Age"])
df["Medal"] = df["Medal"].fillna("No Medal")

# Basic analysis
print("Total Athletes:", len(df))
print("Average Age:", round(np.mean(df["Age"]), 1))

# Top 5 countries by medals
medals = df[df["Medal"] != "No Medal"]
top_countries = medals["Team"].value_counts().head(5)

print("\nTop 5 Countries:")
print(top_countries)

# Graph 1: Medals by country
top_countries.plot(kind="bar", title="Top 5 Countries by Medals")
plt.xlabel("Country")
plt.ylabel("Medals")
plt.tight_layout()
plt.show()

# Graph 2: Age distribution
sns.histplot(df["Age"], bins=20)
plt.title("Age Distribution of Athletes")
plt.xlabel("Age")
plt.tight_layout()
plt.show()

# Graph 3: Height vs Weight
sns.scatterplot(data=df, x="Height", y="Weight")
plt.title("Height vs Weight of Athletes")
plt.tight_layout()
plt.show()

# Graph 4: Athletes over the years
athletes = df.groupby("Year")["ID"].nunique()
athletes.plot(kind="line", title="Athlete Participation Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Athletes")
plt.tight_layout()
plt.show()
