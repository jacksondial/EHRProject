"""
Test the ehr_analysis module part 1. No particular function is needed to test
the parse_data function because it is used in the other two test functions.
"""
from ehr_analysis import parse_data, num_older_than, sick_patients2, first_age

true_dict = {}
true_dict["1A8791E3-A61C-455A-8DEE-763EB90C9B2C"] = [
    "1",
    "rbc",
    "23",
    "mg",
    "09MAR2021",
]
true_dict["23456"] = ["78901", "wbc", "2", "mL", "20APR1999"]


def test_num_older_than():
    """Test the num_older_than function."""
    assert num_older_than(23, parse_data("patient_test.txt")) == 5
    assert num_older_than(25, parse_data("patient_test.txt")) == 4
    assert num_older_than(30, parse_data("patient_test.txt")) == 0


def test_sick_patients2():
    """Test the sick_patients function."""
    assert sick_patients2(
        "CBC: RED BLOOD CELL COUNT", ">", 5, parse_data("lab_test.txt")
    ) == ["DB22A4D9-7E4D-485C-916A-9CD1386507FB"]


def test_first_age():
    """Test the first_age function."""
    assert (
        first_age(
            "1A8791E3-A61C-455A-8DEE-763EB90C9B2C",
            parse_data("patient_test.txt"),
            parse_data("lab_test.txt"),
        )
        == 3
    )
