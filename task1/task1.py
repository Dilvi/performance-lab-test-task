import sys
from math import gcd

def circular_path(size, interval):
    step = (interval - 1) % size
    path_length = size // gcd(size, step)
    return "".join(str((i * step) % size + 1) for i in range(path_length))

def main():
    if len(sys.argv) != 5:
        print("Нужно указать четыре целых числа.", file=sys.stderr)
        sys.exit(2)

    try:
        n1, m1, n2, m2 = map(int, sys.argv[1:])
    except ValueError:
        print("Все аргументы должны быть целыми числами.", file=sys.stderr)
        sys.exit(2)

    if min(n1, m1, n2, m2) < 1:
        print("Все числа должны быть больше нуля.", file=sys.stderr)
        sys.exit(2)
    print(circular_path(n1, m1) + circular_path(n2, m2))


if __name__ == "__main__":
    main()
