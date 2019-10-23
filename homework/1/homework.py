#coding:utf-8
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


#--------------------------------------#
#地図生成プログラムです.
#以下のサイトを参考にしました.
#http://amagame.blog12.fc2.com/blog-entry-1989.html
#
#意外とそれっぽくはならなかった。
#中学生の時に作った時は凄いそれっぽかった(気がする).
#
#多分初期値の時点で、
#青:6割
#緑:3割
#灰:1割
#赤:少々
#みたいな事をしないといけない？
#--------------------------------------#


size = np.array([32, 32])  # マップのサイズです.動作が重い時は小さくしよう.

many = np.prod(size)
map_data = np.random.randint(5, size=many).reshape(size)
dire = [[0,1],[-1,0],[0,-1],[1,0]]

try:
  while True:
    for iy in range(1, size[1]-1):
      for ix in range(1, size[0]-1):
        np.random.shuffle(dire)
        dy, dx =dire[0]
        map_data[iy, ix] = color = map_data[iy+dy, ix+dx]
        for d in dire:
          dy, dx = d
          if not map_data[iy+dy, ix+dx] == color:
            break
        else:
          map_data[iy, ix] = color
    img_data = np.asarray(map_data)
    plt.imshow(img_data)
    plt.pause(0.01)

except KeyboardInterrupt:
  print("--------------------------------------------")
  print("keyboard interrupt. program finished  safety")
  print("--------------------------------------------")
