import asyncio
import random

class AutoJump:
    def __init__(self, config):
        self.config = config
        self._running = False

    async def perform_jump(self):
        if self._running:
            return
        self._running = True
        # Simulate keypress delay
        await asyncio.sleep(self.config.jump_interval * random.uniform(0.8, 1.2))
        print(f"[AutoJump] Pressed {self.config.jump_key}")
        self._running = False