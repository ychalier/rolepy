import logging
import time
from rolepy.tasks import AsyncTask
from rolepy.tasks import BackgroundTask
from rolepy.misc import Position
from rolepy.generate import WorldGenerator
from rolepy.generate.biomes import Zone
from rolepy.graphics.interface import InterfaceManager


def get_neighbors(position):
    """Return the cross neighbors of a position."""
    i, j = position
    return set([(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)])


class DetectZoneBackground(BackgroundTask):
    """Background process for zone detection, which may require
        heavy computation.
    """

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
            for neighbor in get_neighbors(p).difference(seen):
                seen.add(neighbor)
                generator.biome_map.build([neighbor])
                if generator.biome_map[neighbor] == zone.biome:
                    buffer.add(neighbor)
                else:
                    zone.frontier.append(neighbor)
        zone.find_name()
        self.output.put(zone)


class DetectZone(AsyncTask):
    """Thread to wait for zone detection process to terminate."""

    def __init__(self, game, x_float, y_float):

        def function():
            x = round(x_float)
            y = round(y_float)
            logging.debug("Detecting zone at (%d, %d)", x, y)
            bg_task = DetectZoneBackground()
            bg_task.input.put((game.world.generator.seed, x, y))
            bg_task.start()
            zone = bg_task.output.get()
            bg_task.join()
            logging.debug("Detected zone: %s", zone)
            game.interface_manager[InterfaceManager.DEBUG_INTERFACE].zone.update(
                zone.name)
            game.world.zones.append(zone)
            count = 0
            for i, j in zone.inside:
                game.world.zones_map[Position(j, i)] = zone
                count += 1
                if count % 500 == 0:
                    time.sleep(.001)
            bg_task.terminate()
            logging.debug("Finished loading new zone")
        AsyncTask.__init__(self, function)
