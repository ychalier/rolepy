import logging


class TaskManager:

    def __init__(self):
        self.tasks = dict()
        self.log = dict()

    def remove_dead_threads(self, cls):
        indices = list()
        for i in range(len(self.tasks[cls])):
            if not self.tasks[cls][i].is_alive():
                if self.log[cls]:
                    logging.debug("Thread {} has died".format(self.tasks[cls][i]))
                indices.append(i)
        indices.sort()
        indices.reverse()
        for i in indices:
            self.tasks[cls].pop(i)

    def _start(self, task, max_concurrent=1, log=True):
        cls = task.__class__
        self.tasks.setdefault(cls, list())
        self.log[cls] = log
        self.remove_dead_threads(cls)
        if len(self.tasks[cls]) < max_concurrent:
            if log:
                logging.debug("Spawning thread {}".format(task))
            self.tasks[cls].append(task)
            task.start()
            return task
        else:
            return None

    def start(self, *tasks, max_concurrent=1, log=True):
        for task in tasks:
            self._start(task, max_concurrent, log)

    def terminate_all(self, cls):
        for thread in self.tasks.get(cls, list()):
            thread.terminate()
