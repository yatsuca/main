# �N���X�^���̓N���X
class cluster:
    # ���C�u�����̃C���|�[�g
    import numpy as np
    import pandas as pd
    import random
    
    def __init__(self, dataset):
        # *************************************************
        # �R���X�g���N�^
        # data : ���̓f�[�^
        # *************************************************
        # �̃��X�g�쐬
        individuals = []
        for data in dataset:
            individuals.append(self.individual(data))
        self.individuals = individuals
            
    def fit(self, cluster_count, max_iter = 1000):
        # *************************************************
        # ���C������
        # cluster_count : �N���X�^��
        # max_iter      : �ő�J��Ԃ���
        # *************************************************
        self.cluster_count = cluster_count
        # �d�S�̏�����
        centroid = {k: random.choice(self.individuals).vec for k in range(cluster_count)}
        pre_centroid = {}
        # �ő�J��Ԃ��񐔂܂Ŋw�K
        for i in range(max_iter):
            # �e�̂̃N���X�^�ւ̐U�蕪��
            self.distribute(centroid)
            # �d�S�̍Čv�Z
            pre_centroid = centroid
            centroid = self.calc_centroid(centroid)
            # �d�S���ς���Ă��Ȃ���ΏI��
            if not self.is_change_centroid(centroid, pre_centroid):
                break
        # ���͌��ʂ̊i�[
        self.labels = [indi.cluster for indi in self.individuals]
       
    def distribute(self, centroid):
        # *************************************************
        # �N���X�^�U�蕪��
        # centroid : �Z���g���C�h
        # *************************************************
        for individual in self.individuals:
            individual.calc_cluster(centroid)
            
    def calc_centroid(self, centroid):
        # *************************************************
        # �Z���g���C�h�v�Z
        # centroid : �Z���g���C�h
        # *************************************************
        for cluster in range(self.cluster_count):
            cluster_data = np.array([indi.vec for indi in self.individuals if indi.cluster == cluster])
            centroid[cluster] = cluster_data.mean(axis = 0)
        return centroid
    
    def is_change_centroid(self, centroid, pre_centroid):
        # *************************************************
        # �Z���g���C�h�̕ύX�m�F
        # centroid     : �Z���g���C�h
        # pre_centroid : �O�Z���g���C�h
        # *************************************************
        res = True
        for index, _ in enumerate(centroid):
            if round(np.linalg.norm(centroid[index] - pre_centroid[index]), 3) == 0:
                res = False
        return res
         
    # �e�̃N���X   
    class individual:
        def __init__(self, datalist):
            # *************************************************
            # �R���X�g���N�^
            # datalist : �P�̕��̃x�N�g��
            # *************************************************
            self.vec = datalist
            self.cluster = None
            
        def calc_cluster(self, centroid):
            # *************************************************
            # �N���X�^�̌v�Z
            # centroid : �Z���g���C�h
            # *************************************************
            cluster = 0
            dist = np.linalg.norm(self.vec - centroid[0])
            for key in centroid.keys():
                tempdist = np.linalg.norm(self.vec - centroid[key])
                if dist > tempdist:
                    cluster = key
                    dist = tempdist
            self.cluster = cluster