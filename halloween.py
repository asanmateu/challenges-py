def halloween(dt):
		return "Bonfire toffee" if dt.endswith('10/31') else 'toffee'

print(halloween("2013/10/31"))