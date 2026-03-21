import pytest
from src.processor import init_stats, update_stats, get_top_words

"""
@pytest.mark.parametrize(
    "type, filename, expected_dict",
    [
        (
            1,
            "../data/example_text.txt",
            {
                "statistic_type": "File - Text-Analyzer/data/example_text.txt",
                "total_count": 0,
                "word_frequencies": {},
                "longest_word": "",
            },
        ),
        (
            2,
            "User text",
            {
                "statistic_type": "User text",
                "total_count": 0,
                "word_frequencies": {},
                "longest_word": "",
            },
        ),
    ],
)
def test_init_stats(type, filename, expected_dict):
    assert init_stats(type, filename) == expected_dict
"""


@pytest.mark.parametrize(
    "text_type, filename, expected_dict_type",
    [(2, "User text", dict)],
)
def test_type_dict(text_type, filename, expected_dict_type):
    assert type(init_stats(text_type, filename)) == expected_dict_type


@pytest.mark.parametrize(
    "text_type, filename, expected_keys",
    [
        (
            2,
            "User text",
            ("statistic_type", "total_count", "word_frequencies", "longest_word"),
        )
    ],
)
def test_keys_dict(text_type, filename, expected_keys):
    data = init_stats(text_type, filename)
    for key in expected_keys:
        assert key in data


@pytest.mark.parametrize(
    "text_type, filename, expected_dict",
    [
        (
            2,
            "User text",
            {
                "statistic_type": "User text",
                "total_count": 0,
                "word_frequencies": {},
                "longest_word": "",
            },
        )
    ],
)
def test_values_dict(text_type, filename, expected_dict):
    assert init_stats(text_type, filename) == expected_dict
