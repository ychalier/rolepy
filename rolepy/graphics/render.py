import pygame
from rolepy.tasks import AsyncTask
from rolepy.misc import Position
from rolepy.globals import SPRITE_SIZE


class Render(AsyncTask):

    def __init__(self, game):
        def function():
            width, height = game.settings.resolution
            game.screen.fill((0, 0, 0))
            world_surface = game.world_surface_manager.surface()
            position = SPRITE_SIZE * (
                    -   game.camera
                    - .5 * Position(1, 1)
                    - world_surface.offset
                ) + Position(width // 2, height // 2)
            game.screen.blit(world_surface, position.pair())
            game.screen.blit(
                game.tile_manager.entities[game.world.player.texture].sprite(),
                (width / 2 - SPRITE_SIZE / 2, height / 2 - SPRITE_SIZE / 2)
            )
            game.interface.blit(game.screen)
            pygame.display.flip()
        AsyncTask.__init__(self, function)
