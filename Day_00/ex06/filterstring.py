import sys


def main():
    if len(sys.argv) != 3 or not (
        isinstance(sys.argv[1], str) and isinstance(sys.argv[2], int)
    ):
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    else:
        N = int(sys.argv[2])
        try:
            list_words = sys.argv[1].split(" ")
            filtered_list = [word for word in list_words if len(word) > N]
        except Exception as e:
            print(e)
            sys.exit(1)
        print(filtered_list)


if __name__ == "__main__":
    main()
