from __future__ import print_function
"""
Compatible with: 3.x,
"""

class Column(object):
    """
    An Individual Column within a CSV file.This serves as a base for attributes and
    methods that are common to all types of columns. Subclass of Column will define behavior
    for more specific data types.
    """
    #This will be updated for each column's that's instantiated.
    counter = 0
    def __init__(self, title = None, required = True):
        self.title = title
        self.required = required
        self.counter = Column.counter
        Column.counter += 1

    def attach_to_class(self, cls, name, dialect):
            self.cls = cls
            self.name = name
            self.dialect = dialect

            if self.title is None:
                # Check for None so that an empty string will skip this header
                self.title = name.replace('_', ' ')
            dialect.add_column(self)

    def to_python(self, value):
        """
        Convert the given string to a native python object.
        """
        return value
    def to_string(self, value):
        """
        Convert the given python object to a string
        """
        return value

class StringColumn(Column):
    """
    A Column that contains data formatted as generic strings.
    """
    pass

class IntegerColumn(Column):
    """
    A Column that contains data in the form of numeric integers.
    """
    def to_python(self, value):
        return int(value)


class FloatColumn(Column):
    """
    A Column that contains data in the form of floating point numbers.
    """
    def to_python(self, value):
        return float(value)

import decimal
class DecimalColumn(Column):
    """
    A Column that contains data in the form of decimal values, represented
    in python by decimal.Decimal
    """
    def to_python(self, value):
        try:
            return decimal.Decimal(value)
        except decimal.InvalidOperation as e:
            raise ValueError(str(e))

import datetime
class DateColumn(Column):
    """
    A Column that contains data in the form of dates,
    represented in python by datetime.date

    format
        A strptime() - style format string.
        See http://docs.python.org/library/datetime.html for details
    """
    def __init__(self, *args, **kwargs):

        if 'format' in kwargs:
            self.format = kwargs.pop('format')
        else:
            self.format = '%Y-%m-%d'
        super(DateColumn, self).__init__(*args, **kwargs)

    def to_python(self, value):
        """
        Parse a string value according to self.format
        and return only the date portion
        """
        if isinstance(value, datetime.date):
            return value
        return datetime.datetime.strptime(value, self.format).date()
    def to_string(self, value):
        """
        Format a date according to self.format and return that string.
        """
        return value.strftime(self.format)

