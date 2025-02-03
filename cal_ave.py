import os

# フォルダー名
# folder_path = "Simulation_liar/mobility112_simTime=300.tcl/NDGPSR"
folder_path = "Simulation_liar/mobility112_simTime=250.tcl/NDGPSR"

# 3行目の数値を格納するリスト
throuput_line_values = []
pdr_line_values = []

# フォルダー内のすべてのファイルを処理
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # ファイルを開いて3行目の数値を取得
    with open(file_path, "r") as file:
        lines = file.readlines()
        if len(lines) >= 3:
            if (70 < float(lines[1].strip())):
                pdr_line_values.append(float(lines[1].strip()))
            if (6 < float(lines[0].strip())):
                throuput_line_values.append(float(lines[0].strip()))

# 平均値を計算
if throuput_line_values:
    throuput_average = sum(throuput_line_values) / len(throuput_line_values)
    throuput_max = max(throuput_line_values)
    throuput_min = min(throuput_line_values)
    print(f"スループットの平均値: {throuput_average:.5f}, 最大値: {throuput_max:.5f}, 最小値: {throuput_min:.5f}")

else:
    print("throuput:ファイルに適切なデータがありません。")

if pdr_line_values:
    pdr_average = sum(pdr_line_values) / len(pdr_line_values)
    pdr_max = max(pdr_line_values)
    pdr_min = min(pdr_line_values)
    print(f"pdrの平均値: {pdr_average:.5f}, 最大値: {pdr_max:.5f}, 最小値: {pdr_min:.5f}")
else:
    print("pdr:ファイルに適切なデータがありません。")