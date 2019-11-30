import logging
import os


class Settings:
    """Stores and manages user settings."""

    def __init__(self):
        self._file = None
        self.resolution = 32 * 29, 32 * 17
        self.max_fps = 62
        self.key_repeat_delay = 10  # ms
        self.save_file = "save.json"

    def load(self, input_file):
        """Read the configuration file and update settings values."""
        logging.info("Reading configuration from %s", os.path.join(os.getcwd(), input_file))
        self._file = input_file
        for line in open(input_file).readlines():
            try:
                if "=" not in line:
                    continue
                keyword, value = line.strip().split("=")
                if keyword.lower() == "resolution":
                    self.resolution = list(map(int, value.split("*")))
                elif keyword.lower() == "max_fps":
                    if len(value) > 0:
                        self.max_fps = int(value)
                    else:
                        self.max_fps = None
                elif keyword.lower() == "key_repeat_delay":
                    self.key_repeat_delay = int(value)
                elif keyword.lower() == "save_file":
                    self.save_file = value
            except ValueError:
                logging.warning("Incorrect configuration line\n'%s'", line)

    def save(self):
        """Write the current configuration to a file"""
        logging.info("Saving configuration to %s", os.path.join(os.getcwd(), self._file))
        placeholder = """
# Window size in pixels
# resolution=928*544
resolution={resolution}

# FPS cap (leave empty for unlimited)
# max_fps=144
max_fps={max_fps}

# Time between two touchdown events
# key_repeat_delay=10
key_repeat_delay={key_repeat_delay}

# Save file
# save_file=save.json
save_file={save_file}
        """
        if self.max_fps is None:
            max_fps = ""
        else:
            max_fps = "%d" % self.max_fps
        text = placeholder.format(
            resolution="%d*%d" % (self.resolution[0], self.resolution[1]),
            max_fps=max_fps,
            key_repeat_delay="%d" % self.key_repeat_delay,
            save_file="%s" % self.save_file
        )
        with open(self._file, "w") as file:
            file.write(text)
