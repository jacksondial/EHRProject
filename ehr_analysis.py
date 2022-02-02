# Part 1
"""
I chose a dictionary for this assignment because the first function
'num_older_than' can be computed in O(N) time. Though in the second
function, the 'sick_patients' function, using a dynamic array I
BELIEVE I could achieve O(N) instead of O(N^2), the dictionary made
more sense to me when creating each of the functions, so I went with
that.
"""
from datetime import date


def parse_data(filename: str) -> dict:
    """
    Read data and create dictionary.
    This function operates in time as follows:
    1 + 1 + 1 + N(1 + 1 + 1) + 1 = 3N + 4 = N
    O(N)
    """
    my_dict: dict = dict()  # O(1)
    file = open(filename)  # O(1)
    next(file)  # O(1)
    for line in file:  # O (N)
        items = line.split()  # O(1)
        key, values = items[0], items[1:]  # O (1)
        my_dict.setdefault(key, []).extend(values)  # O(1)
    return my_dict  # O(1)


patientdat = parse_data("C:/Users/jacks/BIOSTAT821/EHRProject/Patient.txt")
labdat = parse_data("C:/Users/jacks/BIOSTAT821/EHRProject/Labs.txt")


def num_older_than(age: float) -> int:
    """
    Parse data and count the number of patients older than given age.
    We assume the patient's date of birth is the third column.
    This function operates in time as follows:
    1 + 1 + 1 + N(3 + 3 + 1 + 1) + 1 = 8N + 4 = N
    O(N)
    """
    count_older = 0  # O(1)
    age_in_days = age * 365.25  # O(1)
    today = date.today()  # O(1)
    for values in patientdat.values():  # O(N)
        year, month, day = values[1].split("-")  # O(3)
        patient_age = today - date(int(year), int(month), int(day))  # O(3)
        if patient_age.days > age_in_days:  # O(1)
            count_older += 1  # O(1)
    return count_older  # O(1)


print(num_older_than(51.2))


def sick_patients(lab: str, gl: str, value: float) -> list:
    """
    Parse data and return the patient ID's of any with a test value above
    or below a given value for a given test measurement.
    This function operates in time as follows:
    1 + 1 + 1 + N(1 + N(1 + 1 + 1 + 1)) + 1 = N(1 + 4N) + 4 = N + 4N^2 = N^2
    O(N^2)
    """
    patient_list = dict()  # O(1)
    lab_name = lab.split()  # O(1)
    num_words = len(lab_name)  # O(1)
    for key, values in labdat.items():  # O(N)
        test = list(values)  # O(1)
        for i in range(len(test)):  # O(N)
            if test[i : (i + num_words)] == lab_name:  # O(1)
                if gl == ">":  # O(1)
                    if float(test[i + num_words]) > value:  # O(1)
                        patient_list[key] = key  # O(1)
    return list(patient_list.keys())  # O(1)


print(sick_patients("CBC: RED BLOOD CELL COUNT", ">", 6.9))
