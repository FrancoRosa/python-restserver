#insert
#shell
#bubble
#merge
#quicksort
#bucket
#radix
#heap
#count
#bin
#ramdomizedSelect
#stooge
from time import sleep

def insertionSort(my_list):
    ## for every element in our array
    for index in range(1, len(my_list)):
        current = my_list[index]
        position = index

        while position > 0 and my_list[position-1] > current:
            print("Swapped {} for {}".format(my_list[position], my_list[position-1]))
            my_list[position] = my_list[position-1]
            print(my_list)
            position -= 1

        my_list[position] = current

    return my_list

my_list = [8,2,1,3,5,4]

# json = {'file': 'path', 'algorithm':'buble'}
  