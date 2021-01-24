from typing import List
from pathlib import Path
import shutil


class Parser():

    extensions: List[str] = []

    def valid_extension(self, extension: str) -> bool:
        return extension in self.extensions

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError("Not Implemented")

    def read(self, path: Path) -> str:
        with path.open() as file:
            return file.read()

    def write(self, path: Path, dest: Path, content: str, ext: str = ".html"):
        full_path = dest / path.with_suffix(ext).name
        with full_path.open() as file:
            file.write(content)

    def copy(self, path: Path, source: Path, dest: Path):
        shutil.copy2(path, dest / path.relative_to(source))


class ResourceParser(Parser):
    extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path: Path, source: Path, dest: Path):
        self.copy(path, source, dest)
