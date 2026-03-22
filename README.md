# Text Analyzer

A tool for statistical analysis of text data from files or manual console input.

## Features

- Total word count.
- Search for the longest word.
- Word frequency analysis.
- Output of top-N most frequent words.
- Saving results to a JSON file.
- Input validation and exception handling.

## Installation and Execution (Local)

1.  **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the application**:

    ```bash
    python src/main.py
    ```

3.  **Run tests**:
    ```bash
    pytest tests/test_processor.py
    ```

## Running with Docker

1.  **Build the image**:

    ```bash
    docker build -t text-analyzer .
    ```

2.  **Run the container**:
    ```bash
    docker run -it -v "$(pwd)/data:/app/data" text-analyzer:latest
    ```
    _Note: the `-v` flag is required to persist `output.json` on your local machine._

---

# Анализатор текста

Программа для статистического анализа текстовых данных из файлов или консольного ввода.

## Функционал

- Подсчет общего количества слов.
- Поиск самого длинного слова.
- Анализ частоты встречаемости слов.
- Вывод топ-N самых частотных слов.
- Сохранение результатов в JSON-файл.
- Валидация входных данных и обработка исключений.

## Установка и запуск (Локально)

1.  **Установка зависимостей**:

    ```bash
    pip install -r requirements.txt
    ```

2.  **Запуск программы**:

    ```bash
    python src/main.py
    ```

3.  **Запуск тестов**:
    ```bash
    pytest tests/test_processor.py
    ```

## Запуск через Docker

1.  **Сборка образа**:

    ```bash
    docker build -t text-analyzer .
    ```

2.  **Запуск контейнера**:
    ```bash
    docker run -it -v "$(pwd)/data:/app/data" text-analyzer:latest
    ```
    _Примечание: флаг `-v` необходим для сохранения `output.json` на локальном диске._
