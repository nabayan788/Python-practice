# %% Chapter2: データ分析の基本フロー
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "data" / "adult_income_dataset.csv"

# データ読み込み
df = pd.read_csv(CSV_PATH)

# %% 2-01 ファイルからデータを読み込む
print("===== head() =====")
print(df.head())

# %% 2-02 データフレームの基本情報を確認する
print("\n===== shape =====")
print(df.shape)

print("\n===== dtypes =====")
print(df.dtypes)

print("\n===== info() =====")
print(df.info())

# %% 2-03 データの基本操作
print("\n===== 列の抽出（age） =====")
print(df["age"].head())

print("\n===== 列名の確認 =====")
print(df.columns)

# %% 2-04 データを絞り込む
print("\n===== 年齢が30以上 =====")
print(df[df["age"] >= 30].head())

# %% 2-05 データをソートする
print("\n===== ageでソート =====")
print(df.sort_values(by="age").head())

print("\n===== age, education-numでソート =====")
print(df.sort_values(by=["age", "education-num"]).head())

# %% 2-06 欠損値の扱い
print("\n===== 欠損値数の確認 =====")
print(df.isnull().sum())

print("\n===== 欠損値を含む行の削除後 =====")
df_cleaned = df.dropna()
print(df_cleaned.isnull().sum())

# %% 2-07 グルーピング
print("\n===== 性別ごとの平均年齢 =====")
print(df.groupby("sex")["age"].mean())

# %% 2-08 データを可視化する
df["age"].plot(kind="hist")
# %% 2-09 簡単な統計分析

# 平均値の算出
mean_age = df["age"].mean()

# 中央値の算出
median_age = df["age"].median()

# 標準偏差の算出
std_age = df["age"].std()

print("平均値：" , mean_age)
print("中央値：" , median_age)
print("標準偏差：" , std_age)

# %%　2-10 データの統合

data1 = {
    "student_id" : [1, 2, 3, 4, 5],
    "name" : ["Alice", "Bob", "Charlie", "David", "Eva"],
    "age" : [12, 22, 20, 23, 21],
    "major" : [
        "Computer Sience",
        "Mathematics",
        "Physics",
        "Chemistry",
        "Biology"
    ]
}

df1 = pd.DataFrame(data1)

data2 = {
    "student_id" : [1, 2, 3, 4, 5],
    "gpa" : [3.5, 3.8, 3.2, 3.7, 3.6],
    "credits_completed" : [90, 100, 80, 110, 95]
}

df2 = pd.DataFrame(data2)

# データフレームの結合
merged_df = pd.merge(df1, df2, on = "student_id", how = "inner")
# 結合結果の表示
merged_df
# %%
