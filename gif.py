import imageio
filenames=['cat1.png', 'cat2.png']
images=[]
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.imwrite('cat.gif', images, duration = 500, loop =0)