from rolepy.tasks import AsyncTask


class SwitchWorldSurface(AsyncTask):
    """Thread dedicated to world surface switch."""

    def __init__(self, world_surface_manager, direction):
        def function():
            world_surface_manager.switch(direction)
        AsyncTask.__init__(self, function)
