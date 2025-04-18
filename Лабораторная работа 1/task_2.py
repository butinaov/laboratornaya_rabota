volume = 1.44
page = 100
lines = 50
symbols = 25
volume_symbol = 4

volume_baits = volume*1024**2
count_symbols = page*lines*symbols*volume_symbol
count_books = volume_baits//count_symbols
print("Количество книг, помещающихся на дискету:", int(count_books))
