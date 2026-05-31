class Config:
    def __init__(self):
        self.jump_key = "space"
        self.jump_interval = 0.15
        self.failsafe_key = "q"
        self.failsafe_enabled = True

    def __repr__(self):
        return f"Config(jump_key={self.jump_key}, interval={self.jump_interval})"