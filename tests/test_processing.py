from src.processing import filter_by_state, sort_by_date


def test_processing_func_sort(list_dict: list, list_sort_by_date: list):
    assert sort_by_date(list_dict) == list_sort_by_date


def test_processing_func_filter(list_dict, list_filter_by_state):
    assert filter_by_state(list_dict, "EXECUTED") == list_filter_by_state
