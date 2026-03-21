import pytest
from src.processor import init_stats, update_stats, get_top_words


@pytest.mark.parametrize(
    "text_type, filename",
    [(2, "User text")],
)
def test_type_dict(text_type, filename):
    assert isinstance((init_stats(text_type, filename)), dict)


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
def empty_dict():
    dc = init_stats(2, "User text")
    return dc


@pytest.fixture
def example_dict():
    dc = init_stats(2, "User text")
    update_stats("apple banana ananas cherry banana apricot clackberry clementine", dc)
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
def test_update_stats(line, expected_res, empty_dict):
    update_stats(line, empty_dict)
    assert empty_dict["word_frequencies"] == expected_res


@pytest.mark.parametrize(
    "line, expected_res", [("apple banana ananas cherry", "cherry")]
)
def test_long_word_stats(line, expected_res, empty_dict):
    update_stats(line, empty_dict)
    assert empty_dict["longest_word"] == expected_res


def test_empty_update(empty_dict):
    data = empty_dict
    update_stats("", empty_dict)
    assert empty_dict == data


@pytest.mark.parametrize(
    "line, expected_res",
    [
        (
            "banana apple banana cherry banana apple ananas",
            {"banana": 3, "apple": 2, "cherry": 1, "ananas": 1},
        )
    ],
)
def test_duplicate_words(line, expected_res, empty_dict):
    update_stats(line, empty_dict)
    assert empty_dict["word_frequencies"] == expected_res


@pytest.mark.parametrize(
    "line, expected_res",
    [("banana apple cherry cherry", {"banana": 2, "apple": 2, "cherry": 4})],
)
def test_sum_effects(line, expected_res, empty_dict):
    update_stats(line, empty_dict)
    update_stats(line, empty_dict)
    assert empty_dict["word_frequencies"] == expected_res


def test_sort_words(example_dict):
    assert get_top_words(example_dict["word_frequencies"]) == [
        ("banana", 2),
        ("apple", 1),
        ("ananas", 1),
    ]


def test_count_words(example_dict):
    assert len(get_top_words(example_dict["word_frequencies"], 5)) == 5


@pytest.mark.parametrize(
    "ex_dict, expected_res",
    [
        (
            {
                "banana": 2,
                "apple": 1,
                "ananas": 1,
            },
            [
                ("banana", 2),
                ("apple", 1),
                ("ananas", 1),
            ],
        )
    ],
)
def test_not_enough_data(expected_res, ex_dict):
    assert get_top_words(ex_dict, 5) == expected_res


def test_empty_data(empty_dict):
    assert get_top_words(empty_dict["word_frequencies"]) == []
