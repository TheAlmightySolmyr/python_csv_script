import pytest
from csv_script.report_generator.generator import ReportGenerator


@pytest.fixture
def sample_data():
    return [
        {'position': 'Developer', 'performance': '1.0'},
        {'position': 'Developer', 'performance': '3.0'},
        {'position': 'Designer', 'performance': '2.0'},
    ]


@pytest.fixture
def single_position_data():
    return [
        {'position': 'Developer', 'performance': '5.0'},
    ]


@pytest.fixture
def multiple_identical_positions():
    return [
        {'position': 'QA', 'performance': '1.0'},
        {'position': 'QA', 'performance': '2.0'},
        {'position': 'QA', 'performance': '3.0'},
    ]


def test_get_performance_report_averages(sample_data):
    generator = ReportGenerator(sample_data)
    result = generator.get_performance_report()
    
    assert len(result) == 2
    developer_avg = next(r['average_performance'] for r in result if r['position'] == 'Developer')
    assert developer_avg == 2.0


def test_get_performance_report_handles_single_entry(single_position_data):
    generator = ReportGenerator(single_position_data)
    result = generator.get_performance_report()
    
    assert len(result) == 1
    assert result[0]['average_performance'] == 5.0


def test_choose_rep_type_returns_performance_report(sample_data):
    generator = ReportGenerator(sample_data)
    result = generator.choose_rep_type('performance')
    
    assert isinstance(result, list)
    assert all('position' in item for item in result)


def test_choose_rep_type_rejects_invalid_report(sample_data):
    generator = ReportGenerator(sample_data)
    with pytest.raises(ValueError):
        generator.choose_rep_type('invalid_report')


def test_multiple_identical_positions_correct_average(multiple_identical_positions):
    generator = ReportGenerator(multiple_identical_positions)
    result = generator.get_performance_report()
    
    assert len(result) == 1
    assert result[0]['average_performance'] == 2.0