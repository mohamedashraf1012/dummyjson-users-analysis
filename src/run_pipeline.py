import os
import json
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# =========================
# Paths (project-root safe)
# =========================
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(ROOT_DIR, "data")
OUTPUTS_DIR = os.path.join(ROOT_DIR, "outputs_docker")
PLOTS_DIR = os.path.join(ROOT_DIR, "plots_docker")

CSV_PATH = os.path.join(DATA_DIR, "users_data.csv")

API_URL = "https://dummyjson.com/users"


def ensure_dirs() -> None:
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(OUTPUTS_DIR, exist_ok=True)
    os.makedirs(PLOTS_DIR, exist_ok=True)


def fetch_users_from_api(limit: int = 30) -> pd.DataFrame:
    """
    Fetch all users from DummyJSON API using pagination (limit/skip).
    Returns a normalized DataFrame.
    """
    skip = 0
    all_users = []

    while True:
        params = {"limit": limit, "skip": skip}
        r = requests.get(API_URL, params=params, timeout=30)
        r.raise_for_status()
        data = r.json()

        users = data.get("users", [])
        if not users:
            break

        all_users.extend(users)
        skip += limit

    df = pd.json_normalize(all_users)
    return df


def save_raw_csv(df: pd.DataFrame, path: str = CSV_PATH) -> None:
    df.to_csv(path, index=False)
    print(f"✅ Data fetched and saved successfully -> {path}")
    print("Total users:", df.shape[0])


def load_csv(path: str = CSV_PATH) -> pd.DataFrame:
    df = pd.read_csv(path)
    print(f"✅ Loaded CSV successfully -> {path}")

    # Ensure numeric columns are numeric
    for col in ["age", "height", "weight"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


def extract_country_if_needed(df: pd.DataFrame) -> pd.DataFrame:
    """
    In some cases address might be a JSON string/dict. If address.country is missing,
    try extracting it from address.
    """
    if "address.country" in df.columns:
        return df

    if "address" not in df.columns:
        return df

    def extract_country(x):
        try:
            if isinstance(x, str):
                obj = json.loads(x)
                return obj.get("country")
            if isinstance(x, dict):
                return x.get("country")
        except Exception:
            return pd.NA
        return pd.NA

    df["address.country"] = df["address"].apply(extract_country)
    return df


def fill_missing_numeric(df: pd.DataFrame) -> pd.DataFrame:
    for col in ["age", "height", "weight"]:
        if col in df.columns:
            missing = df[col].isna().sum()
            if missing > 0:
                median_val = df[col].median()
                df[col] = df[col].fillna(median_val)
                print(f"Filled {missing} missing values in '{col}' with median = {median_val}")
    return df


def basic_exploration(df: pd.DataFrame) -> None:
    print("Shape:", df.shape)
    print("\nColumns:\n", df.columns.tolist())
    print("\nData Types:\n", df.dtypes)
    print("\nMissing Values per Column (Top 20):\n", df.isnull().sum().sort_values(ascending=False).head(20))
    print("\nDuplicate Rows:", df.duplicated().sum())
    print("\nSummary Statistics (numeric):\n", df.describe().round(2))

    categorical_cols = ["gender", "bloodGroup", "eyeColor", "role", "address.country"]
    print("\n========== Value Counts (Top 10) ==========")
    for col in categorical_cols:
        if col in df.columns:
            print(f"\n--- {col} ---")
            print(df[col].value_counts(dropna=False).head(10))


def run_analysis(df: pd.DataFrame):
    avg_age = df["age"].mean()
    print("1) Average age:", round(avg_age, 2))

    avg_age_gender = df.groupby("gender")["age"].mean().sort_values(ascending=False)
    print("\n2) Average age by gender:\n", avg_age_gender.round(2))

    users_per_gender = df["gender"].value_counts()
    print("\n3) Number of users per gender:\n", users_per_gender)

    if "address.city" in df.columns:
        top_cities = df["address.city"].value_counts().head(10)
        print("\n4) Top 10 cities with most users:\n", top_cities)
    else:
        top_cities = None
        print("\n4) address.city column not found!")

    avg_height = df["height"].mean()
    avg_weight = df["weight"].mean()
    print("\n5) Average height:", round(avg_height, 2))
    print("   Average weight:", round(avg_weight, 2))

    corr_age_height = df["age"].corr(df["height"])
    corr_age_weight = df["age"].corr(df["weight"])
    print("\n6) Correlation:")
    print("   Age vs Height:", round(corr_age_height, 3))
    print("   Age vs Weight:", round(corr_age_weight, 3))

    return avg_age_gender, users_per_gender, top_cities


def save_outputs(df: pd.DataFrame, avg_age_gender, users_per_gender, top_cities) -> None:
    avg_age_gender.to_csv(os.path.join(OUTPUTS_DIR, "avg_age_by_gender.csv"), header=["avg_age"])
    users_per_gender.to_csv(os.path.join(OUTPUTS_DIR, "users_per_gender.csv"), header=["count"])

    if top_cities is not None:
        top_cities.to_csv(os.path.join(OUTPUTS_DIR, "top10_cities.csv"), header=["count"])

    summary_stats = df[["age", "height", "weight"]].describe().round(2)
    summary_stats.to_csv(os.path.join(OUTPUTS_DIR, "summary_stats_numeric.csv"))

    print("\n✅ Saved analysis outputs in outputs/ folder")


def save_plots(df: pd.DataFrame, avg_age_gender, top_cities) -> None:
    # Important for Docker: no interactive display needed
    sns.set(style="whitegrid")

    # Plot 1: Age Distribution
    plt.figure(figsize=(8, 5))
    sns.histplot(df["age"], kde=True)
    plt.title("Age Distribution")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "plot1_age_distribution.png"))
    plt.close()

    # Plot 2: Users per Gender
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x="gender")
    plt.title("Users per Gender")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "plot2_users_per_gender.png"))
    plt.close()

    # Plot 3: Average Age by Gender
    plt.figure(figsize=(6, 4))
    sns.barplot(x=avg_age_gender.index, y=avg_age_gender.values)
    plt.title("Average Age by Gender")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "plot3_avg_age_by_gender.png"))
    plt.close()

    # Plot 4: Age vs Height
    plt.figure(figsize=(7, 5))
    sns.scatterplot(data=df, x="age", y="height", hue="gender")
    plt.title("Age vs Height")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "plot4_age_vs_height.png"))
    plt.close()

    # Plot 5: Age vs Weight
    plt.figure(figsize=(7, 5))
    sns.scatterplot(data=df, x="age", y="weight", hue="gender")
    plt.title("Age vs Weight")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "plot5_age_vs_weight.png"))
    plt.close()

    # Plot 6: Top 10 Cities
    if top_cities is not None:
        plt.figure(figsize=(10, 5))
        sns.barplot(x=top_cities.index, y=top_cities.values)
        plt.xticks(rotation=45)
        plt.title("Top 10 Cities with Most Users")
        plt.tight_layout()
        plt.savefig(os.path.join(PLOTS_DIR, "plot6_top10_cities.png"))
        plt.close()

    print("\n✅ Plots saved in plots/ folder")


def main():
    ensure_dirs()

    # 1) Fetch from API -> Save to data/users_data.csv
    raw_df = fetch_users_from_api(limit=30)
    save_raw_csv(raw_df, CSV_PATH)

    # 2) Load CSV and clean
    df = load_csv(CSV_PATH)
    df = extract_country_if_needed(df)
    df = fill_missing_numeric(df)

    # 3) Explore + Analyze
    basic_exploration(df)
    avg_age_gender, users_per_gender, top_cities = run_analysis(df)

    # 4) Save outputs + plots
    save_outputs(df, avg_age_gender, users_per_gender, top_cities)
    save_plots(df, avg_age_gender, top_cities)

    print("\n✅ Project finished.")


if __name__ == "__main__":
    main()