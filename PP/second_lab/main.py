from tests import test_images as t
import os

KERNEL_INCREASE_CONTRAST = [
                            [0, 0,  0,  0,  0],
                            [0, 0,  -1, 0,  0],
                            [0, -1, 5,  -1, 0],
                            [0, 0,  -1, 0,  0],
                            [0, 0,  0,  0,  0]
                            ]

#t.tests_images_A(os.path.abspath("images/inputImg/2697944.jpg"),1,77,1)
#t.tests_images_A(os.path.normpath(os.path.abspath("images/inputImg/dom_les_sneg_156611_3200x2400.jpg")),3,77,3,1)
#t.tests_images_A(os.path.abspath("images/inputImg/b602dea6e1c4207681daf2c95fd608f1.jpg"),2,77,3,1)

t.tests_images_B(os.path.abspath("images/inputImg/2697944.jpg"),1,KERNEL_INCREASE_CONTRAST,12)
t.tests_images_B(os.path.normpath(os.path.abspath("images/inputImg/dom_les_sneg_156611_3200x2400.jpg")),2,KERNEL_INCREASE_CONTRAST,12)
t.tests_images_B(os.path.abspath("images/inputImg/b602dea6e1c4207681daf2c95fd608f1.jpg"),3,KERNEL_INCREASE_CONTRAST,12)