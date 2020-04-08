'''
生成10张经过MLS的图片，用于作为frame生成gif

@author: Jiang Rivers
'''


from human2animal_demo.MLS import mls_affine_deformation,mls_rigid_deformation
import pandas as pd
import cv2
import numpy as np

class generate:

    def __init__(self,name):
        """
        :param name: 动物名
        """
        self.name=name

    def generate(self):
        _first=pd.read_excel('./xlsx/human_a.png.xlsx',usecols=[1,2])
        _first=_first.values.tolist()
        first=[_first[0],_first[2],_first[5],_first[8],_first[11],_first[14],_first[16],_first[17],_first[19],_first[21],_first[22]
               ,_first[24],_first[26],_first[28],_first[30],_first[36],_first[39],_first[43],_first[45],_first[49],_first[54 ],_first[51],_first[57]]

        _end=pd.read_excel('./xlsx/'+self.name+'.xlsx',usecols=[1,2])
        _end=_end.values.tolist()
        end= [_end[0], _end[1], _end[2], _end[3], _end[4], _end[5], _end[6], _end[7],_end[8],_end[9],_end[10],
              _end[11],_end[12],_end[13],_end[14],_end[15],_end[16],_end[17],_end[18],_end[19],_end[20],_end[21],_end[22]]
        second,third,forth,fifth,sixth,seventh,eighth,ninth=[],[],[],[],[],[],[],[]


        image=cv2.imread('./img/1.png')

        for idx in range(len(first)):
            second_, third_, forth_, fifth_, sixth_, seventh_, eighth_, ninth_ = self.MLS_three_points(first[idx], end[idx])
            second.append(second_)
            third.append(third_)
            forth.append(forth_)
            fifth.append(fifth_)
            sixth.append(sixth_)
            seventh.append(seventh_)
            eighth.append(eighth_)
            ninth.append(ninth_)

        self.MLS_img(first, second, image, 2)
        self.MLS_img(first, third, image, 3)
        self.MLS_img(first, forth, image, 4)
        self.MLS_img(first, fifth, image, 5)
        self.MLS_img(first, sixth, image, 6)
        self.MLS_img(first, seventh, image, 7)
        self.MLS_img(first, eighth, image, 8)
        self. MLS_img(first, ninth, image, 9)
        self. MLS_img(first, end, image, 10)

    @staticmethod
    def MLS(p,q,image):
        p = np.array(p)
        q = np.array(q)
        result_img = mls_affine_deformation(image,p,q)
        return result_img

    @staticmethod
    def MLS_three_points(first_, end_):
        first_x = first_[0]
        first_y = first_[1]
        end_x = end_[0]
        end_y = end_[1]
        dis_x = (end_x - first_x) / 10
        dis_y = (end_y - first_y) / 10

        second_ = [first_x + dis_x, first_y + dis_y]
        third_ = [first_x + 2 * dis_x, first_y + 2 * dis_y]
        forth_ = [first_x + 3 * dis_x, first_y + 3 * dis_y]
        fifth_ = [first_x + 4 * dis_x, first_y + 4 * dis_y]
        sixth_ = [first_x + 5 * dis_x, first_y + 5 * dis_y]
        seventh_ = [first_x + 6 * dis_x, first_y + 6 * dis_y]
        eighth_ = [first_x + 7 * dis_x, first_y + 7 * dis_y]
        ninth_ = [first_x + 8 * dis_x, first_y + 8 * dis_y]

        return second_, third_, forth_, fifth_, sixth_, seventh_, eighth_, ninth_


    def MLS_img(self,pre, pos, image,num):
        img = self.MLS(pre, pos, image)
        cv2.imwrite('./img/' + str(num) + '.png', img)








