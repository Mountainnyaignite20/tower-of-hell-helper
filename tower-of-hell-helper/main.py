import sys
import asyncio
from src.auto_jump import AutoJump
from src.failsafe import Failsafe
from src.config import Config

async def main():
    config = Config()
    auto_jump = AutoJump(config)
    failsafe = Failsafe(config)

    print("Tower of Hell Helper started. Press Ctrl+C to stop.")
    try:
        while True:
            if failsafe.check():
                await auto_jump.perform_jump()
            await asyncio.sleep(0.01)
    except KeyboardInterrupt:
        print("\nShutting down.")
        sys.exit(0)

if __name__ == "__main__":
    asyncio.run(main())