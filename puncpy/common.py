import collections


def process_tagged_text(items):
    if not isinstance(items, collections.abc.Sequence):
        raise TypeError("items should be list")

    for item in items:
        print('item from tagged text :: {}'.format(item))
