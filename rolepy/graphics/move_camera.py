import time
from rolepy.misc import AsyncTask
from rolepy.misc import Position
from rolepy.globals import Ordinal
from rolepy.globals import WalkAnimation
from rolepy.globals import SPRITE_SIZE
from rolepy.graphics import LoadWorld

class MoveCamera(AsyncTask):

    def __init__(self, game, direction):
        iterator = WalkAnimation.cycle()
        player = game.tile_manager.entities[game.world.player.texture]
        def function():
            if game.is_moving:
                return
            game.is_moving = True
            game.movements[direction] = True
            player.direction = direction
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
                last = start
                progress = 0
                LoadWorld(game, destination).start()
                while progress < 1:
                    current = time.time()
                    progress = min(1, (current - start) / duration)
                    game.camera = (1 - progress) * source + progress * destination
                    if current - last > duration / 4:
                        player.walk_animation = next(iterator)
                        last = current
                    time.sleep(duration / 25)
            game.camera.round()
            player.walk_animation = WalkAnimation.REST
            game.is_moving = False
        AsyncTask.__init__(self, function)
