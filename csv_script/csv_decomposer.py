import csv


def read_csv(file_paths: list[str]):
    result = []
    for path in file_paths:
        with open(path) as file:
            dict_csv = csv.DictReader(file)
            result.extend(list(dict_csv))
    return result