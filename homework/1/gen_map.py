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
#
# Update
# 10/4 初期値の確率を設定できるようにしておきました。
#
#--------------------------------------#


size = (sx, sy) = np.array([64, 64])  # マップのサイズです.動作が重い時は小さくしよう.
color_P = [ 60, 25, 10, 5]   #各色の出現確率[%]です.

many = np.prod(size)
map_data = np.random.randint(sum(color_P), size=many).reshape(size)
dire = [[0,1],[-1,0],[0,-1],[1,0]]

color_P_sum = 0
for i in range(len(color_P)):
  rang = np.logical_and( color_P_sum<=map_data, map_data<(color_P_sum+color_P[i])  )
  map_data[ rang] = i
  color_P_sum += color_P[i]


try:
  while True:
    for iy in range(sy):
      for ix in range(sx):
        first = True
        for d in np.random.permutation(dire):
	  px, py = (ix, iy) + d
	  if (0<=py and py<sy) and (0<=px and px<sx):
	    if first == True:
	      first = False
              map_data[iy, ix] = color = map_data[py, px]
            if not map_data[py, px] == color:
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
