def print_next_n_numbers(count):
    def n_numbers_from(number):
        for i in range(number, number+count):
            print(i, end=" ")
    return n_numbers_from

initial = print_next_n_numbers(4)
initial(6)