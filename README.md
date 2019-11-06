# RolePy

A 2D scrolling RPG game, with procedural universe including lore and terrain.

## 1. Setup

### 1.1. Dependencies

The game is implemented using Python 3 (v3.5.2. to be precise).

Current implementation uses the [pygame](https://www.pygame.org/news) module
for Python (find here the [documentation](https://www.pygame.org/docs)). Version is reported in `requirements.txt`.

### 1.2. Quick start

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

## 2. Links

 - [Roadmap](//yohan.chalier.fr/notes/public/rolepy)
 - [Documentation on the game engine](//yohan.chalier.fr/notes/public/rolepy-game-engine)
 - [YouTube](//www.youtube.com/channel/UCiNHU2xHojEsiInOtNtYrkg)
