import pytest
from csv_script.csv_decomposer import read_csv
from csv_script.report_generator.generator import ReportGenerator


def test_full_with_real_data():
    data = read_csv(['tests/test_data.csv'])
    
    generator = ReportGenerator(data)
    result = generator.get_performance_report()
    
    positions_from_csv = {row['position'] for row in data}
    positions_from_report = {row['position'] for row in result}
    
    assert positions_from_csv == positions_from_report
    assert len(result) == len(positions_from_csv)


def test_performance_report_real_data():
    data = read_csv(['tests/test_data.csv'])
    generator = ReportGenerator(data)
    result = generator.get_performance_report()
    
    for item in result:
        assert set(item.keys()) == {'position', 'average_performance'}
        assert isinstance(item['position'], str)
        assert isinstance(item['average_performance'], float)