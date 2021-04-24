costs = {
    'tokyo': {
        'destination': 818,
        'hotel': 192
    },
    'kuala_lumpur': {
        'destination': 245,
        'hotel': 72
    },
    'bangkok': {
        'destination': 359,
        'hotel': 88
    },
    'taipei': {
        'destination': 657,
        'hotel': 90
    }
}


def flight_cost(dest):
    if dest in costs:
        return costs[dest]['destination']
    else:
        raise Exception("Invalid transport")


def hotel_cost(dest, days):
    if dest in costs:
        return costs[dest]['hotel'] * days
    else:
        raise Exception("Invalid transport")


def transportation_cost(transport, days):
    if transport == "car":
        return 50 * days
    elif transport == "public":
        return 0.5 * days
    else:
        raise Exception("Invalid transport")


def total_cost(dest, transport, days):
    dest = dest.lower().replace(' ', '_')
    flight = flight_cost(dest)
    hotel = hotel_cost(dest, days)
    transport = transportation_cost(transport, days)

    return {
        'flight': flight,
        'hotel': hotel,
        'transport': transport,
        'total': flight + hotel + transport
    }
