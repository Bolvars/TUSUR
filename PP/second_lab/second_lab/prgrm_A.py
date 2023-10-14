import numpy as np 
from PIL import Image
import cv2
from datetime import datetime
import concurrent.futures


class Intv:
    def __init__(self, path_pict:str, threshold:int, step:int, threads:int):
        self.kernel = np.ones((step,step), np.uint8)
        self.threshold = threshold
        self.threads = threads
        self.array_pic = np.array_split(np.array(Image.open(path_pict)),self.threads)
        self.start_time = datetime.now()

    def get_array_Iv(self,chunk:np.ndarray) -> np.ndarray:
        return np.array(
                        (chunk[:,:,0]+chunk[:,:,1]+chunk[:,:,2])/3
                    )
    
    def get_fil_threshold(self,chunk:np.ndarray) -> np.ndarray:
        return np.where(self.get_array_Iv(chunk) < self.threshold,0,1)

    def pic_dilate(self,chunk:np.ndarray):
        intv = self.get_fil_threshold(chunk)
        intv = intv.astype('uint8')
        return cv2.dilate(intv,self.kernel,iterations=1)

    def savePic_array(self, name_pict:str):
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.threads) as executor:
            results = list(executor.map(self.pic_dilate,self.array_pic))

        comb_result = np.concatenate(results)*255
        comb_result = cv2.cvtColor(comb_result.astype(np.uint8), cv2.COLOR_GRAY2RGB)
        Image.fromarray(comb_result).save(name_pict)

    def get_time_work(self):
        return datetime.now()-self.start_time
    


def main(path_pic:str,i:int,threshold:int, kernel:int,threads:int):
    a = Intv(path_pic,threshold,kernel,threads=1)
    a.savePic_array(f'test{i}.jpg')
    print(int(a.get_time_work().microseconds))