class Fifo:
    """FIFO data structure with streamed average."""

    def __init__(self, window):
        self.window = window
        self.data = list()
        self.mean = 0
        self.size = 0

    def add(self, element):
        """Append a new element to the file."""
        if self.size == self.window:
            self.data.append(element)
            old = self.data.pop(0)
            self.mean += (element - old) / self.size
        else:
            self.size += 1
            self.data.append(element)
            self.mean = sum(self.data) / self.size
