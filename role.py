import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import logging
import pygame
import sys
from rolepy import Settings
from rolepy import Game

if __name__ == "__main__":
    log_format = "%(asctime)s\t%(levelname)s\t%(message)s"
    logging.basicConfig(format=log_format, level=logging.DEBUG)
    logging.info("Starting the program.")
    logging.debug("Initalizing PyGame")
    pygame.init()
    logging.debug("Done initializing PyGame")
    settings = Settings()
    settings.load("settings.txt")
    game = Game(settings)
    game.load()
    game.start()
