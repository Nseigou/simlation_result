import matplotlib.pyplot as plt
import pandas as pd
import os

# ✅ ファイルの絶対パスを指定
file_path = "Simulation300\mobility112.tcl\Delay.txt"

# ✅ ファイルが存在するか確認
if not os.path.exists(file_path):
    print(f"エラー: ファイルが見つかりません -> {file_path}")
    exit()

# ✅ CSVファイルを読み込む（空白やタブ区切りに対応）
df = pd.read_csv(file_path, header=0)

# ✅ 2行目（インデックス1）から251行目（インデックス250）を取得し、2~5列目を選択
df_subset = df.iloc[1:251, 1:5]  # 2列目～5列目（0-indexed）

# ✅ 箱ひげ図のプロット
plt.figure(figsize=(8, 6))
df_subset.boxplot(grid=True, patch_artist=True, boxprops=dict(facecolor="lightblue"))

# ✅ ラベルの設定
plt.ylabel("Delay [ms]")
plt.title("Delay Box Plot")
plt.xticks(rotation=15)  # X軸ラベルが長い場合は回転
plt.grid(axis='y', linestyle='--', alpha=0.7)

# ✅ グラフを表示
plt.show()
