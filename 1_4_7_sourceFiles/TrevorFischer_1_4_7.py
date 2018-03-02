import PIL
import matplotlib.pyplot as plt
import os.path

'''Reading the image''' 
directory = os.path.dirname(os.path.abspath(\Desktop\Python_Files\1_4_x\1_4_7_sourceFiles\Pictures))
filename = os.path.join(directory, 'Buick.jpg, Cadillac.jpg, Chevrolet.jpg, GMC.jpg, Hummer.jpg, Saturn.jpg')
img = plt.imread(filename)

'''Open Image'''
fig, ax = plt.subplots(1, 1)
ax.imshow(img, interpolation='none')
fig.show()