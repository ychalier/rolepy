# RolePy

RolePy is a role play game (RPG) based on the procedural generation of the
logical and physical world, which the player may interract with to achieve
personal goals or life principals.

[Documentation](https://rolepy.readthedocs.io/en/latest/) - [Wiki](https://github.com/ychalier/rolepy/wiki) - [YouTube](//www.youtube.com/channel/UCiNHU2xHojEsiInOtNtYrkg)

## Getting Started

Checkout [documentation](https://rolepy.readthedocs.io/en/latest/usage/index.html) for more details.

### Prerequisites

The game is implemented using Python 3 (v3.5.2. to be precise). Current
implementation uses the [pygame](https://www.pygame.org/news) module
for Python (find here the [documentation](https://www.pygame.org/docs)).
Version is reported in `requirements.txt`.

### Installing

Create a configuration file, `settings.txt`, with the following format:

```
# Window size in pixels
# resolution=928*544
resolution=928*544

# FPS cap (leave empty for unlimited)
# max_fps=144
max_fps=

# Time between two touchdown events
# key_repeat_delay=10
key_repeat_delay=10
```

Then start the main script with:

```bash
python role.py
```

## Built With

 - [PyGame](https://www.pygame.org/news) - Python graphic module
 - [Aseprite](//www.aseprite.com) - Pixel art and sprites creation software

## Contributing

Contributions are welcomed. You might want to check the [roadmap](https://github.com/ychalier/rolepy/wiki/Roadmap) to have an idea of what to do, and the [documentation](https://rolepy.readthedocs.io/en/latest/) to have and idea of how to do it. Push your branch and create a pull request detailling your changes. Please make sure to maintain documentation up to date.

## Authors

Project is maintained by [Yohan Chalier](https://github.com/ychalier/). See the list of [contributors](https://github.com/ychalier/rolepy/graphs/contributors) who participated.

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE.txt](LICENSE.txt) file for details.

## Acknowledgments

The gamme core mechanics are inspired by the [RPG Maker](https://www.rpgmakerweb.com/) series. Current sprites come from [Sharm's Tiny 16](https://opengameart.org/content/tiny-16-basic), but are only used for development purposes.
