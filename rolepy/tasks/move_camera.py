import time
from rolepy.tasks import AsyncTask
from rolepy.misc import Position
from rolepy.globals import Ordinal


class MoveCamera(AsyncTask):

    def __init__(self, game, direction):
        def function():
            game.movements[direction] = True
            while game.movements[direction]:
                duration = 1 / game.speed
                source = Position(*game.camera.pair())
                if direction == Ordinal.NORTH:
                    destination = source + Position(0, -1)
                elif direction == Ordinal.SOUTH:
                    destination = source + Position(0, 1)
                elif direction == Ordinal.WEST:
                    destination = source + Position(-1, 0)
                elif direction == Ordinal.EAST:
                    destination = source + Position(1, 0)
                start = time.time()
                progress = 0
                while progress < 1:
                    current = time.time()
                    progress = min(1, (current - start) / duration)
                    game.camera = (1 - progress) * source + progress * destination
                    time.sleep(duration / 25)
                game.entity_manager.update_registry(game.camera.target())
            game.camera.round()
        AsyncTask.__init__(self, function)
