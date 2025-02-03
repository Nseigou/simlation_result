# 必要なライブラリを再インポート
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# データの設定
protocols = ["No Authentication", "DSA", "ECDSA", "Ed25519"]
x_values = np.array([0, 37, 74, 112, 148, 185])  # 各データポイントのインデックス
y_values = np.array([
    [0, 0, 0, 0], 
    [14.1802, 69.9882, 55.0108, 24.4069],
    [50.5984, 267.433, 194.408, 89.2728],
    [110.405, 625.504, 436.926, 200.901],
    [196.971, 1172.57, 910.373, 431.346],
    [345.059, 1908.7, 1324.55, 635.155]
])

# 近似曲線の関数（2次関数）
def quadratic(x, a, b, c):
    return a * x**2 + b * x + c

# プロットの設定
plt.figure(figsize=(9, 6))
colors = ['gray', 'orange', 'skyblue', 'mediumseagreen']

for i, protocol in enumerate(protocols):
    y = y_values[:, i]

    # 2次関数のフィッティング
    params, _ = curve_fit(quadratic, x_values, y)
    x_fit_extended = np.linspace(min(x_values), max(x_values) + 20, 100)
    y_fit_extended = quadratic(x_fit_extended, *params) # 拡張した x 範囲で計算

    # データポイントと近似曲線をプロット
    plt.scatter(x_values, y, label=f"{protocol} (data)", color=colors[i])
    plt.plot(x_fit_extended, y_fit_extended, color=colors[i], label=f"{protocol} (fit)")

# 軸ラベルとタイトル

plt.ylabel("Simulation Time [s]", fontsize=14)
plt.legend()
plt.grid(axis='y')
plt.yticks(np.arange(0, np.max(y_values) + 400, 200))  # y軸のグリッドを200ごとに設定

# グラフを表示
plt.show()
