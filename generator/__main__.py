from config import Config
from core import Generator


config = Config()
generator = Generator(config)
generator.generate()