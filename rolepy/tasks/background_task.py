import multiprocessing as mp


class BackgroundTask(mp.Process):

    def __init__(self):
        mp.Process.__init__(self)
        self.input = mp.JoinableQueue()
        self.output = mp.Queue()
