class Fifo:

    def __init__(self, window):
        self.window = window
        self.data = list()
        self.mean = 0
        self.n = 0

    def add(self, element):
        if self.n == self.window:
            self.data.append(element)
            old = self.data.pop(0)
            self.mean += (element - old) / self.n
        else:
            self.n += 1
            self.data.append(element)
            self.mean = sum(self.data) / self.n
