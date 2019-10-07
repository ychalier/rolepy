import pygame
from rolepy.misc import AsyncTask
from rolepy.misc import Position
from rolepy.globals import SPRITE_SIZE


class Render(AsyncTask):

    def __init__(self, game):
        def function():
            game.screen.fill((0, 0, 0))
            width, height = game.settings.resolution
            n_cols = width // SPRITE_SIZE
            n_rows = height // SPRITE_SIZE
            margin = 1
            for x in range(-margin - n_cols // 2, n_cols + margin - n_cols // 2):
                for y in range(-margin - n_rows // 2, n_rows + margin - n_rows // 2):
                    position = Position(x, y) + game.camera.target()
                    tile = game.world.terrain.get(position, None)
                    if tile is not None:
                        dest_centered = SPRITE_SIZE * \
                            (position - game.camera + .5 * Position(-1, 1))
                        dest_upper_left = (
                            int(width / 2 + dest_centered.x),
                            int(height / 2 - dest_centered.y)
                        )
                        game.screen.blit(
                            game.tile_manager.terrain[tile].sprite(),
                            dest_upper_left
                        )
            game.screen.blit(
                game.tile_manager.entities[game.world.player].sprite(),
                (width / 2 - SPRITE_SIZE / 2, height / 2 - SPRITE_SIZE / 2)
            )
            pygame.display.flip()
        AsyncTask.__init__(self, function)
