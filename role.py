import logging
import pygame
import sys
from rolepy import Settings
from rolepy import Game

if __name__ == "__main__":
    # logging.basicConfig(
    #     format="%(asctime)s\t%(levelname)s\t%(message)s", level=logging.DEBUG)
    # logging.info("Starting the program.")
    # logging.debug("Initalizing PyGame")
    # pygame.init()
    # logging.debug("Done initializing PyGame")
    # settings = Settings()
    # game = Game(settings)
    # game.load()
    # game.start()
    from rolepy.generate.biomes import BiomeMap
    BiomeMap.demo()
