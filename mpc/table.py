"""Docstring.

```python

def func(input1, input2, input3):
    return result1, result2, result3, result4

analysis = table(n_procs=5, db_filename='some_sqllite_db.db',
                 columns=['result1', 'result2', 'result3', 'result4'],
                 index=dict(input1=range(10), input2=np.linspace(0., 5.),
                              input3=['a', 'b']),
                 time_complexity='input1^3 * input2')
analysis()
```

"""


class table(object):
    """Docstring."""
    def __init__(self, n_proc=1, db_filename, columns, index, time_complexity):
        """Docstring."""
        pass

    def __call__(self):
        """Docstring."""
        pass
