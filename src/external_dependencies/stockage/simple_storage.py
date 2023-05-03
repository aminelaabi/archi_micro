import random
import string
import time
import os

from anonfile import AnonFile
from .simple_storage_abc import SimpleStorageABC
from loguru import logger


class SimpleStorage(SimpleStorageABC):



    def __init__(self):
        self.anon = AnonFile()

    def _generate_random_string(self, length: int = 10) -> str:
        random_string = ''.join(random.choices(string.ascii_lowercase, k=6))
        timestamp = int(time.time())
        filename = f"{timestamp}_{random_string}.jpg"
        return filename
    
    def _correct_file_extension(self, file_name: str) -> str:
        splitted_filename = file_name.split("_")
        return "_".join(splitted_filename[:-1]) + "." + splitted_filename[-1]


    def upload(self, file_content: bytes) -> str:
        img_name = self._generate_random_string()
        with open(img_name, "wb") as f:
            f.write(file_content)
        file = self.anon.upload(img_name)
        os.remove(img_name)
        return file.url.geturl()

    def download(self, url: str, path: str = "./") -> bytes:
        logger.debug(f"Downloading {url} to {path}")
        
        
        file = self.anon.download(url, path)
        file_content = None
        file_name = self._correct_file_extension(file.name.stem)
        logger.debug(f"Downloaded {url} to {path}, {file.name}")
        with open(file_name, "rb") as f:
            file_content = f.read()
        os.remove(file_name)
        return file_content