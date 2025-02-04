import matplotlib.pyplot as plt
import numpy as np

# 項目
categories = ['No Authentication', 'DSA', 'ECDSA', 'EdDSA']

# 各データの平均値、最大値、最小値
# include_liar simTime=250 Throughput
# mean_values = [4.18347, 7.64043, 7.50869, 7.32539]  # 平均値
# max_values = [4.44273, 7.9406, 7.9407, 7.66063]   # 最大値
# min_values = [4.0228, 6.95432, 6.61118, 6.61123]    # 最小値
# include_liar simTime=250 PDR
# mean_values = [48.2002, 88.1545, 86.6152, 84.48212]  # 平均値
# max_values = [51.2097, 91.6224, 91.6224, 88.34120]   # 最大値
# min_values = [46.371, 80.2412, 76.2848, 76.23970]    # 最小値
# simTime=300 PDR
# mean_values = [75.3124, 86.2848, 84.9965, 83.9748]  # 平均値
# max_values = [80.8725, 89.9329, 91.9463, 86.9128]   # 最大値
# min_values = [71.8121, 83.557, 80.8857, 81.2214]    # 最小値
# simTime=300 Overhead
# mean_values = [2694.3, 5982.8, 5384.2, 5364.5]  # 平均値
# max_values = [2777.1, 6054.1, 5557.6, 5411.5]   # 最大値
# min_values = [2608.4, 5933.4, 5318.6, 5315.4]
# simTime=300 Delay
# mean_values = [7.02477, 6.07848, 4.568, 5.78833]
# max_values = [19.7153, 25.3697, 22.5077, 17.7234]   # 最大値
# min_values = [2.24874, 2.0424, 2.09385, 2.23783]
# simTime=300 PDR node=185
# mean_values = [83.2086, 87.801, 86.8936, 87.3915]
# max_values = [85.5705, 90.2685, 91.6107, 89.2617]   # 最大値
# min_values = [81.5436, 84.8485, 83.557, 86.2416]
# simTime=300 memory
mean_values = [73742.9, 74832.9, 151699, 106226]
max_values = [74316, 75216, 152160, 106656]   # 最大値
min_values = [73324, 74360, 151144, 105680]



# エラーバー（平均値から最大・最小への範囲）
error_bars = [np.array(mean_values) - np.array(min_values), 
              np.array(max_values) - np.array(mean_values)]

# プロット
fig, ax = plt.subplots(figsize=(10, 7))
bars = ax.bar(categories, mean_values, width=0.4, yerr=error_bars, capsize=5, color=['gray', 'orange', 'skyblue', 'mediumseagreen'])

# グリッドを棒グラフの後ろに設定
ax.set_axisbelow(True)  
ax.grid(axis='y', linestyle='--', alpha=1)

# ラベル設定
# Throughput [kbps]
# Average packet delively rate [%]
# Overhead [KB]
ax.set_ylabel("# memory usage [KB]", fontsize=14) 
ax.set_xticklabels(categories, fontsize=12)
ax.set_ylim(0, max(max_values) + 20000)  # y軸の範囲調整 # 2 1000 20000
# ax.set_ylim(0, 100)  # y軸の範囲調整
# 各棒の下に平均値を表示
for bar, mean in zip(bars, mean_values):
    x = bar.get_x() + bar.get_width() / 2  # 棒の中央位置
    y = -10000  # 軸の下に配置するためのオフセット    # 0.8 7  500   10000         # 棒の下の少し空いた位置
    ax.text(x, y, f"{mean:.1f} KB", ha='center', va='top', fontsize=12, color='black')

# グラフを表示
plt.show()
