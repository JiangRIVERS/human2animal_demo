'''
在原图上点取关键点，并返回坐标

@author: Jiang Rivers
'''

import cv2
import pandas as pd
import os

class operate:
    def __init__(self,name,color,r):
        """
        :param name: 动物名字
        :param color: 标注点的颜色
        :param r: 标注点的半径
        """
        self.name=name
        self.color=color
        self.num_list=[]
        self.x_list=[]
        self.y_list=[]
        self.r=r

    def start(self):
        self.img=cv2.imread('./mask/'+self.name+'.png')
        cv2.namedWindow('image', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
        self.num=0
        self.xlsx_path='./xlsx/'+self.name+'.xlsx'

        self.img=cv2.resize(self.img,(1024,1024))
        cv2.imwrite('./mask/'+self.name+'.png',self.img)

        cv2.imshow('image', self.img)
        cv2.setMouseCallback('image', self.label)
        cv2.waitKey(0) & 0xFF

    def label(self,event,x,y,flags, param):

        if event == cv2.EVENT_LBUTTONDOWN:
            self.num+=1
            no = '{}'.format(self.num)
            pre_img=self.img.copy()
            cv2.circle(self.img, (x, y), self.r, self.color, thickness = -1)
            cv2.putText(self.img, no, (x, y), cv2.FONT_HERSHEY_PLAIN,1.0, self.color, thickness = 1)
            cv2.imshow('image', self.img)
            self.num_list.append(self.num)
            self.x_list.append(x)
            self.y_list.append(y)

            label_k = cv2.waitKey(0) & 0xFF
            if label_k==ord('d'):
                cv2.imshow('image', pre_img)
                self.img=pre_img
                self.num-=1
                del self.num_list[-1]
                del self.x_list[-1]
                del self.y_list[-1]

            elif label_k==ord('s'):
                writer=pd.ExcelWriter(self.xlsx_path)
                dit={'No.':self.num_list,'coordinate_x':self.x_list,'coordinate_y':self.y_list}
                df=pd.DataFrame(dit)
                df.to_excel(writer,columns=['No.','coordinate_x','coordinate_y'],index=False,encoding='utf-8')
                writer.save()

        if event == cv2.EVENT_RBUTTONDOWN:
            quit_k = cv2.waitKey(0) & 0xFF
            if quit_k == ord('q'):
                #cv2.imwrite(self.saving_path + '/' + self.img_name + '.png', self.img)
                cv2.destroyAllWindows()


if __name__=='__main__':
    operate('dog',(0,255,0),5).start()