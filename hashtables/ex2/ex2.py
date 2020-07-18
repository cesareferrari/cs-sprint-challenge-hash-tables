#  Hint:  You may not need all of these.  Remove the unused functions.

"""
Input:
array of Ticket objects (ticket.source, ticket.destination)
If ticket has source == "NONE", it's first stop
If ticket has destination == "NONE", it's last stop

Output:
Array of strings with airport code
"""

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # initialize airports dict and route list
    airports = {}
    route = []


    # For all the tickets in the input array:
    # Create airports entry where:
    #     key == ticket.source and
    #     value == ticket.destination
    for ticket in tickets:
        airports[ticket.source] = ticket.destination

    # append destination where source is NONE
    # first destination
    route.append(airports["NONE"])

    # for the length of the trip
    for i in range(length - 1):
        # find the airport (value) that corresponds to the last key in
        # the route and append it to route.
        airport = airports[route[-1]]
        route.append(airport)

    return route


if __name__ == "__main__":

    ticket_11 = Ticket("NONE", "PDX")
    ticket_20 = Ticket("PDX", "DCA")
    ticket_30 = Ticket("DCA", "NONE")

    tickets_short = [ticket_11, ticket_20, ticket_30]

    expected = ["PDX", "DCA", "NONE"]
    result = reconstruct_trip(tickets_short, 3)

    print(expected)
    print(result)

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

    tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
                ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

    expected = ["LAX", "SFO", "BHM", "FLG", "XNA", "SAP",
                "SLC", "PIT", "ORD", "NONE"]

    result = reconstruct_trip(tickets, 10)

    print(expected)
    print(result)
