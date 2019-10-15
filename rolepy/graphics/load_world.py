from rolepy.misc import AsyncTask

class LoadWorld(AsyncTask):

    def __init__(self, game, camera):
        def function():
            game.world_surface.check(camera)
        AsyncTask.__init__(self, function)
