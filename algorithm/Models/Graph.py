from Element import Element


class Graph:
    def __init__(self, elements_size):
        self.size = elements_size
        self.elements = []
        for i in range(0, self.size):
            self.elements.append(Element(0, i, 1))

    def size_element(self, x):
        value = self.elements[x].get_c()
        return value

    def num_sets(self):
        return self.size

    def find(self, element):
        index = element
        while index != self.elements[index].get_b():
            index = self.elements[index].get_b()
        self.elements[element].set_b(index)
        return index

    def join(self, x, y):
        if self.elements[x].get_a() > self.elements[y].get_a():
            self.elements[y].set_b(x)
            new_value = self.elements[x].get_c() + self.elements[y].get_c()
            self.elements[x].set_c(new_value)
        else:
            self.elements[x].set_b(y)
            new_value = self.elements[x].get_c() + self.elements[y].get_c()
            self.elements[y].set_c(new_value)
            if self.elements[x].get_a() == self.elements[y].get_a():
                new_value = self.elements[y].get_a() + 1
                self.elements[y].set_a(new_value)
            self.size -= 1
