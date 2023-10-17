import pandas as pd
import numpy as np

from os.path import abspath

from sklearn.cluster import KMeans
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import pairwise_distances

import concurrent.futures

class Kmean_cluster:
    def __init__(self, path_to_csv:str, sep,count_cluster:int, threads:int):
        self.Df = pd.read_csv(path_to_csv, sep=sep)
        self.countClusters = count_cluster
        self.mb_index = None
        self.threads = threads
        
    def getDfwithAxis(self, *args:str)->pd.DataFrame:
        try:
            print(self.Df[[*args]].isnull)
            return self.Df[[*args]]
        except Exception as e:
            print(e)
    
    def normalization(self,*args:str)-> pd.DataFrame:
        imputer = SimpleImputer(strategy='mean')
        selcted_features = imputer.fit_transform(self.getDfwithAxis(*args))
        scaler = MinMaxScaler()
        return scaler.fit_transform(selcted_features)
    
    def calculateMB(self,X,labels,centers):
        intradist = 0
        for i in range(len(centers)):
            cluster_points = X[labels == i]
            center = centers[i]
            intradist += np.sum(pairwise_distances(cluster_points, [center]))
        
        # Рассчитываем межкластерное расстояние
        interdist = 0
        for i in range(len(centers)):
            for j in range(i + 1, len(centers)):
                interdist += np.linalg.norm(centers[i] - centers[j])
        
        # Рассчитываем MB-индекс
        mb_index = intradist / interdist
        
        return mb_index

    def kMeansClstr(self,*args:str):
        kmeans = KMeans(n_clusters=self.countClusters, random_state=0)
        scaled_features = self.normalization(*args)
        clusters = kmeans.fit_predict(scaled_features)
        self.Df[f"Cluster{self.countClusters}"] = clusters

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.threads) as executor:
            results = list(executor.map(self.calculateMB,[scaled_features,clusters,kmeans.cluster_centers_]))
        self.mb_index = self.calculateMB(scaled_features,clusters,kmeans.cluster_centers_)

    def getMB(self):
        return self.mb_index

    
    
            
DfPatients = Kmean_cluster(abspath("../BD-Patients.csv"),',',3)
print(DfPatients.kMeansClstr("HCT_mean","Urine_mean"))
print(DfPatients.mb_index)