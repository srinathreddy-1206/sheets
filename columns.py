from __future__ import print_function

class Column(object):
    """
    An Individual Column within a CSV file.This serves as a base for attributes and
    methods that are common to all types of columns. Subclass of Column will define behavior
    for more specific data types.
    """

    def __init__(self, title = None, required = True):
        self.title = title
        self.required = required

        def attach_to_class(self, cls, name, options):
            self.cls = cls
            self.name = name
            self.options = options

            if self.title is None:
                # Check for None so that an empty string will skip this header
                self.title = name.replace('_', ' ')
