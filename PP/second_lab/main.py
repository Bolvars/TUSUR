from tests import test_images as t
import os

t.tests_images(os.path.abspath("images/inputImg/168905579817222341.jpg"),1,77,3)
t.tests_images(os.path.abspath("images/inputImg/315510.jpg"),2,77,3,4)
t.tests_images(os.path.normpath(os.path.abspath("images/inputImg/a3d83d552a2b4caf875e322736bc.jpg")),3,77,3,6)