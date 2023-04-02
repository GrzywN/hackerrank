if __name__ == "__main__":
    n = int(input().strip())
    is_odd = n % 2 == 1

    WEIRD = "Weird"
    NOT_WEIRD = "Not Weird"

    if is_odd:
        print(WEIRD)
    elif n >= 2 and n <= 5:
        print(NOT_WEIRD)
    elif n >= 6 and n <= 20:
        print(WEIRD)
    else:
        print(NOT_WEIRD)
