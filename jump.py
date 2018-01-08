import numpy as np     # installed with matplotlib
import matplotlib.pyplot as plt
from math import radians
import os
from PIL import Image
import math
import time

DISTANCE = 30

def pullImg():
    os.chdir('C:\\Users\\tf\\Desktop\\platform-tools') 
    os.system('adb shell /system/bin/screencap -p /sdcard/screenshot.png')
    os.system('adb pull /sdcard/screenshot.png C:/Users/tf/Desktop/screenshot.png')

def touch(time):
    command = 'adb shell input swipe 200 200 200 200 ' + str(time)
    os.chdir('C:\\Users\\tf\\Desktop\\platform-tools') 
    os.system(command)

def calculate(imgPath):
    img = Image.open(imgPath)
    img_array = img.load()
    width = img.size[0]
    height = img.size[1]
    dest_y, dest_x = findDest(img_array, height, width)
    start_y, start_x = findStart(img_array, height, width)
    dist = math.sqrt((start_x - dest_x) * (start_x - dest_x) + (start_y - dest_y) * (start_y - dest_y))
    presstime = int(dist * 1.35)
    print 'start:', start_x, start_y
    print 'dest:', dest_x, dest_y
    print 'dist:', dist
    print 'press time:', presstime
    return presstime

def findDest(img_array, height, width):
    start_r,start_g,start_b, start_a = img_array[100,600]
    head_r,head_g,head_b,head_a = [73,61,99,0]
    i = 600
    i1 = 600
    i2 = 600
    j = 100
    findj = False
    for i in range(600, height):
        if not findj:
            for j in range(100, width):
                cur_r,cur_g,cur_b,cur_a = img_array[j,i]
                dist = abs(start_r - cur_r) + abs(start_g - cur_g) + abs(start_b - cur_b)
                if dist > DISTANCE and (abs(head_r - cur_r) + abs(head_g - cur_g) + abs(head_b - cur_b) > DISTANCE):
                    findj = True
                    i1 = i
                    break
        else:
            cur2_r,cur2_g,cur2_b,cur2_a = img_array[j,i]
            dist2 = abs(cur2_r - cur_r) + abs(cur2_g - cur_g) + abs(cur2_b - cur_b)
            if dist2 > DISTANCE:
                cur3_r,cur3_g,cur3_b,cur3_a = img_array[j,i + 30]
                dist3 = abs(cur3_r - cur_r) + abs(cur3_g - cur_g) + abs(cur3_b - cur_b)
                if dist3 > DISTANCE:
                    cur4_r,cur4_g,cur4_b,cur4_a = img_array[j,i + 180]
                    dist4 = abs(cur4_r - cur_r) + abs(cur4_g - cur_g) + abs(cur4_b - cur_b)
                    if dist4 > DISTANCE:
                        i2 = i
                        break
                    else:
                        return [i + 70, j]
                else:
                    return [i + 15, j]
          
                

    return [(i1 + i2) / 2, j]
   
def findStart(img_array, height, width):
    start_r,start_g,start_b, start_a = [73,61,99,0]
    i,j = [600,100]
    for i in range(600,height):
        for j in range(100,width):
            cur_r,cur_g,cur_b,cur_a = img_array[j,i]
            dist = abs(start_r - cur_r) + abs(start_g - cur_g) + abs(start_b - cur_b)
            if dist < DISTANCE:
                return [i + 190, j]
    return [i, j]
       
def main():
    while(1):
        pullImg()
        presstime = int(calculate('C:/Users/tf/Desktop/screenshot.png'))
        touch(presstime)
        time.sleep(2)

def test():
    while 1:
        x = raw_input()
        if x == '1':
            pullImg()
            presstime = int(calculate('C:/Users/tf/Desktop/screenshot.png'))
            image = plt.imread('C:/Users/tf/Desktop/screenshot.png')
            plt.imshow(image)
            plt.show()  
            touch(presstime)

main()
#test()
