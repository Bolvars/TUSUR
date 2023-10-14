from first_lab import dilate

def tests_images(path_pic:str,i:int,threshold:int, kernel:int):
    a = dilate.Intv(path_pic,threshold,kernel)
    a.savePic_array(f'images/outputImg/test{i}.jpg')
    print(int(a.get_time_work().microseconds))