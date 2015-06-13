from __future__ import print_function

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

