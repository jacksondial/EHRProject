# EHRProject

1. For End Users:
    This repository is made to analyze Electronic Heath Record (EHR) data. It provides a few simple descriptive statistics on the data provided. Each of the functions expect data of a particular structure, as can be seen in the docstrings (found just below the 'def function_name(...):' part of the modules) for each function.

    In general, the expected file input is a '.txt' file, structured in the way of rows and columns, with each column distinguished by a tab, and each row distingueshed by a new line. As mentioned earlier, the 'column' number that is expected to contain given information is given in the docstring of each function.

    The '*num_older_than*' function takes an age as a float, and a dictionary of patients that should be parsed by the *parse_data* function, and returns the number of patients that are older than the age that is inputted.

    The '*sick_patients2*' function takes a specific lab name as a string (for example, "CBC: RED BLOOD CELL COUNT"), a second string that should be either ">" or "<", a lab value as a float, and a dictionary of lab values that should have been parsed by the *parse_data* function. It returns a list of patient IDs for each patient that has a higher/lower (depending on the second input) lab value for the given lab than the given value.

    The '*first_age*' function takes in a particular patient's ID, and two dictionaries, one of patients and one of labs each parsed by the *parse_data* function.

2. For Contributors:
    **Testing**
    To test the _ehr analysis_ python file using the _pytest_ library, use the following code in your terminal, where the test file and file to be tested are located:
    
````
pytest test_ehr_analysis.py
```

