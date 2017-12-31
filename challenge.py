#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 18:26:38 2017

@author: Mingyang Zheng
"""

from PIL import Image
import requests
import numpy as np


list = []

for i in range(0, 5):
    res = requests.get('https://www.random.org/integers/?num=10000&min=0&max=255&col=1&base=10&format=plain&rnd=new')
    text = res.text
    nums = text.split('\n')[0: -1]
    vals = [int(i) for i in nums]
    list.extend(vals)

list = list[0: 49152]

array = np.array(list)
array2 = array.reshape(128, 128, 3).astype('uint8')

img = Image.fromarray(array2,"RGB")
img.show()
img.save('out.bmp')

