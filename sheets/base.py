from __future__ import print_function
from sheets import options

class RowMeta(type):
    def __init__(cls, name, bases, attrs):
        if 'Dialect' in attrs:
            #Filter out Python's own additions to the namespace
            items = attrs.pop('Dialect').__dict__.items()
            items = dict((k,v) for (k,v) in items if not k.startswith('__'))
        else:
            #No Dialect options were explicitly defined.
            items = {}
        cls._dialect = options.Dialect(**items)
        for key, attr in attrs.items():
            if hasattr(attr, 'attach_to_class'):
                attr.attach_to_class(cls,name,cls._dialect)
        #Sort the columns according to their order of instantiation
        cls._dialect.columns.sort(key = lambda column: column.counter)
        super(RowMeta, cls).__init__(name, bases, attrs)


class Row(object, metaclass=RowMeta):
    __metaclass__ = RowMeta
    pass
