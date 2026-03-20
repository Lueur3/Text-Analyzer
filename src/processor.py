from typing import Dict, List, Tuple


def init_stats() -> Dict:
    dc_stat = {"total_count": 0, "word_frequencies": {}, "longest_word": ""}

    return dc_stat


def update_stats(line: str, stats: Dict):
    words = line.split()
    for word in words:
        stats["total_count"] += 1

        stats["word_frequencies"][word] = stats["word_frequencies"].get(word, 0) + 1

        stats["longest_word"] = max(word, stats["longest_word"], key=len)


def get_top_words(word_frequencies: Dict, n: int = 3) -> List[Tuple[str, int]]:
    result = sorted(word_frequencies.items(), key=lambda item: -item[1])[:n]
    return result
