from second_lab import prgrm_A
from second_lab import prgrm_B
from numpy import ndarray

def tests_images_A(path_pic:str,i:int,threshold:int, kernel:int, threads:int = 1):
    a = prgrm_A.Intv(path_pic,threshold,kernel,threads)
    a.savePic_array(f'images/outputImg/test_A{i}.jpg')
    print(int(a.get_time_work().microseconds))

def tests_images_B(path_pic:str,i:int, kernel:ndarray, threads:int = 1):
    b = prgrm_B.ImgConvB(path_pic,kernel,threads)
    b.savePic_array(f'images/outputImg/test_B{i}.jpg')
