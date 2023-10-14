from second_lab import prgrm_A

def tests_images(path_pic:str,i:int,threshold:int, kernel:int, threads:int = 1):
    a = prgrm_A.Intv(path_pic,threshold,kernel,threads)
    a.savePic_array(f'images/outputImg/test{i}.jpg')
    print(int(a.get_time_work().microseconds))