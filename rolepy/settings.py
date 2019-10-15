import logging


class Settings:

    def __init__(self):
        self.resolution = 32 * 29, 32 * 17
        self.max_fps = None
        self.key_repeat_delay = 10  # ms

    def load(self, input_file):
        logging.info("Reading configuration from " + input_file)
        for line in open(input_file).readlines():
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

    def save(self, output_file):
        pass
