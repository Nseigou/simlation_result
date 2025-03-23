import pandas as pd

def remove_outliers_iqr(df):
    """
    四分位範囲（IQR）を用いて外れ値を除去する関数。
    """
    filtered_df = df.copy()
    for column in df.columns[1:]:  # 1列目（試行回数など）を除外
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        filtered_df[column] = df[column][(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    return filtered_df

# CSVファイルを読み込む（適宜ファイル名を変更してください）
file_path = "Simulation300/mobility74_185.tcl/Delay.txt"  # ユーザーのCSVファイル

df = pd.read_csv(file_path)
df = remove_outliers_iqr(df)

# 外れ値を除去した後の平均値を計算
mean_values = df.mean(numeric_only=True)

# 結果を表示
print("外れ値を除去した後の平均値:")
print(mean_values)

# 外れ値を除去した後の標準偏差を計算
std_values = df.std(numeric_only=True)

# 結果を表示
print("外れ値を除去した後の標準偏差:")
print(std_values)

max_values = df.max(numeric_only=True)
min_values = df.min(numeric_only=True)

# 結果を表示
print("外れ値を除去した後の最大値:")
print(max_values)

print("外れ値を除去した後の最小値:")
print(min_values)