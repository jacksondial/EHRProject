"""EHR Analysis with SQLite."""
import sqlite3
import os

if os.path.exists("ehr.db"):
    os.remove("ehr.db")

con = sqlite3.connect("ehr.db")

cur = con.cursor()


def parse_patients(patient_file: str):
    """build patient table and insert patients into patient table."""
    cur.execute(
        """
        CREATE TABLE patient(
            [patient_id] TEXT PRIMARY KEY,
            [patient_gender] TEXT,
            [patient_dob] TEXT,
            [patient_race] TEXT,
            [patient_marital] TEXT,
            [patient_language] TEXT,
            [patient_pop_below_pov] FLOAT
        )
        """
    )

    pat_file = open(patient_file)
    next(pat_file)
    for line in pat_file:
        items = line.strip().split("\t")
        data = [items[0], items[1], items[2], items[3], items[4], items[5], items[6]]
        cur.execute("INSERT INTO patient VALUES(?, ?, ?, ?, ?, ?, ?)", data)


parse_patients("patient_test.txt")

con.commit()

# test = cur.execute("SELECT * FROM patient")

# for row in test:
#     print(row)


def parse_labs(given_lab: str):
    """Insert labs into lab table."""
    cur.execute(
        """
        CREATE TABLE lab(
            [patient_id] TEXT NOT NULL,
            [admission_id] INTEGER NOT NULL,
            [lab_name] TEXT,
            [lab_value] FLOAT,
            [lab_units] TEXT,
            [lab_date_time] TEXT,
            CONSTRAINT PK_lab PRIMARY KEY (patient_id, admission_id)
        )
        """
    )

    lab_file = open(given_lab)
    next(lab_file)
    for line in lab_file:
        items = line.strip().split("\t")
        data = [items[0], items[1], items[2], items[3], items[4], items[5]]
        cur.execute("INSERT INTO lab VALUES(?, ?, ?, ?, ?, ?)", data)


parse_labs("lab_test.txt")

con.commit()

# test_lab = cur.execute("SELECT * FROM lab")
# for row in test_lab:
#     print(row)

# sick_patients


def sick_patients(given_name: str, gl: str, given_value: float) -> list[str]:
    """Give ID numbers for patients that are 'sick'."""
    inputs = [given_value, given_name]
    sick = cur.execute(
        f"""
        SELECT DISTINCT patient_id
        FROM lab
        WHERE lab_value {gl} ? AND lab_name = ?
        """,
        inputs,
    )
    patient_list = []
    for row in sick:
        patient_list.append(row[0])
    return patient_list


# print(sick_patients("CBC: MCH", ">", 3.0))

# num_older_than


def num_older_than(age: float) -> list[tuple[int, int]]:
    """Find number of patients older than a given age."""
    age_iterable = [age]
    older = cur.execute(
        """
        SELECT COUNT(patient_id)
        FROM patient
        WHERE (julianday('now') - julianday(patient_dob)) / 365.25 > ?
        """,
        age_iterable,
    )
    test = older.fetchall()[0][0]
    return test


# print(num_older_than(25.0))


def first_age(patient_test: str) -> int:
    """Compute age at first admisison for a given patient."""
    patient_list = [patient_test]
    age_cur = cur.execute(
        """
        SELECT (julianday(l.lab_date_time) - julianday(p.patient_dob)) / 365.25
        FROM patient p
        LEFT JOIN lab l
        ON p.patient_id = l.patient_id
        WHERE p.patient_id = ? AND l.admission_id = 1
        """,
        patient_list,
    )
    age = int(age_cur.fetchall()[0][0])
    return age


# first_age("1A8791E3-A61C-455A-8DEE-763EB90C9B2C")

# con.close()
