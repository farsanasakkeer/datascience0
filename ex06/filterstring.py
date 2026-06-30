import sys
from ft_filter import ft_filter


def is_long_enough(n):
    def checker(word):
        return len(word) >= n
    return checker


def main():
    """Main function"""
    try:
        assert len(sys.argv) == 3, "wrong number of arguments"
        text = sys.argv[1]
        n = sys.argv[2]
        assert n.isdigit(), "second argument is not a positive integer"
        n = int(n)
        words = text.split()
        result = ft_filter(is_long_enough(n), words)
        print(result)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()