# Text Analyzer

A program for performing statistical analysis of text data from files or console input.

## Features

- Total word count.
- Search for the longest word.
- Word frequency analysis.
- Output of top-N most frequent words (default is 3).
- Saving analysis results (metadata and statistics) to a JSON file.
- Handling input errors and missing files.

## Project Structure

- `main.py`: Entry point and module coordination.
- `utils.py`: Module for file system operations, validation, and text preprocessing.
- `processor.py`: Module for statistics calculation and data analysis.
- `tests/`: Unit tests based on pytest.
- `data/`: Directory for input texts and output reports.

## Installation and Execution

1. Install dependencies: `pip install pytest`.
2. Run the program: `python src/main.py`.

## Testing

To run the tests, use the following command:
`pytest tests/test_processor.py`

---

# Анализатор текста

Программа для проведения статистического анализа текстовых данных из файлов или консольного ввода.

## Функционал

- Подсчет общего количества слов.
- Поиск самого длинного слова.
- Анализ частоты встречаемости слов.
- Вывод топ-N самых частых слов (по умолчанию 3).
- Сохранение результатов анализа (метаданные и статистика) в JSON-файл.
- Обработка ошибок ввода и отсутствия файлов.

## Структура проекта

- `main.py`: Точка входа и координация модулей.
- `utils.py`: Модуль для работы с файловой системой, валидации и предобработки текста.
- `processor.py`: Модуль для вычисления статистики и анализа данных.
- `tests/`: Модульные тесты на базе pytest.
- `data/`: Директория для входных текстов и выходных отчетов.

## Установка и запуск

1. Установите зависимости: `pip install pytest`.
2. Запустите программу: `python src/main.py`.

## Тестирование

Для запуска тестов используйте команду:
`pytest tests/test_processor.py`
