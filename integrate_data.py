#coding:utf-8

import pandas as pd
import glob
from collections import defaultdict

# �Ώۃt�H���_�p�X
folder_path = ""
out_path = ""
# �t�H���_���̃t�@�C�������X�g�擾
file_paths = glob.glob(folder_path + "/*")

# ��̃f�[�^�t���[���쐬
data = pd.DataFrame(index=[], columns=[0,1,2,"set"])
# �t�@�C�����ƂɃf�[�^�t���[���擾�A�Z�b�g�쐬�A����
for file_path in file_paths:
    # �f�[�^�擾
    temp_data = pd.read_csv(file_path, encoding="utf-8", header=None)
    col_data = []
    # �s���[�v���A�Z�b�g�̃��X�g�쐬
    for key, val in temp_data.iterrows():
        col_data.append(set([val[1], val[2]]))
    # �f�[�^�t���[���֗�ǉ�
    keys = {"set": col_data}
    temp_data = temp_data.assign(**keys)
    # ������ɕϊ�    
    temp_data = temp_data.astype('str')
    # "set"��̏d�����폜
    temp_data = temp_data.drop_duplicates(["set"])
    # �c�Ɍ���
    data = pd.concat([data, temp_data])

# �C���f�b�N�X�̍~�蒼��
data.index = range(data.shape[0])

# id_dict �̍쐬
id_dict = defaultdict(str)
for _, val in data.iterrows():
    id_dict[val["set"]] += "," + val[0]
# word_dict�̍쐬
word_dict = {val["set"]: [val[1], val[2]] for _, val in data.iterrows()}
# word_divt����f�[�^�t���[���쐬
result_df = pd.DataFrame(index=[], columns=["id", "from", "to"])

# dict ���� df �ւ̕ϊ�
for key in word_dict.keys():
    #pdb.set_trace()
    result_df = result_df.append(pd.Series([id_dict[key][1:], word_dict[key][0], word_dict[key][1]], \
                                           index=["id", "from", "to"]), ignore_index=True)
# csv�o��
result_df.to_csv(out_path + "/result.csv", header=False, index=False)