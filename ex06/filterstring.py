import sys
from ft_filter import ft_filter


def is_long_enough(n):
    """Return a function checking if a string is at least n characters."""
    def checker(word):
        """Check if word length is greater or equal to n."""
        return len(word) >= n
    return checker


def main():
    """Main function: filter words from a string by minimum length."""
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