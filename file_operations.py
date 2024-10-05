import os
from abc import ABC, abstractmethod

class AbstractFile(ABC):
    def __init__(self, file_name: str):
        self._file_name = file_name

    @abstractmethod
    def read_lines(self, num_lines: int = 1) -> list:
        pass

    @abstractmethod
    def write_lines(self, lines) -> None:
        pass

    @abstractmethod
    def read(self, num_bytes: int = None) -> str:
        pass

    @abstractmethod
    def write(self, content: str) -> None:
        pass

    @abstractmethod
    def delete(self) -> None:
        pass

    @abstractmethod
    def copy(self, new_file_name: str) -> None:
        pass

    @abstractmethod
    def rename(self, new_file_name: str) -> None:
        pass


class File(AbstractFile):
    def read_lines(self, num_lines: int = 1) -> list:
        lines = []
        try:
            with open(self._file_name, 'r') as file:
                for _ in range(num_lines):
                    lines.append(next(file))
            return lines
        except StopIteration:
            return []
        except OSError:
            print(f"File not found or error reading: {self._file_name}")
            return []

    def write_lines(self, lines) -> None:
        try:
            with open(self._file_name, 'a') as file:
                if isinstance(lines, (list, tuple)):
                    for line in lines:
                        file.write(str(line) + '\n')
                else:
                    file.write(str(lines) + '\n')
        except OSError:
            print(f"Error writing to file: {self._file_name}")

    def read(self, num_bytes: int = None) -> str:
        try:
            with open(self._file_name, 'r') as file:
                return file.read() if num_bytes is None else file.read(num_bytes)
        except OSError:
            print(f"File not found or error reading: {self._file_name}")
            return ""

    def write(self, content: str) -> None:
        try:
            with open(self._file_name, 'a') as file:
                file.write(content)
        except OSError:
            print(f"Error writing to file: {self._file_name}")

    def delete(self) -> None:
        try:
            os.remove(self._file_name)
        except OSError:
            print(f"File not found or error deleting: {self._file_name}")

    def copy(self, new_file_name: str) -> None:
        try:
            with open(self._file_name, 'r') as original:
                with open(new_file_name, 'w') as new_file:
                    new_file.write(original.read())
        except OSError:
            print(f"Error copying file: {self._file_name}")

    def rename(self, new_file_name: str) -> None:
        try:
            os.rename(self._file_name, new_file_name)
            self._file_name = new_file_name
        except OSError:
            print(f"Error renaming file: {self._file_name}")


