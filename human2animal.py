'''
实现human2animal功能，所有图片应为png格式

@author: Jiang Rivers
'''


from human2animal_demo.get_human_landmark import get_human_landmark
from human2animal_demo.generate import generate
from human2animal_demo.match import create_gif

class hunman2animal:

    def __init__(self,animal_name,gif_name='/Users/jiangmingda/Desktop/a.gif',duration = 0.15):
        """
        :param animal_name: 动物名(例如:monkey)
        :param gif_name: gif保存路径
        :param duration: gif时间间隔
        """
        self.animal_name=animal_name
        self.gif_name=gif_name
        self.duration=duration

    def convert(self):
        get_human_landmark(self.animal_name).label()
        generate(self.animal_name).generate()
        create_gif(self.gif_name,self.animal_name,self.duration)

if __name__=='__main__':
    hunman2animal('dog').convert()


