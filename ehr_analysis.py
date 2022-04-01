"""
I chose a dictionary for this assignment because the first function
'num_older_than' can be computed in O(N) time. Though in the second
function, the 'sick_patients' function, using a dynamic array I
BELIEVE I could achieve O(N) instead of O(N^2), the dictionary made
more sense to me when creating each of the functions, so I went with
that.
"""
from datetime import date


def parse_data(filename: str) -> dict[str, list[str]]:
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
        items = line.split("\t")  # O(1)
        key, values = items[0], items[1:]  # O (1)
        my_dict.setdefault(key, []).extend(values)  # O(1)
    return my_dict  # O(1)


def num_older_than(age: float, patient_dict: dict[str, list[str]]) -> int:
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
    for values in patient_dict.values():  # O(N)
        just_date = values[1].split()[0]
        year, month, day = just_date.split("-")  # O(3)
        patient_age = today - date(int(year), int(month), int(day))  # O(3)
        if patient_age.days > age_in_days:  # O(1)
            count_older += 1  # O(1)
    return count_older  # O(1)


def sick_patients(
    lab: str, gl: str, value: float, lab_dict: dict[str, list[str]]
) -> list[str]:
    """
    Parse data and return the patient ID's of any with a test value above
    or below a given value for a given test measurement.
    """
    patient_list = dict()  # O(1)
    lab_name = lab.split()  # O(1)
    num_words = len(lab_name)  # O(1)
    for key, values in lab_dict.items():  # O(N)
        test = list(values)  # O(1)
        for i in range(len(test)):  # O(N)
            if test[i : (i + num_words)] == lab_name:  # O(1)
                if gl == ">":  # O(1)
                    if float(test[i + num_words]) > value:  # O(1)
                        patient_list[key] = key  # O(1)
                elif gl == "<":  # O(1)
                    if float(test[i + num_words]) < value:  # O(1)
                        patient_list[key] = key  # O(1)
                else:
                    raise ValueError(f"Unexpected character: {gl}")
    return list(patient_list.keys())  # O(1)


def sick_patients2(
    lab_name: str, gl: str, value: float, lab_dict: dict[str, list[str]]
) -> list:
    patient_list = []
    for key, values in lab_dict.items():
        test = list(values)
        # print(test)
        if test[1] == lab_name:
            if gl == "<":
                if float(test[2]) < value:
                    patient_list.append(key)
            elif gl == ">":
                if float(test[2]) > value:
                    patient_list.append(key)
            else:
                raise ValueError(f"Unexpected character: {gl}")
    return patient_list


def first_age(
    patient_id: str, patient_dict: dict[str, list[str]], lab_dict: dict[str, list[str]]
) -> int:
    """
    Compute the age of given patient at first admission.
    It is assumed that the first recorded lab record for a patient is their
    first in the file. We also assume the date is in the format of
    YYYY-MM-DD. The date item for the patient file is assumed
    to be the second in the list that is the items in a dictionary,
    and the date item for the labs file is assumed to be the second
    from the last item
    """
    patient_dob = patient_dict.get(patient_id)[1]
    patient_dob2 = patient_dob.split()[0]
    visit_day = lab_dict.get(patient_id)[4]
    visit_day2 = visit_day.split()[0]

    dob_year, dob_month, dob_day = patient_dob2.split("-")
    ad_year, ad_month, ad_day = visit_day2.split("-")
    age_at_admission = date(int(ad_year), int(ad_month), int(ad_day)) - date(
        int(dob_year), int(dob_month), int(dob_day)
    )
    return int(age_at_admission.days / 365.25)
