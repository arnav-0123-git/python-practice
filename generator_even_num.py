def even_numbers(limit):
    for num in range(0, limit + 1,2):
        yield num

for even in even_numbers(10):
    print(even)