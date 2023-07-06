#badger
from element_data import *

def get_element(atomic_num):
    for element in total_element:
        if element.atomic_num == atomic_num:
            return element