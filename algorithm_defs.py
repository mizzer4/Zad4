from class_defs import Knapsack, Items

"""
def greedy_algorithm(knapsack, items_param):
    items = items_param.get_items()

    for item in items:
        if item.volume <= knapsack.volume_left:
            knapsack.items.add_item(item)
            knapsack.volume_left -= item.volume
"""
def greedy_algorithm(volume_left, values, volumes):
    value = 0

    for i in range(len(volumes)):
        if volumes[i] <= volume_left:
            value += values[i]
            volume_left -= volumes[i]

    return value

def dynamic_prog_algorithm(num_items, max_volume, values, volumes):

    table = [[0 for x in range(max_volume + 1)] for y in range(num_items + 1)]

    for item in range(num_items + 1):
        for vol_unit in range(max_volume + 1):
            if item==0 or vol_unit==0:
                table[item][vol_unit] = 0
            elif volumes[item-1] <= vol_unit:
                table[item][vol_unit] = max(values[item-1] + table[item-1][vol_unit - volumes[item-1]], table[item-1][vol_unit]) 
            else:
                table[item][vol_unit] = table[item-1][vol_unit]

    return table[num_items][max_volume]
