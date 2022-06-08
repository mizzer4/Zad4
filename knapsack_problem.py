from helpers import generate_list_of_items
from algorithm_defs import greedy_algorithm, dynamic_prog_algorithm
from time import time_ns
from copy import deepcopy

import csv

def main():
    results = [["value_greedy", "totaltime_greedy", "value_dynamic", "totaltime_dynamic"]]

    for i in range(1,16):
        num_items = 1000
        max_volume = 1000 * i

        items = generate_list_of_items(num_items)

        items_greedy = deepcopy(items)
        items_dynamic = deepcopy(items)

        print('----------------------------')
        starttime_greedy = time_ns()
        value_greedy = greedy_algorithm(items_greedy, max_volume)
        endtime_greedy = time_ns()

        totaltime_greedy = int((endtime_greedy - starttime_greedy)/ (10 ** 6))
        print('-> greedy[' + str(1000 * i) + ']: ' + 'value = ' + str(value_greedy) + ', time = ' + str(totaltime_greedy) + 'ms')  

        starttime_dynamic = time_ns()
        value_dynamic = dynamic_prog_algorithm(items_dynamic, num_items, max_volume)
        endtime_dynamic = time_ns()

        totaltime_dynamic = int((endtime_dynamic - starttime_dynamic)/ (10 ** 6))
        print('-> dynamic[' + str(1000 * i) + ']: ' + 'value = ' + str(value_dynamic) + ', time = ' + str(totaltime_dynamic) + 'ms')  
        print('----------------------------')

        results.append([value_greedy, totaltime_greedy, value_dynamic, totaltime_dynamic])

    f = open('results.csv', 'w', newline='')
    writer = csv.writer(f)

    for row in results:
        writer.writerow(row)

    f.close()


if __name__=="__main__":
    main()
