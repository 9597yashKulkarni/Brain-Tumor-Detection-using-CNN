# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 23:47:17 2018

@author: AKASHTA
"""

ino=39
img='HGG'+str(ino)+'.png'
from nilearn import plotting
display = plotting.plot_epi('Brats18_2013_12_1_t2.nii',output_file=img)
print(ino)
ino+=1

