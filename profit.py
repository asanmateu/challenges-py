def profit(info):
    """ Calculates the profit given a dictionary containing cost price per unit (in dollars),
        sell price per unit (in dollars), and the starting inventory"""

    return round(info['inventory'] * (info['sell_price'] - info ['cost_price']))
