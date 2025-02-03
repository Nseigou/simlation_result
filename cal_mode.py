import numpy as np
import pandas as pd

# CSVファイルのパスを指定（適宜変更）
file_path = "Simulation300/mobility112.tcl/Delay.txt"  # 実際のファイル名を指定してください

# CSVファイルを読み込む（1行目をヘッダーとして扱う）
df = pd.read_csv(file_path, header=0)

# 2行目（インデックス1）から251行目（インデックス250）を取得し、2~5列目を選択
df_subset = df.iloc[1:251, 1:5]  # 0-indexed（2列目～5列目）

# 1秒ごとの範囲を作成
min_value = df_subset.min().min() // 1  # 最小値（切り捨て）
max_value = df_subset.max().max() // 1 + 1  # 最大値（切り上げ）
bin_edges = np.arange(min_value, max_value + 1, 1)  # 1秒刻みの区間

# 最頻階級と2番目・3番目に多い階級を取得する関数
def get_top_three_frequent_bins(column):
    bin_counts = pd.cut(column, bins=bin_edges, right=False).value_counts()  # 各階級のデータ数を取得
    most_frequent_bin = bin_counts.index[0] if len(bin_counts) > 0 else np.nan  # 最頻階級
    most_frequent_count = bin_counts.iloc[0] if len(bin_counts) > 0 else np.nan  # その頻度

    second_most_frequent_bin = bin_counts.index[1] if len(bin_counts) > 1 else np.nan  # 2番目に多い階級
    second_most_frequent_count = bin_counts.iloc[1] if len(bin_counts) > 1 else np.nan  # その頻度

    third_most_frequent_bin = bin_counts.index[2] if len(bin_counts) > 2 else np.nan  # 3番目に多い階級
    third_most_frequent_count = bin_counts.iloc[2] if len(bin_counts) > 2 else np.nan  # その頻度

    return (most_frequent_bin, most_frequent_count, 
            second_most_frequent_bin, second_most_frequent_count, 
            third_most_frequent_bin, third_most_frequent_count)

# 各列ごとに最頻階級と2番目・3番目に多い階級を取得
top_three_frequent_bins = df_subset.apply(get_top_three_frequent_bins).apply(pd.Series)

# ✅ **列数に合わせてカラム名を設定**
expected_columns = ["最頻階級", "最頻回数", "2番目の階級", "2番目の回数", "3番目の階級", "3番目の回数"]

if top_three_frequent_bins.shape[1] == len(expected_columns):
    top_three_frequent_bins.columns = expected_columns
else:
    print("⚠️ 列数が一致しません！データの内容を確認してください。")


# 結果を表示
print("✅ 各列の最頻階級とその出現回数（上位3つ）:")
print(top_three_frequent_bins)
