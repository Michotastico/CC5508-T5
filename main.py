from algorithm.Segmentation import Segmentation
from skimage import io
import matplotlib.pyplot as plt
from datetime import datetime

images = [{'original': 'Images/gs_image_1.jpg', 'result': 'Images/Result1.png'},
          {'original': 'Images/gs_image_2.jpg', 'result': 'Images/Result2.png'},
          {'original': 'Images/gs_image_3.jpg', 'result': 'Images/Result3.png'},
          {'original': 'Images/gs_image_4.jpg', 'result': 'Images/Result4.png'},
          {'original': 'Images/gs_image_5.png', 'result': 'Images/Result5.png'},
          {'original': 'Images/Img6.jpg', 'result': 'Images/Result6.png'},
          {'original': 'Images/Img7.jpg', 'result': 'Images/Result7.png'},
          {'original': 'Images/Img8.png', 'result': 'Images/Result8.png'},
          {'original': 'Images/Img9.png', 'result': 'Images/Result9.png'},
          {'original': 'Images/Img10.jpg', 'result': 'Images/Result10.png'},
          {'original': 'Images/Img11.png', 'result': 'Images/Result11.png'},]
sigma = 0.8
k = 500
min_sz = 20

segmentation = Segmentation(sigma, k, min_sz)
times = []

for image in images:
    print 'Working on', image['original']

    original = io.imread(image['original'])
    init_time = datetime.now()
    print init_time
    segmented_image = segmentation.segment_image(image['original'])
    end_time = datetime.now()
    print end_time
    delta_time = str(end_time - init_time)
    times.append({'image': image['original'], 'elapsed_time': delta_time})
    fig, (img, dif) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

    img.imshow(original)

    dif.imshow(segmented_image)

    plt.savefig(image['result'], bbox_inches='tight')
    print 'Comparative stored'

text = 'Time table\nSigma: ' + str(sigma) + '; Threshold: ' + str(k) + '\n'
for time in times:
    line = 'Image: ' + time['image'] + '; Elapsed time: ' + time['elapsed_time'] + '\n'
    text += line
text_file = open('Images/Results.txt', "w+")
text_file.write(text)
text_file.close()
