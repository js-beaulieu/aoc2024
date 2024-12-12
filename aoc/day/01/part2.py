from collections import Counter
from pathlib import Path


def get_similarity_score(raw: str) -> int:
    lines = raw.splitlines()
    left, right = zip(*(line.split("   ") for line in lines))
    right_counts = Counter(right)
    return sum(int(value) * right_counts.get(value, 0) for value in left)


def main():
    test_result = get_similarity_score(
        """3   4
4   3
2   5
1   3
3   9
3   3"""
    )
    test_expected = 31
    assert test_result == test_expected, f"Expected {test_expected}, got {test_result}"

    data = open(Path(__file__).parent / "data.txt").read()
    result = get_similarity_score(data)
    print(f"Similarity score is {result}")


if __name__ == "__main__":
    main()
