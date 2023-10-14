from first_lab.t import Intv

def main(path_pic:str,i:int,threshold:int, kernel:tuple[int,int]):
    a = Intv(path_pic,threshold,kernel)
    a.savePic_array(f'test{i}.jpg')
    print(int(a.get_time_work().microseconds))