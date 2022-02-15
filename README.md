# EHRProject

1. For End Users:
    This repository is made to analyze Electronic Heath Record (EHR) data. It provides a few simple descriptive statistics on the data provided. Each of the functions expect data of a particular structure, as can be seen in the docstrings (found just below the 'def function_name(...):' part of the modules) for each function.

    In general, the expected file input is a '.txt' file, structured in the way of rows and columns, with each column distinguished by a space or by multiple spaces, and each row distingueshed by a new line. As mentioned earlier, the 'column' number that is expected to contain given information is given in the docstring of each function.


2. For Contributors:
    **Testing**
    To test the _ehr analysis_ python file using the _pytest_ library, use the following code:
    
````
pytest test_ehr_analysis.py
```

