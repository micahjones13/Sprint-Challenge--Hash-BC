#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # add all of the weights into the ht
    v = 0
    for k in weights:
        # Makes the HT look like: [{4: 0}, {6: 1}, {10:2}, {15:3}, {16:4}]
        # makes it so we can return the correct indicies, since thats what the answer wants
        # print(k, 'K')
        hash_table_insert(ht, k, v)
        v += 1
    # find where limit - weight is in the HT
    for i in range(len(weights)):
        # this is where the value is that we want.
        # print(weights[i], 'weights[i]')
        # each = hash_table_retrieve(ht, weights[i])
        # print(each, 'each')
        #limit: 21
        match = limit - weights[i]
        # print(match, 'MATCH')
        # if the ideal pair exists in the HT, return it
        is_there = hash_table_retrieve(ht, match)

        if is_there != None:
            # print(is_there, i, 'ANSWER')
            # return the indexes of the perfect match
            return (is_there, i)
        # else:
        #     print('not there.')

    # print(ht.storage)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


weights = [4, 6, 10, 15, 16]
length = 5
limit = 21
get_indices_of_item_weights(weights, length, limit)
