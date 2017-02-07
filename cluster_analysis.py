# クラスタ分析クラス
class cluster:
    # ライブラリのインポート
    import numpy as np
    import pandas as pd
    import random
    
    def __init__(self, dataset):
        # *************************************************
        # コンストラクタ
        # data : 入力データ
        # *************************************************
        # 個体リスト作成
        individuals = []
        for data in dataset:
            individuals.append(self.individual(data))
        self.individuals = individuals
            
    def fit(self, cluster_count, max_iter = 1000):
        # *************************************************
        # メイン処理
        # cluster_count : クラスタ数
        # max_iter      : 最大繰り返し回数
        # *************************************************
        self.cluster_count = cluster_count
        # 重心の初期化
        centroid = {k: random.choice(self.individuals).vec for k in range(cluster_count)}
        pre_centroid = {}
        # 最大繰り返し回数まで学習
        for i in range(max_iter):
            # 各個体のクラスタへの振り分け
            self.distribute(centroid)
            # 重心の再計算
            pre_centroid = centroid
            centroid = self.calc_centroid(centroid)
            # 重心が変わっていなければ終了
            if not self.is_change_centroid(centroid, pre_centroid):
                break
        # 分析結果の格納
        self.labels = [indi.cluster for indi in self.individuals]
       
    def distribute(self, centroid):
        # *************************************************
        # クラスタ振り分け
        # centroid : セントロイド
        # *************************************************
        for individual in self.individuals:
            individual.calc_cluster(centroid)
            
    def calc_centroid(self, centroid):
        # *************************************************
        # セントロイド計算
        # centroid : セントロイド
        # *************************************************
        for cluster in range(self.cluster_count):
            cluster_data = np.array([indi.vec for indi in self.individuals if indi.cluster == cluster])
            centroid[cluster] = cluster_data.mean(axis = 0)
        return centroid
    
    def is_change_centroid(self, centroid, pre_centroid):
        # *************************************************
        # セントロイドの変更確認
        # centroid     : セントロイド
        # pre_centroid : 前セントロイド
        # *************************************************
        res = True
        for index, _ in enumerate(centroid):
            if round(np.linalg.norm(centroid[index] - pre_centroid[index]), 3) == 0:
                res = False
        return res
         
    # 各個体クラス   
    class individual:
        def __init__(self, datalist):
            # *************************************************
            # コンストラクタ
            # datalist : １個体分のベクトル
            # *************************************************
            self.vec = datalist
            self.cluster = None
            
        def calc_cluster(self, centroid):
            # *************************************************
            # クラスタの計算
            # centroid : セントロイド
            # *************************************************
            cluster = 0
            dist = np.linalg.norm(self.vec - centroid[0])
            for key in centroid.keys():
                tempdist = np.linalg.norm(self.vec - centroid[key])
                if dist > tempdist:
                    cluster = key
                    dist = tempdist
            self.cluster = cluster