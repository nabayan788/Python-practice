
# ファイルを読み取れるように
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "data" / "adult_income_dataset.csv"

df = pd.read_csv(CSV_PATH)

# 先頭5行を表示
print("===== head() =====")
print(df.head())

# データの基本情報を表示
print("\n===== info() =====")
print(df.info())

# 統計情報を表示
print("\n===== describe() =====")
print(df.describe())



# %% 2-01 ファイルからデータを読み込む
import pandas as pd

df = pd.read_csv("date/adult_income_dataset.csv")
df

# 2-02 データフレームの基本情報を確認する
# %% 2-02-1 データフレームの先頭５行を表示する方法
df.head()

# %% 2-02-2 データフレームの行数と列数を表示する方法
df.shape

# %% 2-02-3 データフレームの各列のデータ型を確認する方法
df.dtypes

# %% 2-02 応用詳細情報を確認する
df.info()

# %% 2-03 データフレームの基本操作
age_columun = df["age"]
age_columun.head()

# %% 2-03 応用 列名の確認
print(df.columns)

# %% 2-04 データを絞り込む
df[df["age"] >= 30]

# %% 2-05 データをソートする
df_sorted = df.sort_values(by = "age")
df_sorted.head()

# %% 2-05 応用　複数項目でソート
df_sorted = df.sort_values(by = ["age", "education-num"])
df_sorted.head()

# 2-06 欠損値の扱い
# %% 欠損値数の確認
df.isnull().sum() 
# %% 欠損値を含む行の削除
df_cleaned = df.dropna
# %% 欠損値の再確認
df_cleaned.isnull().sum() 

# %% 2-07 グルーピングを理解する
mean_ages = df.groupby("sex")["age"].mean()
mean_ages

# %%
