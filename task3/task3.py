import json
import sys

def iter_nodes(nodes):
    pending = list(reversed(nodes))
    while pending:
        node = pending.pop()
        yield node
        pending.extend(reversed(node.get("values", [])))

def main():
    if len(sys.argv) != 4:
        print("Нужно указать пути к трём файлам.", file=sys.stderr)
        sys.exit(2)
    values_path, tests_path, report_path = sys.argv[1:]

    try:
        with open(values_path, encoding="utf-8-sig") as file:
            values = json.load(file)
        with open(tests_path, encoding="utf-8-sig") as file:
            report = json.load(file)
        results = {
            node["id"]: node["value"]
            for node in iter_nodes(values["values"])
            if "value" in node
        }
        for node in iter_nodes(report["tests"]):
            if "value" in node and node["id"] in results:
                node["value"] = results[node["id"]]
    except FileNotFoundError as error:
        print(f"Файл не найден: {error.filename}", file=sys.stderr)
        sys.exit(2)
    except (OSError, ValueError, TypeError, KeyError, AttributeError, RecursionError):
        print("Неверный формат данных или ошибка чтения файла.", file=sys.stderr)
        sys.exit(2)
    try:
        with open(report_path, "w", encoding="utf-8") as file:
            json.dump(report, file, ensure_ascii=False, indent=2)
            file.write("\n")
    except (OSError, ValueError, TypeError, RecursionError):
        print("Не удалось записать отчёт.", file=sys.stderr)
        sys.exit(2)

if __name__ == "__main__":
    main()
