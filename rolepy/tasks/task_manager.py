import logging


class TaskManager:
    """Handle current tasks and avoid having many concurrent threads."""

    def __init__(self):
        self.tasks = dict()
        self.log = dict()

    def remove_dead_threads(self, cls):
        """Check for terminated threads and forget them."""
        indices = list()
        for i in range(len(self.tasks[cls])):
            if not self.tasks[cls][i].is_alive():
                if self.log[cls]:
                    logging.debug("Thread %s has died", self.tasks[cls][i])
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
                logging.debug("Spawning thread %s", task)
            self.tasks[cls].append(task)
            task.start()
            return task
        return None

    def start(self, *tasks, max_concurrent=1, log=True):
        """Spawn a set of task threads."""
        for task in tasks:
            self._start(task, max_concurrent, log)

    def terminate_all(self, cls):
        """Kill all threads of a given class."""
        for thread in self.tasks.get(cls, list()):
            thread.terminate()
