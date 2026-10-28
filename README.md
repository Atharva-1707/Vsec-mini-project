# Olympic Sports Data Analysis and Visualization Using Python

## About the Project
This mini project analyses Olympic Games athlete data from 1896 to 2016 using Python. It explores athlete participation, medal-winning countries, age distribution, and the relationship between athletes' height and weight.

## Features
- Cleans the dataset by removing duplicate records and rows with missing ages.
- Calculates the total number of athlete records and average age.
- Displays the top five countries by medal count.
- Creates visualizations:
  - Medals by country (bar chart)
  - Athlete age distribution (histogram)
  - Height vs. weight (scatter plot)
  - Athlete participation over the years (line chart)

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Dataset
The program expects a file named `athlete_events.csv` in the same folder as the Python script.

The dataset is from **120 Years of Olympic History: Athletes and Results**:
[Kaggle dataset](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results)

## Requirements
Install the required Python libraries:

```bash
pip install pandas numpy matplotlib seaborn
```

## How to Run
1. Download `athlete_events.csv` from the dataset link above.
2. Place `athlete_events.csv` and `olympics_analysis.py` in the same folder.
3. Run the script:

```bash
python olympics_analysis.py
```

The program prints basic statistics and displays the charts.

## Project Files
- `olympics_analysis.py` — Python source code
- `athlete_events.csv` — Dataset required to run the analysis (download separately)

## Note
The project is a simple educational mini project for data analysis and visualization. The results depend on the dataset file used.
