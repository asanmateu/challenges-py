def get_budgets(lst):
    """Sum budget values in list of dictionaries"""
    return sum([key['budget'] for key in lst])

print(get_budgets([{"name": "John",  "age": 21, "budget": 23000},
                   {"name": "Steve",  "age": 32, "budget": 40000},
                   {"name": "Martin",  "age": 16, "budget": 2700}]))
