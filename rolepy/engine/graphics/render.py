import pygame
from rolepy.engine.core.tasks import AsyncTask
from rolepy.engine.core.structs import Position
from rolepy.engine.core.globals import SPRITE_SIZE


class Render(AsyncTask):
    """Thread dedicated to frame rendering."""

    def __init__(self, game):
        def function():
            width, height = game.settings.resolution

            def transformer(position):
                return SPRITE_SIZE * (
                    position - game.camera - .5 * Position(1, 1)
                ) + Position(width // 2, height // 2)
            world_surface = game.world_surface_manager.surface()
            game.screen.fill((0, 0, 0))
            game.screen.blit(
                world_surface, transformer(-world_surface.offset).pair())
            game.entity_manager.blit(
                game.tile_manager, game.screen, transformer)
            game.interface_manager.blit(game.screen, transformer)
            pygame.display.flip()
        AsyncTask.__init__(self, function)
