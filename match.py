"""
匹配生成gif&&渐入渐出效果

@author: Jiang Rivers
"""
import imageio
import os
import os.path
import cv2

def create_gif(gif_name,name, duration = 0.3):
    '''
    :param: gif_name: gif保存路径
    :param: name: 动物名
    :param: duration: gif 图像时间间隔
    '''
    def sortkey(elem): # 根据文件名前数字大小排序
        return int(elem.split('.')[0])

    frames = []
    pngFiles = os.listdir('./img')
    pngFiles.remove('.DS_Store')
    pngFiles.remove('a.png')
    pngFiles.sort(key=sortkey) # 排序

    for image_name in pngFiles:
        # 读取 png 图像文件
        frames.append(imageio.imread('./img/'+image_name))
    # 保存为 gif
    over_frames=[]

    monkey=imageio.imread('./mask/'+name+'.png')

    over_frames.append(cv2.addWeighted(monkey,0,frames[0],1,0))
    over_frames.append(cv2.addWeighted(monkey, 0.2, frames[1], .8, 0))
    over_frames.append(cv2.addWeighted(monkey, 0.3, frames[2], .7, 0))
    over_frames.append(cv2.addWeighted(monkey, 0.4, frames[3], .6, 0))
    over_frames.append(cv2.addWeighted(monkey, 0.5, frames[4], .5, 0))
    over_frames.append(cv2.addWeighted(monkey, 0.6, frames[5], .4, 0))
    over_frames.append(cv2.addWeighted(monkey, 0.7, frames[6], .3, 0))
    over_frames.append(cv2.addWeighted(monkey, 0.8, frames[7], .2, 0))
    over_frames.append(cv2.addWeighted(monkey, 0.9, frames[8], .1, 0))
    over_frames.append(cv2.addWeighted(monkey, 1, frames[9], 0, 0))

    imageio.mimsave(gif_name,over_frames,'GIF',duration = duration)

if __name__ == "__main__":
    create_gif('a.gif','cat',0.2)
