import random, operator

class Item():
    def __init__(self, ID, value, volume):
        self.ID = ID
        self.value = value
        self.volume = volume
        self.ratio = self.value / self.volume

    def to_string(self):
        return "[ID:" + str(self.ID) + ', ratio: ' + str(round(self.ratio, 2)) + ']'
        
    def to_string_extended(self):
        return "[ID:" + str(self.ID) + ', value:' + str(self.value) + ', volume: ' + str(self.volume) + ', ratio: ' + str(round(self.ratio, 2)) + ']'

class Items():
    def __init__(self):
         self.items = []

    def add_item(self, item):
        self.items.append(item)

    def generate_items(self, num_of_items):
        for i in range(num_of_items):
            self.add_item(Item(i, random.randint(1,num_of_items), random.randint(1,num_of_items)))

    def sort_items(self):
        self.items.sort(reverse=True, key=operator.attrgetter('ratio'))

    def get_items(self):
        return self.items

    def get_list_of_volumes(self):
        return [item.volume for item in self.items]

    def get_list_of_values(self):
        return [item.value for item in self.items]

    def print_contents(self, extend):
        str_represantion_list = []

        if extend:   
            for item in self.items:
                str_represantion_list.append(item.to_string_extended())
        else:
            for item in self.items:
                str_represantion_list.append(item.to_string())            

        print('->'.join(str_represantion_list))


        print('sum of values: ' + str(sum(item.value for item in self.items)))

class Knapsack():
    def __init__(self, volume):
         self.items = Items()
         self.volume_left = volume
         self.volume_max = volume


