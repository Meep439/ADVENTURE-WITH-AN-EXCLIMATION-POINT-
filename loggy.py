muted = False

def mute():
    muted = not muted

def log(text, level="INFO"):
    if not muted:
        print(f"{level}: {text}")

class Logger:
    def __init__(self, name="Unnamed Logger", muted=False):
        self.n = name
        self.m = muted

    def mute(self):
        self.m = not self.m

    def log(self, text, level="INFO"):
        print(f"{self.n}: ", end="")
        log(text, level)
