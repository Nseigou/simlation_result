import matplotlib.pyplot as plt
import numpy as np

# 項目
categories = ['No Authentication', 'ECDSA', 'EdDSA']

# 各データの平均値、最大値、最小値
# include_liar simTime=250 Throughput
# mean_values = [4.18347, 7.50869, 7.32539]  # 平均値
# max_values = [4.44273, 7.9407, 7.66063]   # 最大値
# min_values = [4.0228, 6.61118, 6.61123]    # 最小値
# include_liar simTime=250 PDR
# mean_values = [48.2002,  86.6152, 84.48212]  # 平均値
# max_values = [51.2097, 91.6224, 88.34120]   # 最大値
# min_values = [46.371, 76.2848, 76.23970]    # 最小値
# simTime=300 Overhead
# mean_values = [2694.3,  5384.2, 5364.5]  # 平均値
# max_values = [2777.1, 5557.6, 5411.5]   # 最大値
# min_values = [2608.4,  5318.6, 5315.4]
# simTime=300 PDR node=185
mean_values = [83.2086,  86.8936, 87.3915]
max_values = [85.5705,  91.6107, 89.2617]   # 最大値
min_values = [81.5436,  83.557, 86.2416]
# simTime=300 delay node=74_185
# mean_values = [6.162969,  5.546580, 5.313161]  # 平均値
# max_values = [15.31670,  10.64250, 10.18950]   # 最大値
# min_values = [2.24950,  2.1870, 2.30275]





# エラーバー（平均値から最大・最小への範囲）
error_bars = [np.array(mean_values) - np.array(min_values), 
              np.array(max_values) - np.array(mean_values)]

# プロット
fig, ax = plt.subplots(figsize=(10, 7))
bars = ax.bar(categories, mean_values, width=0.3, yerr=error_bars, capsize=5, color=['gray', 'skyblue', 'orange'])

# グリッドを棒グラフの後ろに設定
ax.set_axisbelow(True)  
ax.grid(axis='y', linestyle='--', alpha=1)

# ラベル設定
# Throughput [kbps]
# Packet delively rate [%]
# Overhead [KB]
# memory usage [KB]
# Delay [ms]
ax.set_ylabel("Packet delively rate [%]", fontsize=14) #ここいじる
ax.set_xticklabels(categories, fontsize=12)
# ax.set_ylim(0, max(max_values) + 3)  # y軸の範囲調整 # 2 1000 20000  # ここいじる
ax.set_ylim(0, 100)  # y軸の範囲調整
# 各棒の下に平均値を表示
for bar, mean in zip(bars, mean_values):
    x = bar.get_x() + bar.get_width() / 2  # 棒の中央位置
    y = -7 # 軸の下に配置するためのオフセット    # -0.8 -7  -500   -10000         # 棒の下の少し空いた位置   # ここいじる
    ax.text(x, y, f"{mean:.2f} %", ha='center', va='top', fontsize=12, color='black')  # ここいじる

# グラフを表示
plt.show()
