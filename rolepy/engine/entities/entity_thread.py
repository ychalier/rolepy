from rolepy.engine.core.tasks import AsyncTask
from rolepy.engine.entities.enums import EntityState


class EntityThread(AsyncTask):
    """Thread dedicated for entity AI."""

    def __init__(self, entity_manager):
        def function():
            for entity in entity_manager.registry.copy():
                if entity.attributes.state == EntityState.IDLE:
                    entity.take_action()
        AsyncTask.__init__(self, function)
