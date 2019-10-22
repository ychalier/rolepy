import multiprocessing as mp


class BackgroundTask(mp.Process):
    """Separated process dedicated to a given task."""

    def __init__(self):
        mp.Process.__init__(self)
        self.input = mp.JoinableQueue()
        self.output = mp.Queue()
