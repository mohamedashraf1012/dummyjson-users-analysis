# 📊 DummyJSON Users Data Analysis

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-orange)

> A Python-based data analysis project that explores user demographics using data fetched from the DummyJSON API.

---

## 🚀 Project Overview

This project focuses on analyzing user data obtained from the **DummyJSON API**.  
It demonstrates a complete data analysis workflow including:

- Fetching data from a REST API
- Cleaning and preparing the data
- Exploratory Data Analysis (EDA)
- Statistical analysis
- Data visualization using Seaborn
- Organizing results in a professional GitHub repository

---

## 🧩 Project Structure


dummyjson-users-analysis/
│
├── data/ # Raw data (CSV)
│ └── users_data.csv
│
├── src/ # Python scripts
│ └── fetch_users.py
│
├── notebooks/ # Jupyter Notebook analysis
│ └── analysis.ipynb
│
├── outputs/ # Exported analysis results
│ ├── avg_age_by_gender.csv
│ ├── users_per_gender.csv
│ ├── top10_cities.csv
│ └── summary_stats_numeric.csv
│
├── plots/ # Data visualizations
│ ├── plot1_age_distribution.png
│ ├── plot2_users_per_gender.png
│ ├── plot3_avg_age_by_gender.png
│ ├── plot4_age_vs_height.png
│ └── plot5_age_vs_weight.png
│
├── requirements.txt
└── README.md


---

## 📈 Key Analysis Performed

- Average age of users
- Average age by gender
- Number of users per gender
- Top 10 cities with the highest number of users
- Average height and weight
- Relationship between age and height / weight

---

## 📊 Sample Visualizations

<p align="center">
  <img src="plots/plot1_age_distribution.png" width="45%" />
  <img src="plots/plot2_users_per_gender.png" width="45%" />
</p>

<p align="center">
  <img src="plots/plot4_age_vs_height.png" width="45%" />
  <img src="plots/plot5_age_vs_weight.png" width="45%" />
</p>

---

## 🧠 Key Findings

- The average age of users is approximately in the mid-30s.
- The age distribution is relatively balanced across genders.
- No strong correlation was found between age and height or weight.
- Some cities show significantly higher user concentration than others.

---

## 🛠️ Tools & Libraries Used

- **Python**
- **Pandas**
- **NumPy**
- **Requests**
- **Seaborn**
- **Matplotlib**

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
2️⃣ (Optional) Fetch data from the API
python src/fetch_users.py
3️⃣ Run the analysis

Open the notebook:

notebooks/analysis.ipynb
```
🎓 Academic Context

This project was developed as part of an ITI Data Analysis Lab, focusing on:

Practical data analysis skills

Working with APIs

Clean and structured GitHub projects

👤 Author

Mohamed Ashraf
ITI – Data Analysis Track

⭐ If you find this project useful, feel free to explore the repository.