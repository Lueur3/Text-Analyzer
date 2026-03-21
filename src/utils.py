import os
import string
import json
from collections.abc import Iterable

SUPPORTED_EXTENSIONS = (".txt",)
PUNCTUATION_MAP = str.maketrans("", "", string.punctuation)


def validate_file_path(filename: str) -> str:
    if filename:
        file_path = os.path.abspath(filename.rstrip())
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            raise FileNotFoundError(
                f"The file at {file_path} was not found or file is empty."
            )
        elif not os.path.splitext(file_path)[1] in SUPPORTED_EXTENSIONS:
            raise ValueError("The file contains an incorrect extension type.")
        elif not os.access(file_path, os.R_OK):
            raise PermissionError(f"The file does not have access rights.")

        return file_path
    else:
        raise ValueError("The file path is not specified.")


def raw_text(text: str):
    if not (text and text.strip()):
        raise ValueError("The entered text is empty or contains only spaces.")


def get_file_lines(file_path: str) -> Iterable[str]:
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            yield line


def get_text_lines(text: str) -> Iterable[str]:
    for line in text.splitlines():
        yield line


def preprocess_line(line: str) -> str:
    return line.lower().strip().translate(PUNCTUATION_MAP)


def save_stats(stats: dict):
    file_path = "../data/output.json"
    folder_path = "../data"
    os.makedirs(folder_path, exist_ok=True)
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    data.append(stats)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
