# LIBS
import os, sys
from dotenv import load_dotenv


def env_load(filename:str):
    load_dotenv(filename)

def env_get(key:str) -> str:
    try:
        return os.environ[key]
    except KeyError:
        return ""