'''
利用dlib标注人脸关键点及其坐标

@author: Jiang Rivers
'''
import numpy as np
import cv2
import dlib
import pandas as pd

class get_human_landmark:

    def __init__(self,name):
        '''
        :param name: 动物名
        '''
        self.name=name
        self.path='./img/a.png'


    def label(self):
        idx_list=[]
        x_list=[]
        y_list=[]

        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor('./shape_predictor_68_face_landmarks.dat')

        img = cv2.imread(self.path)
        img = cv2.resize(img, (1024,1024))

        cv2.imwrite('./img/1.png', img)
        img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        # 人脸数rects
        rects = detector(img_gray, 0) # 人脸检测bondingbox
        for i in range(len(rects)):
            landmarks = np.matrix([[p.x, p.y] for p in predictor(img,rects[i]).parts()])
            for idx, point in enumerate(landmarks):
                # 68点的坐标
                x=point[0, 0] # x坐标
                y=point[0, 1] # y坐标
                pos = (point[0, 0], point[0, 1])

                x_list.append(x)
                y_list.append(y)
                idx_list.append(idx+1)

                # 利用cv2.circle给每个特征点画一个圈，共68个
                cv2.circle(img, pos, 5, color=(0, 255, 0))
                # 利用cv2.putText输出1-68
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img, str(idx+1), pos, font, 0.8, (0, 0, 255), 1,cv2.LINE_AA)

        writer = pd.ExcelWriter('./xlsx/human_a.png.xlsx')
        dit = {'No.': idx_list, 'coordinate_x': x_list, 'coordinate_y': y_list}
        df = pd.DataFrame(dit)
        df.to_excel(writer, columns=['No.', 'coordinate_x', 'coordinate_y'], index=False, encoding='utf-8')
        writer.save()



        '''
        cv2.namedWindow("img", 2)
        cv2.imshow("img", img)
        k=cv2.waitKey(0) & 0xFF
        if k == 27:
        # wait for ESC key to exit
            writer = pd.ExcelWriter('./xlsx/human_a.png.xlsx')
            dit = {'No.': idx_list, 'coordinate_x': x_list, 'coordinate_y': y_list}
            df = pd.DataFrame(dit)
            df.to_excel(writer, columns=['No.', 'coordinate_x', 'coordinate_y'], index=False, encoding='utf-8')
            writer.save()
            cv2.destroyAllWindows()
        '''




if __name__=='__main__':
    get_human_landmark('cat').label()


