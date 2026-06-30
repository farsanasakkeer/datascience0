def ft_filter(function, iterable):
    """a
    abc
1344
"""
    if function is None:
        return [item for item in iterable if item]
    return [item for item in iterable if function(item)]


def main():
    """Quick test of ft_filter."""
    nums = [0, 1, 2, 3, 4, 5, 6, "", "hi", None]

    print(ft_filter(lambda x: isinstance(x, int) and x % 2 == 0, nums))
    print(ft_filter(None, nums))
    print(ft_filter.__doc__)


if __name__ == "__main__":
    main()