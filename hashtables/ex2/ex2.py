#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    # print(tickets)
    # insert tickets in ht /// source and destination from class
    for t in tickets:
        hash_table_insert(hashtable, t.source, t.destination)

    # start = None
    # for i in range(len(tickets)):
    #     print(tickets[i].source, 'second for')
    #     if tickets[i].source == "NONE":
    #         # start now holds the beggining ticket. OBJ form tho
    #         start = tickets[i]
    #         # print(start, 'after')

    # print(start)
    # hash_start = hash_table_retrieve(hashtable, start.source)
    # # route[0] = start
    # print(hash_start)

    # * ---------------------------------------------------------------

    # count for iteration
    count = 0
    # current/start location
    cur = "NONE"
    # while the last elemetn in the route list is None, it means we haven't hit the end, so keep going
    while route[-1] is None:
        # find wehre the next flight is, store it here. The return of the hash_retrieve is the key of the next flight
        next_flight = hash_table_retrieve(hashtable, cur)
        # add the flight to the route list
        route[count] = next_flight
        # increment in order to keep moving through list
        count += 1
        # change cur to where you're at on the list now
        cur = next_flight

    print(route)
    return route


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

reconstruct_trip(tickets, 3)
