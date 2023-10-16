import numpy as np 
from PIL import Image
import cv2
from datetime import datetime
import concurrent.futures
from scipy.signal import convolve2d

class ImgConvB:
     
    def __init__(self, path_pict:str, kernel:np.ndarray, threads:int):
        self.kernel = kernel
        self.threads = threads
        self.array_pic = np.array_split(np.array(Image.open(path_pict)),self.threads)
        self.start_time = datetime.now()
    
    def inv_pixel(self,chunk:np.ndarray) -> np.ndarray:
        return 255 - chunk
    

    def convert(self,chunk:np.ndarray):
        for channel in range(chunk.shape[2]):
            chunk[:,:,channel] = convolve2d(self.inv_pixel(chunk[:,:,channel]), self.kernel, mode='same', boundary='wrap')

        return np.clip(chunk,0,255).astype(np.uint8)
    
    def savePic_array(self, path_name_pic:str):
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.threads) as executor:
            results = list(executor.map(self.convert,self.array_pic))

    
        comb_result = np.vstack(results)
        print(self.get_time_work().microseconds)
        Image.fromarray(comb_result).save(path_name_pic)
    
    def get_time_work(self):
        return datetime.now()-self.start_time
    