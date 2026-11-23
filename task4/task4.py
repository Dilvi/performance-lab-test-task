import sys

def main():
    if len(sys.argv) != 2:
        print("Нужно указать путь к файлу с числами.", file=sys.stderr)
        sys.exit(2)
        
    try:
        with open(sys.argv[1], encoding="utf-8-sig") as file:
            numbers = [int(line) for line in file if line.strip()]
    except FileNotFoundError as error:
        print(f"Файл не найден: {error.filename}", file=sys.stderr)
        sys.exit(2)
    except OSError:
        print("Не удалось прочитать файл.", file=sys.stderr)
        sys.exit(2)
    except ValueError:
        print("В каждой строке должно быть одно целое число.", file=sys.stderr)
        sys.exit(2)
        
    if not numbers:
        print("Файл не должен быть пустым.", file=sys.stderr)
        sys.exit(2)
        
    numbers.sort()
    median = numbers[len(numbers) // 2]
    moves = sum(abs(number - median) for number in numbers)
    
    if moves <= 20:
        print(moves)
    else:
        print("20 ходов недостаточно для приведения всех элементов массива к одному числу")

if __name__ == "__main__":
    main()
