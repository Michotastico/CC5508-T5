import numpy as np
from Models.Graph import Graph
from random import randint


def diff(matrix, a, b):
    value = matrix[a[0], a[1]] - matrix[b[0], b[1]]
    value = np.square(value)
    return np.sum(value)


def calculate_threshold(size, c):
    return float(c)/float(size)


def graph_segmentation(size, edges, k):
    # Sort edges
    edges = sorted(edges, key=lambda key: key.get_a())

    # Make a 'Graph'

    graph = Graph(size)

    threshold = []

    for i in range(0, size):
        threshold.append(calculate_threshold(1, k))

    for edge in edges:
        a = graph.find(edge.get_b())
        b = graph.find(edge.get_c())
        if a != b:
            if (edge.get_a() <= threshold[a]) and (edge.get_a() <= threshold[b]):
                graph.join(a, b)
                a = graph.find(a)
                threshold[a] = edge.get_a() + calculate_threshold(graph.size_element(a), k)

    return graph


def random_rgb():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return [r, g, b]


def rgb_to_gray(rgb):
    r_w = rgb[0] * 0.299
    g_w = rgb[1] * 0.587
    b_w = rgb[2] * 0.114
    return r_w + g_w + b_w
