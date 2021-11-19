# [Bite 33. Transpose a data structure](https://codechalleng.es/bites/33/)

Good luck and please share you code in the Bite forums upon completion.

For questions use [our Slack](https://pybites.slack.com/archives/C6BGDQQ3B) (no spoilers please).

Check out our full catalogue of Bites of Py [here](https://codechalleng.es/bites/catalogue).

Enjoy and keep calm and code in Python!

Sometimes you need to restructure a nested data structure. For example you can convert a `dict` in a `list` of (`key`, `value`) `tuple` via `dict.items()`.In this Bite a real world scenario where we wanted to plot some data from a `Counter dict`. For plots you typically need 2 lists: X + Y axis or labels + values. So we needed an easy way to transpose data structures.Complete the `transpose`function to do just that. It has to work for both dicts and lists of (named)tuples. Examples given in the _docstring_. See also the _TESTS_ tab. Have fun!

## Bite 33: Transpose a data structure

### Example Dataset #1 Dictionary

```Python
data = {'2017-8': 19, '2017-9': 13}
In:transpose(data)
Out: [('2017-8', '2017-9'), (19, 13)]
```

### Example Dataset #2 List of (Named) Tuples

```Python
data = [
    Member(
        name='Bob',
        since_days=60,
        karma_points=60
        bitecoin_earned=56
    ),
    Member(
        name='Julian',
        since_days=221,
        karma_points=34,
        bitecoin_earned=78
    )
]
In: transpose(data)
Out: [('Bob', 'Julian'), (60, 221), (60, 34), (56, 78)
```
