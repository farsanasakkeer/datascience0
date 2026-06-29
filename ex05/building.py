import sys
import string


def count_characters(text):
    """Count and print upper, lower, punctuation, spaces, and digits."""
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    punct = sum(1 for c in text if c in string.punctuation)
    spaces = sum(1 for c in text if c == ' ' or c == '\n')
    digits = sum(1 for c in text if c.isdigit())

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    """Main function to handle arguments and launch character counting."""
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            print("What is the text to count?")
            text = input()
        count_characters(text)
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except EOFError:
        print()


if __name__ == "__main__":
    main()