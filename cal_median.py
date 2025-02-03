import pandas as pd

# CSVファイルを読み込む（適切なファイル名を指定）
file_path = "Simulation300/mobility112.tcl/Delay.txt"  # ファイル名を適宜変更

# CSVファイルを読み込む（1行目をヘッダーとして扱い、インデックスをリセット）
df = pd.read_csv(file_path, header=0)

# 2行目（インデックス1）から251行目（インデックス250）を取得
df_subset = df.iloc[1:251, 1:5]  # 2列目～5列目を選択（0-indexed）

# 各列の統計量を計算（中央値、第一四分位数、第三四分位数）
stats = df_subset.describe(percentiles=[0.25, 0.5, 0.75]).loc[['25%', '50%', '75%']]

# 結果を表示
print("✅ 各列の統計量（Q1, Median, Q3）:")
print(stats)