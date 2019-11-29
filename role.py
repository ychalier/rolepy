import logging
import os
import rolepy
from rolepy import Settings
from rolepy import Game
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"


if __name__ == "__main__":
    import pygame
    log_format = "%(asctime)s\t%(levelname)s\t%(message)s"
    logging.basicConfig(format=log_format, level=logging.DEBUG)
    logging.info("Starting RolePy version %s", rolepy.__version__)
    logging.debug("Initalizing PyGame")
    pygame.init()
    logging.debug("Done initializing PyGame")
    settings = Settings()
    settings.load("settings.txt")
    game = Game(settings)
    game.start()
    game.load()
    game.main()
