#  Hint:  You may not need all of these.  Remove the unused functions.
# O(n)
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # set up hash table like {"pit":ticket1,"XNA":ticket2,...}
    src_tic = {x.source:x for x in tickets}
    # empty list
    route = []
    # set current(departure) ticket which with the source="None"
    # we found out that is ticket_5
    curr_ticket = src_tic["NONE"]
    # traverse until the destination is "None"
    while curr_ticket.destination != "NONE":
        # append the current ticket's destination to route
        route.append(curr_ticket.destination)
        # move to the next, update the cuurent ticket to the next fight ticket
        curr_ticket = src_tic[curr_ticket.destination]
    # for pass the test, append the last destination, since our expect output need it.
    route.append(curr_ticket.destination)
    return route

ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")
tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

length = len(tickets)
#print(tickets)
print(reconstruct_trip(tickets, length))
