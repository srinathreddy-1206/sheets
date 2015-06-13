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
                attr.attach_to_class(cls,key,cls._dialect)
        #Sort the columns according to their order of instantiation
        cls._dialect.columns.sort(key = lambda column: column.counter)
        super(RowMeta, cls).__init__(name, bases, attrs)


class Row(object, metaclass=RowMeta):
    def __init__(self, *args, **kwargs):
        #First, make sure the arguments make sense
        column_names = [column.name for column in self._dialect.columns]
        if len(args) > len(column_names):
            msg = "__init__() takes at most %d arguments (%d given)"
            raise TypeError(msg % (len(column_names), len(args)))
        for name in kwargs:
            if name not in column_names:
                msg = "__init__() got an unexpected keyword argument '%s'"
                raise TypeError(msg % name)
        for i, name in enumerate(column_names[:len(args)]):
            if name in kwargs:
                msg = "__init__() got multiple values for keyword argument '%s'"
                raise TypeError(msg % name)
            kwargs[name]=args[i]
        #Now populate the actual values on the object
        for column in self._dialect.columns:
            try:
                value = column.to_python(kwargs[column.name])
            except KeyError:
                #No Value was provided
                value = None
            setattr(self, column.name, value)

    #__metaclass__ = RowMeta
    pass
