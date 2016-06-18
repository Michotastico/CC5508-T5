import numpy as np
from skimage import io
from skimage.filters import gaussian
from Models.Element import Element as Edge
import Functions


class Segmentation:
    def __init__(self, sigma, threshold, min_size):
        self.sigma = sigma
        self.k = threshold
        self.min_sz = min_size

    def segment_image(self, image_path):
        # Read image
        image = io.imread(image_path)
        size = image.shape
        width = size[0]
        height = size[1]

        # Smooth image
        original_type = image.dtype
        image = image.astype(np.float64)
        image = gaussian(image, self.sigma)

        # Build Graph
        edges = []
        for x in range(0, width):
            for y in range(0, height):
                if x < width - 1:
                    a = y * width + x
                    b = y * width + (x + 1)
                    w = Functions.diff(image, (x, y), (x + 1, y))
                    edges.append(Edge(w, a, b))

                if y < height - 1:
                    a = y * width + x
                    b = (y + 1) * width + x
                    w = Functions.diff(image, (x, y), (x, y + 1))
                    edges.append(Edge(w, a, b))

                if (x < width - 1) and (y < height - 1):
                    a = y * width + x
                    b = (y + 1) * width + (x + 1)
                    w = Functions.diff(image, (x, y), (x + 1, y + 1))
                    edges.append(Edge(w, a, b))

                if (x < width - 1) and (y > 0):
                    a = y * width + x
                    b = (y - 1) * width + (x + 1)
                    w = Functions.diff(image, (x, y), (x + 1, y - 1))
                    edges.append(Edge(w, a, b))

        graph = Functions.graph_segmentation(width * height, edges, self.k)

        for i in range(0, len(edges)):
            a = graph.find(edges[i].get_b())
            b = graph.find(edges[i].get_c())
            if (a != b) and ((graph.size_element(a) < self.min_sz) or (graph.size_element(b) < self.min_sz)):
                graph.join(a, b)

        return_image = image.astype(original_type)



        colors = []
        for i in range(0, width * height):
            colors.append(Functions.random_rgb())

        if len(size) == 3:
            flag = True
        else:
            flag = False

        for y in range(0, height):
            for x in range(0, width):
                value = graph.find(y * width + x)
                color = colors[value]
                if flag:
                    return_image[x, y, 0] = color[0]
                    return_image[x, y, 1] = color[1]
                    return_image[x, y, 2] = color[2]
                else:
                    color_value = Functions.rgb_to_gray(color)
                    return_image[x, y] = color_value

        return return_image
