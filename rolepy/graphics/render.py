import pygame
from rolepy.misc import AsyncTask
from rolepy.misc import Position
from rolepy.globals import SPRITE_SIZE


class Render(AsyncTask):

    def __init__(self, game):
        def function():
            game.screen.fill((0, 0, 0))
            width, height = game.settings.resolution
            world_surface_position = Position(width // 2, height // 2) \
                + SPRITE_SIZE * (.5 * Position(-1, 1)\
                    - Position(1, -1) * game.camera\
                    - Position(
                        game.world_surface.offset_x,
                        game.world_surface.offset_y
                        )
                    )
            game.screen.blit(
                game.world_surface.surface,
                world_surface_position.pair()
            )
            game.screen.blit(
                game.tile_manager.entities[game.world.player].sprite(),
                (width / 2 - SPRITE_SIZE / 2, height / 2 - SPRITE_SIZE / 2)
            )
            pygame.display.flip()
        AsyncTask.__init__(self, function)
