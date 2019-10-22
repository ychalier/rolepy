from rolepy.tasks import AsyncTask


class EntityAiThread(AsyncTask):
    """Thread dedicated for entity AI."""

    def __init__(self, entity_manager):
        def function():
            entity_manager.ai_iterate()
        AsyncTask.__init__(self, function)
