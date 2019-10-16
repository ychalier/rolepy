import pygame
from rolepy.misc import AsyncTask
from rolepy.misc import Position
from rolepy.globals import SPRITE_SIZE


class Render(AsyncTask):

    def __init__(self, game):
        def function():
            game.screen.fill((0, 0, 0))
            width, height = game.settings.resolution
            position = SPRITE_SIZE * (
                    game.camera
                    + .5 * Position(1, 1)
                    + Position(game.world_surface.offset_x, game.world_surface.offset_y)
                ) - Position(width // 2, height // 2)
            game.screen.blit(
                game.world_surface.surface,
                (0, 0),
                area=(*position.pair(), width, height)
            )
            game.screen.blit(
                game.tile_manager.entities[game.world.player.texture].sprite(),
                (width / 2 - SPRITE_SIZE / 2, height / 2 - SPRITE_SIZE / 2)
            )
            game.interface.blit(game.screen)
            pygame.display.flip()
        AsyncTask.__init__(self, function)
