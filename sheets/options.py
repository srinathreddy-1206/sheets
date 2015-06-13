from __future__ import print_function

class Dialect(object):
    """
    A Container for options that control how a CSV file should be handled when
    converting it to a set of objects.

    has_header_row
        A Boolean indicating whether the file has a row containing header values.
        If True, the row will skipped when looking for data.
        Defaults to False.
    For a list of additional options that can be passed in, see documentation
    for the dialects and formatting parameters of Python's csv module at
    http://docs.python.org/library/csv.html#dialects-and-formatting-parameters
    """
    def __init__(self, has_header_row = False, **kwargs):
        self.has_header_row = has_header_row
        self.csv_dialect = kwargs


