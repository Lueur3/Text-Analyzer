import pytest
from src.processor import init_stats, update_stats, get_top_words


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


@pytest.fixture
def example_dict():
    dc = init_stats("User text")
    return dc


@pytest.mark.parametrize(
    "line, expected_res",
    [
        (
            "apple banana apple",
            {"apple": 2, "banana": 1},
        )
    ],
)
def test_update_stats(line, expected_res, example_dict):
    update_stats(line, example_dict)
    assert example_dict["word_frequencies"] == expected_res


@pytest.mark.parametrize(
    "line, expected_res", [("apple banana ananas cherry", "cherry")]
)
def test_long_word_stats(line, expected_res, example_dict):
    update_stats(line, example_dict)
    assert example_dict["longest_word"] == expected_res


def test_empty_update(example_dict):
    data = example_dict
    update_stats("", example_dict)
    assert example_dict == data


@pytest.mark.parametrize(
    "line, expected_res",
    [
        (
            "banana apple banana cherry banana apple ananas",
            {"banana": 3, "apple": 2, "cherry": 1, "ananas": 1},
        )
    ],
)
def test_duplicate_words(line, expected_res, example_dict):
    update_stats(line, example_dict)
    assert example_dict["word_frequencies"] == expected_res


@pytest.mark.parametrize(
    "line, expected_res",
    [("banana apple cherry cherry", {"banana": 2, "apple": 2, "cherry": 4})],
)
def test_sum_effects(line, expected_res, example_dict):
    update_stats(line, example_dict)
    update_stats(line, example_dict)
    assert example_dict["word_frequencies"] == expected_res
