# data-science-education-earnings

# Project Overview

This project analyzes labor force trends and earnings by educational attainment. It includes data preprocessing, exploratory analysis, trend analysis, and forecasting to provide insights into workforce patterns over time.

# Folder Structure

```
project-root/
├── data/               # Raw and processed datasets
├── scripts/            # Python scripts for analysis
├── outputs/            # Generated reports, figures, and forecasts
├── README.md           # Project documentation
├── requirements.txt    # Dependencies list
```

# Usage

## 1. Setup the Project:

Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file.
```sh
pip install -r requirements.txt
```

## 2. Preprocess the Data:
Run the following command to clean and prepare the dataset:
```sh
python scripts/01_preprocess.py
```

## 3. Perform Exploratory Data Analysis:
Run the exploratory analysis script to generate summaries and plots:
```sh
python scripts/02_exploratory_analysis.py
```

## 4. Analyze Trends:
Compute moving averages and analyze historical trends with:
```sh
python scripts/03_trend_analysis.py
```

## 5. Forecast Future Earnings:
Use the forecasting script to predict labor force and earnings trends:
```sh
python scripts/04_forecasting.py
```

# Requirements

- Python 3.x
- pandas
- matplotlib
- statsmodels

Install dependencies using:
```sh
pip install -r requirements.txt
```

# Acknowledgments

dataset name: Labor Force and Earnings by Educational Attainment  
dataset author: Hridesh Kedia  
dataset source: [Kaggle](https://www.kaggle.com/datasets/hrideshkedia/labor-force-and-earnings-by-educational-attainment)