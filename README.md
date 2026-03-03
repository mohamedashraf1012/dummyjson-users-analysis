# 📊 DummyJSON Users Data Analysis

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-orange)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED)

> A Python-based data analysis project that explores user demographics using data fetched from the DummyJSON API — now with an automated pipeline and Docker support.

---

## 🚀 Project Overview

This project focuses on analyzing user data obtained from the **DummyJSON API**.  
It demonstrates a complete data analysis workflow including:

- Fetching data from a REST API
- Cleaning and preparing the data
- Exploratory Data Analysis (EDA)
- Statistical analysis
- Data visualization using Seaborn
- Saving results as CSV files and plots
- Running the entire pipeline automatically using **Docker**

---

## 🧩 Project Structure

```bash
dummyjson-users-analysis/
│
├── data/                    # Raw data (CSV)
│   └── users_data.csv
│
├── src/                     # Python scripts
│   └── run_pipeline.py      # End-to-end automated pipeline (API -> analysis -> outputs -> plots)
│
├── notebooks/               # Jupyter Notebook analysis (for exploration)
│   └── analysis.ipynb
│
├── outputs/                 # Manual analysis outputs (original)
│   ├── avg_age_by_gender.csv
│   ├── users_per_gender.csv
│   ├── top10_cities.csv
│   └── summary_stats_numeric.csv
│
├── plots/                   # Manual plots (original)
│   ├── plot1_age_distribution.png
│   ├── plot2_users_per_gender.png
│   ├── plot3_avg_age_by_gender.png
│   ├── plot4_age_vs_height.png
│   └── plot5_age_vs_weight.png
│
├── outputs_docker/          # Docker pipeline outputs (separated)
│   └── *.csv
│
├── plots_docker/            # Docker pipeline plots (separated)
│   └── *.png
│
├── Dockerfile
├── .dockerignore
├── requirements.txt
└── README.md
```
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
- **Docker (for automated execution)**

---

## ▶️ How to Run the Project
### ✅ Option 1: Run Locally (Python)
#### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
#### 2️⃣ Run the automated pipeline
```bash
python src/run_pipeline.py
```
##### Outputs will be saved in:

- **outputs_docker/**

- **plots_docker/**


### 🐳 Option 2: Run with Docker (Recommended)
#### 1️⃣ Build the image
```bash
docker build -t dummyjson-users-analysis .
```
#### 2️⃣ Run the container
##### This mounts folders so results are saved on your machine.

###### Windows (PowerShell):
```bash
docker run --rm `
 -v "${PWD}\outputs_docker:/app/outputs_docker" `
 -v "${PWD}\plots_docker:/app/plots_docker" `
 -v "${PWD}\data:/app/data" `
 dummyjson-users-analysis
```
###### Linux/Mac:
```bash
docker run --rm \
 -v "$(pwd)/outputs_docker:/app/outputs_docker" \
 -v "$(pwd)/plots_docker:/app/plots_docker" \
 -v "$(pwd)/data:/app/data" \
 dummyjson-users-analysis

```

## 🎓 Academic Context

### This project was developed as part of an ITI Data Analysis Lab, focusing on:

- **Practical data analysis skills**
- **Working with APIs**
- **Clean and structured GitHub projects**
- **Production-friendly automation with Docker**

## 👤 Author

Mohamed Ashraf

ITI – Data Engineering Track

# ⭐ If you find this project useful, feel free to explore the repository.