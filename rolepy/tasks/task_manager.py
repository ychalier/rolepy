import logging


class TaskManager:

    def __init__(self):
        self.tasks = dict()

    def remove_dead_threads(self, cls):
        indices = list()
        for i in range(len(self.tasks[cls])):
            if not self.tasks[cls][i].is_alive():
                logging.debug("Thread {} has died".format(self.tasks[cls][i]))
                indices.append(i)
        indices.sort()
        indices.reverse()
        for i in indices:
            self.tasks[cls].pop(i)

    def start(self, task, max_concurrent=1):
        cls = task.__class__
        self.tasks.setdefault(cls, list())
        self.remove_dead_threads(cls)
        if len(self.tasks[cls]) < max_concurrent:
            logging.debug("Spawning thread {}".format(task))
            self.tasks[cls].append(task)
            task.start()
            return task
        else:
            return None

    def terminate_all(self, cls):
        for thread in self.tasks.get(cls, list()):
            thread.terminate()
