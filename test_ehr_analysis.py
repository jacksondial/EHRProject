"""
Test the ehr_analysis module part 1. No particular function is needed to test
the parse_data function because it is used in the other two test functions.
"""
from ehr_analysis import parse_data, num_older_than, sick_patients

true_dict = {}
true_dict["12345"] = ["67890", "rbc", "23", "mg", "09MAR2021"]
true_dict["23456"] = ["78901", "wbc", "2", "mL", "20APR1999"]


def test_num_older_than():
    """Test the num_older_than function."""
    assert num_older_than(23, parse_data("test2.txt")) == 2
    assert num_older_than(25, parse_data("test2.txt")) == 1
    assert num_older_than(30, parse_data("test2.txt")) == 0


def test_sick_patients():
    """Test the sick_patients function."""
    assert sick_patients("wbc count", ">", 1, parse_data("test1.txt")) == ["23456"]
    assert sick_patients("rbc count", "<", 24, parse_data("test1.txt")) == ["12345"]
