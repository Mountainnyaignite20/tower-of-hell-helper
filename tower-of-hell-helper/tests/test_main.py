import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import asyncio
from src.auto_jump import AutoJump
from src.failsafe import Failsafe
from src.config import Config

def test_config_defaults():
    cfg = Config()
    assert cfg.jump_key == "space"
    assert cfg.jump_interval == 0.15

def test_auto_jump():
    cfg = Config()
    aj = AutoJump(cfg)
    assert aj._running == False
    asyncio.run(aj.perform_jump())
    assert aj._running == False

def test_failsafe():
    cfg = Config()
    fs = Failsafe(cfg)
    result = asyncio.run(fs.check())
    assert result == True

if __name__ == "__main__":
    test_config_defaults()
    test_auto_jump()
    test_failsafe()
    print("All tests passed.")