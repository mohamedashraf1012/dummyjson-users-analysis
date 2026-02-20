# 📊 DummyJSON Users Data Analysis

> Python data analysis project exploring user demographics using the DummyJSON API.

---

## 🚀 Project Overview
This project fetches user data from the DummyJSON API and performs:
- Data cleaning and preparation
- Exploratory data analysis (EDA)
- Statistical insights
- Data visualization using Seaborn

---

## 🧩 Project Structure

dummyjson-users-analysis/
│
├── data/ # Raw data (CSV)
├── src/ # Python scripts
├── notebooks/ # Jupyter analysis
├── outputs/ # Analysis results (CSV)
├── plots/ # Visualizations (PNG)
└── README.md


---

## 📈 Key Analysis
- Average age of users
- Average age by gender
- Users distribution by gender
- Top 10 cities by number of users
- Relationship between age, height, and weight

---

## 📊 Sample Visualizations
<p align="center">
  <img src="plots/plot1_age_distribution.png" width="45%" />
  <img src="plots/plot4_age_vs_height.png" width="45%" />
</p>

<p align="center">
  <img src="plots/plot5_age_vs_weight.png" width="45%" />
  <img src="plots/plot2_users_per_gender.png" width="45%" />
</p>

---

## 🛠️ Tools & Libraries
- Python
- Pandas
- NumPy
- Seaborn
- Matplotlib

---

## ▶️ How to Run
```bash
pip install -r requirements.txt
python src/fetch_users.py