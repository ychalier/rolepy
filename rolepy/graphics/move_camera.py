import time
from rolepy.misc import AsyncTask
from rolepy.misc import Position
from rolepy.globals import WalkAnimation


def cycle():
    while True:
        yield WalkAnimation.LEFT
        yield WalkAnimation.REST
        yield WalkAnimation.RIGHT
        yield WalkAnimation.REST


class MoveCamera(AsyncTask):

    def __init__(self, game, dest, steps, duration, anim_step=10):
        def function():
            game.camera_is_moving = True
            player_tile = game.tile_manager.entities[game.world.player]
            source = Position(*game.camera.pair())
            delay = float(duration) / float(steps + 1)
            iterator = cycle()
            for step in range(steps + 1):
                if step % anim_step == 0:
                    player_tile.walk_animation = next(iterator)
                progress = float(step) / float(steps)
                game.camera.x = source.x * (1 - progress) + dest.x * progress
                game.camera.y = source.y * (1 - progress) + dest.y * progress
                time.sleep(delay)
            game.camera_is_moving = False
            player_tile.walk_animation = WalkAnimation.REST
        AsyncTask.__init__(self, function)
