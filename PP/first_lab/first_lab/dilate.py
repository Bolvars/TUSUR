import numpy as np 
from PIL import Image
import cv2
from datetime import datetime


class Intv:
    def __init__(self, path_pict:str, threshold:int, step:int):
        self.kernel = np.ones((step,step), np.uint8)
        self.array_pic = np.array(Image.open(path_pict))
        self.threshold = threshold
        self.start_time = datetime.now()

    def get_array_Iv(self) -> np.ndarray:
        return np.array(
                                    (self.array_pic[:,:,0]+
                                    self.array_pic[:,:,1]+
                                    self.array_pic[:,:,2])
                                    /3
                        )
    
    def get_fil_threshold(self):
        return np.where(self.get_array_Iv() < self.threshold,0,1)

    def pic_dilate(self):
        intv = self.get_fil_threshold()
        intv = intv.astype('uint8')
        return cv2.dilate(intv,self.kernel,iterations=1)

    def savePic_array(self, name_pict:str):
        resilt_array = (self.pic_dilate()*255).astype(np.uint8)
        resilt_array = cv2.cvtColor(resilt_array,cv2.COLOR_GRAY2RGB)
        Image.fromarray(resilt_array).save(name_pict)

    def get_time_work(self):
        return datetime.now()-self.start_time
    




