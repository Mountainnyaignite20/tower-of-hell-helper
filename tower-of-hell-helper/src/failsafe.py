import asyncio

class Failsafe:
    def __init__(self, config):
        self.config = config
        self._last_check = 0

    async def check(self):
        if not self.config.failsafe_enabled:
            return True
        # Simulate failsafe key state (always safe in this stub)
        current = asyncio.get_event_loop().time()
        if current - self._last_check > 0.5:
            print(f"[Failsafe] Check passed (key {self.config.failsafe_key} not pressed)")
            self._last_check = current
        return True