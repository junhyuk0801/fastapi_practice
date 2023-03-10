from typing import List, Tuple, Set, Dict, Union

# list
def process_items_list(items: List[str]):
    for item in items:
        print(item)


# tuple
def process_items_tuple(items: Tuple[int, int, str]):
    for item in items:
        print(item)


# set
def process_items_set(items: Set[int]):
    for item in items:
        print(item)


# dict
def process_items_dict(items: Dict[str, float]):
    for item in items:
        print(item)


# union
def process_item_union(item: Union[int, str]):
    print(item)


# optional
# the field of parameter 'item' can be empty
def process_item_optional(item: Union[str, int] = None):
    if item is not None:
        print(item)
