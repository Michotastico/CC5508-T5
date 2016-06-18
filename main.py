from algorithm.Segmentation import Segmentation
from skimage import io
import matplotlib.pyplot as plt

sigma = 0.5
k = 500
min_sz = 20

segmentation = Segmentation(sigma, k, min_sz)

image_path = 'Images/Img11.png'
image = io.imread(image_path)

segmented_image = segmentation.segment_image(image_path)

fig, (img, dif) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

img.imshow(image)

dif.imshow(segmented_image)

plt.savefig('Images/Result11.png', bbox_inches='tight')
plt.show()