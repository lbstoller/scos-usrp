import sys
from os import path

from django.conf import settings
from environs import Env

env = Env()

CONFIG_DIR = path.join(path.dirname(path.abspath(__file__)), "configs")
ACTION_DEFINITIONS_DIR = path.join(CONFIG_DIR, "actions")
TEST_ACTION_DEFINITIONS_DIR = path.join(CONFIG_DIR, "test_actions")

__cmd = path.split(sys.argv[0])[-1]
RUNNING_TESTS = "test" in __cmd

if not settings.configured or not hasattr(settings, "MOCK_SIGAN"):
    MOCK_SIGAN = env.bool("MOCK_SIGAN", default=False) or RUNNING_TESTS
else:
    MOCK_SIGAN = settings.MOCK_SIGAN
if not settings.configured or not hasattr(settings, "MOCK_SIGAN_RANDOM"):
    MOCK_SIGAN_RANDOM = env.bool("MOCK_SIGAN_RANDOM", default=False)
else:
    MOCK_SIGAN_RANDOM = settings.MOCK_SIGAN_RANDOM

USRP_CONNECTION_ARGS = env("USRP_CONNECTION_ARGS", default="num_recv_frames=650")
