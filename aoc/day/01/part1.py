from pathlib import Path


def get_total_distance(raw: str) -> int:
    lines = raw.splitlines()
    list1, list2 = zip(*(line.split("   ") for line in lines))
    s1, s2 = sorted(list1), sorted(list2)
    return sum(abs(int(x) - int(y)) for x, y in zip(s1, s2))


def main():
    test_result = get_total_distance(
        """3   4
4   3
2   5
1   3
3   9
3   3"""
    )
    test_expected = 11
    assert test_result == test_expected, f"Expected {test_expected}, got {test_result}"

    data = open(Path(__file__).parent / "data.txt").read()
    result = get_total_distance(data)
    print(f"Total distance is {result}")


if __name__ == "__main__":
    main()
