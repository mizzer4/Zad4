from class_defs import Items
from algorithm_defs import greedy_algorithm, dynamic_prog_algorithm
from time import time

def main():
    for i in range(1,16):
        num_items = 2000
        max_volume = 2000 * i

        items = Items()
        items.generate_items(num_items)
        items.sort_items()

        values = items.get_list_of_values()
        volumes = items.get_list_of_volumes()

        print('----------------------------')
        starttime_greedy = time()
        value_greedy = greedy_algorithm(max_volume, values, volumes)
        endtime_greedy = time()

        totaltime_greedy = int((endtime_greedy - starttime_greedy) * 1000)
        print('-> greedy[' + str(2000 * i) + ']: ' + 'value = ' + str(value_greedy) + ', time = ' + str(totaltime_greedy) + 'ms')  

        starttime_dynamic = time()
        value_dynamic = dynamic_prog_algorithm(num_items, max_volume, values, volumes)
        endtime_dynamic = time()

        totaltime_dynamic = int((endtime_dynamic - starttime_dynamic) * 1000)
        print('-> dynamic[' + str(2000 * i) + ']: ' + 'value = ' + str(value_dynamic) + ', time = ' + str(totaltime_dynamic) + 'ms')  
        print('----------------------------')

if __name__=="__main__":
    main()
