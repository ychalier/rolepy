from rolepy.tasks import AsyncTask


class EntityAiThread(AsyncTask):

    def __init__(self, entity_manager):
        def function():
            entity_manager.ai_step()
        AsyncTask.__init__(self, function)
