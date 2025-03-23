# 必要なライブラリを再インポート
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# データの設定
protocols = ["No Authentication", "ECDSA", "EdDSA"]# ここいじる
# x_values = np.array([0, 37, 74, 112, 148, 185])  # 各データポイントのインデックス
x_values = np.array([0, 37, 74, 112, 148, 185])
y_values = np.array([
    # simulation time
    [0, 0, 0], 
    [14.1802, 55.0108, 24.4069],
    [50.5984, 194.408, 89.2728],
    [110.405, 436.926, 200.901],
    [196.971, 910.373, 431.346],
    [345.059, 1324.55, 635.155]
    # memory
    # [68000, 68000, 68000],
    # [70939.4,  93749.3, 80647.1],
    # [74089.7,  151853, 106442],
    # [77070.1,  254247, 151401],
    # [80749.9,  409965, 219102],
    # [84548.1,  560753, 285191]
])

# 近似曲線の関数（2次関数）
def quadratic(x, a, b, c):
    return a * x**2 + b * x + c

# 近似曲線の関数（1次関数）
def linear(x, a, b):
    return a * x + b

# プロットの設定
plt.figure(figsize=(9, 6))
colors = ['gray', 'skyblue', 'orange']# ここいじる

plt.legend(fontsize=30)
for i, protocol in enumerate(protocols):
    y = y_values[:, i]

    # 2次関数のフィッティング
    params, _ = curve_fit(quadratic, x_values, y) 
    x_fit_extended = np.linspace(min(x_values), max(x_values) + 20, 100)
    y_fit_extended = quadratic(x_fit_extended, *params) 

    # データポイントと近似曲線をプロット
    plt.scatter(x_values, y, label=f"{protocol}", color=colors[i])
    plt.plot(x_fit_extended, y_fit_extended, color=colors[i])

# 軸ラベルとタイトル
plt.xlabel("Number of Nodes", fontsize=14)
plt.ylabel("Simlation Time [s]", fontsize=14) #ここいじる Memory Usage [KB]  Simlation Time [s]
plt.legend()
plt.grid(axis='y')
plt.yticks(np.arange(0, np.max(y_values) + 200, 200))  # y軸のグリッドを200ごとに設定 ここもいじる
# momory=40000, 100000
# sim=200, 200
# グラフを表示
plt.show()
