#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = [None for i in range(length)]
    my_tickets = dict()

    for i in tickets:
        my_tickets.update({i.source: i.destination})
        
    
    for i in range(length):
        if i == 0:
            route[i] = my_tickets.get('NONE')
        else:
            route[i] = my_tickets.get(route[i - 1])


    return route


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

print(reconstruct_trip(tickets, 3))