# python_csv_script
Скрипт для анализа CSV файлов с данными о сотрудниках и генерации отчетов.

# Установка:
make install

# Запуск 1 файла:
uv run main.py --files data.csv --report performance

# Запуск 2 и более файлов:
uv run main.py --files data.csv data2.csv data3.csv --report performance

# Возможности расширения:
1. В файл csv_script/cli.py в константу CHOICES добавить название отчета в строчном формате.
2. Реализовать новый метод в csv_script/report_generator/generator.py по шаблону с get_{report_name}_report(). Метод должен возвращать список словарей для вывода tabulate
3. Добавить дополнительные валидации и проверки форматов данных.
4. Сортировка выводимых данных в алфавитном порядке или же по возрастанию/убыванию среднеарифметических значений

[![asciicast](https://asciinema.org/a/KNCDqVdVjAVWmRaX750aTuawt.svg)](https://asciinema.org/a/KNCDqVdVjAVWmRaX750aTuawt)

