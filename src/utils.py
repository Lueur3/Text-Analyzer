import os
import string
from collections.abc import Iterable

SUPPORTED_EXTENSIONS = (".txt",)
PUNCTUATION_MAP = str.maketrans("", "", string.punctuation)


def validate_file_path(filename: str) -> str:
    if filename:
        file_path = os.path.abspath(filename.rstrip())
        if not (os.path.exists(file_path)):
            raise FileNotFoundError(f"Файл по адресу {file_path} не найден.")
        elif not (os.path.splitext(file_path)[1] in SUPPORTED_EXTENSIONS):
            raise ValueError("Файл содержит неверный тип расширения.")
        elif not (os.access(file_path, os.R_OK)):
            raise PermissionError(f"У файла нет прав доступа.")

        return file_path
    else:
        raise ValueError("Путь к файлу не указан.")


def raw_text(text: str):
    if not (text and text.strip()):
        raise ValueError("Введенный текст пуст или содержит только пробелы.")


def get_file_lines(file_path: str) -> Iterable[str]:
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            yield line


def get_text_lines(text: str) -> Iterable[str]:
    for line in text.splitlines():
        yield line


def preprocess_line(line: str) -> str:
    return line.lower().strip().translate(PUNCTUATION_MAP)
