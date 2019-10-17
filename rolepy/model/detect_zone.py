import logging
from rolepy.misc import AsyncTask
from rolepy.misc import BackgroundTask
from rolepy.misc import Position
from rolepy.generate import WorldGenerator
from rolepy.generate.biomes import Biome
from rolepy.generate.biomes import Zone


class DetectZoneBackground(BackgroundTask):

    def run(self):
        seed, x, y = self.input.get()
        generator = WorldGenerator(seed)
        generator.biome_map.build([(y, x)])
        zone = Zone(generator.biome_map[y, x])
        buffer, seen = set(), set()
        buffer.add((y, x))
        seen.add((y, x))
        while len(buffer) > 0:
            p = buffer.pop()
            zone.add(p)
            for neighbor in generator.biome_map.get_neighbors(p).difference(seen):
                seen.add(neighbor)
                generator.biome_map.build([neighbor])
                if generator.biome_map[neighbor] == zone.biome:
                    buffer.add(neighbor)
                else:
                    zone.frontier.append(neighbor)
        zone.find_name()
        self.output.put(zone)


class DetectZone(AsyncTask):

    def __init__(self, game, x_float, y_float):

        def function():
            x = round(x_float)
            y = round(y_float)
            logging.debug("Detecting zone at ({}, {})".format(x, y))
            bg_task = DetectZoneBackground()
            bg_task.input.put((game.world.generator.seed, x, y))
            bg_task.start()
            zone = bg_task.output.get()
            bg_task.join()
            bg_task.terminate()
            logging.debug("Detected zone: {}".format(zone))
            game.world.zones.append(zone)
            for i, j in zone.inside:
                game.world.zones_map[Position(j, i)] = zone
            game.zone_interface_box.update(zone.name)
        AsyncTask.__init__(self, function)
