def profit_margin(cost_price, sales_price):
    """Calculate profit margin give the cost and sales prices returning in percentage
    _____________

    :param cost_price: float
    :param sales_price: float

    _____________

    :return: string
    """
    return str(round((float(sales_price - cost_price) / sales_price) * 100, 1)) + '%'


print(profit_margin(28, 39))
