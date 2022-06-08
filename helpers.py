import random

def generate_list_of_items(num_of_items):
    ls = []

    for i in range(num_of_items):
        ls.append((random.randint(1,num_of_items), random.randint(1,num_of_items)))

    return ls

def sort_by_ratio(list):
    list.sort(reverse=True, key=ratio)

def ratio(elem):
    return elem[0] / elem[1]