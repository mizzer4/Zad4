from helpers import sort_by_ratio


def greedy_algorithm(items, volume_left):
    value = 0

    sort_by_ratio(items)

    for i in range(len(items)):
        if items[i][1] <= volume_left:
            value += items[i][0]
            volume_left -= items[i][1]
        
    return value

def dynamic_prog_algorithm(items, num_items, max_volume):

    table = [[0 for x in range(max_volume + 1)] for y in range(num_items + 1)]

    for item in range(num_items + 1):
        for vol_unit in range(max_volume + 1):
            if item==0 or vol_unit==0:
                table[item][vol_unit] = 0
            elif items[item-1][1] <= vol_unit:
                table[item][vol_unit] = max(items[item-1][0] + table[item-1][vol_unit - items[item-1][1]], table[item-1][vol_unit]) 
            else:
                table[item][vol_unit] = table[item-1][vol_unit]

    return table[num_items][max_volume]
