
import sys
from fractions import Fraction


def read_pairs(path):
    pairs = []
    with open(path, encoding="utf-8-sig") as file:
        for line in file:
            coordinates = line.split()
            if coordinates:
                x, y = coordinates
                pairs.append((Fraction(x), Fraction(y)))
    return pairs


def main():
    if len(sys.argv) != 3:
        print("Нужно указать пути к двум файлам.", file=sys.stderr)
        sys.exit(2)

    try:
        (cx, cy), (rx, ry) = read_pairs(sys.argv[1])
        points = read_pairs(sys.argv[2])
    except FileNotFoundError as error:
        print(f"Файл не найден: {error.filename}", file=sys.stderr)
        sys.exit(2)
    except OSError:
        print("Не удалось прочитать файлы.", file=sys.stderr)
        sys.exit(2)
    except (ValueError, ZeroDivisionError):
        print("Неверный формат координат.", file=sys.stderr)
        sys.exit(2)

    if rx <= 0 or ry <= 0:
        print("Полуоси должны быть больше нуля.", file=sys.stderr)
        sys.exit(2)

    if not 1 <= len(points) <= 100:
        print("В файле должно быть от 1 до 100 точек.", file=sys.stderr)
        sys.exit(2)

    for x, y in points:
        value = ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2
        if value == 1:
            print(0)
        elif value < 1:
            print(1)
        else:
            print(2)


if __name__ == "__main__":
    main()