#coding:utf-8

import pandas as pd
import glob
from collections import defaultdict

# 対象フォルダパス
folder_path = ""
out_path = ""
# フォルダ内のファイル名リスト取得
file_paths = glob.glob(folder_path + "/*")

# 空のデータフレーム作成
data = pd.DataFrame(index=[], columns=[0,1,2,"set"])
# ファイルごとにデータフレーム取得、セット作成、結合
for file_path in file_paths:
    # データ取得
    temp_data = pd.read_csv(file_path, encoding="utf-8", header=None)
    col_data = []
    # 行ループし、セットのリスト作成
    for key, val in temp_data.iterrows():
        col_data.append(set([val[1], val[2]]))
    # データフレームへ列追加
    keys = {"set": col_data}
    temp_data = temp_data.assign(**keys)
    # 文字列に変換    
    temp_data = temp_data.astype('str')
    # "set"列の重複を削除
    temp_data = temp_data.drop_duplicates(["set"])
    # 縦に結合
    data = pd.concat([data, temp_data])

# インデックスの降り直し
data.index = range(data.shape[0])

# id_dict の作成
id_dict = defaultdict(str)
for _, val in data.iterrows():
    id_dict[val["set"]] += "," + val[0]
# word_dictの作成
word_dict = {val["set"]: [val[1], val[2]] for _, val in data.iterrows()}
# word_divtからデータフレーム作成
result_df = pd.DataFrame(index=[], columns=["id", "from", "to"])

# dict から df への変換
for key in word_dict.keys():
    #pdb.set_trace()
    result_df = result_df.append(pd.Series([id_dict[key][1:], word_dict[key][0], word_dict[key][1]], \
                                           index=["id", "from", "to"]), ignore_index=True)
# csv出力
result_df.to_csv(out_path + "/result.csv", header=False, index=False)