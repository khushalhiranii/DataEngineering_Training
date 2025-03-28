class List_Iterator:

    def __init__(self, list_for_iteration=None):
        self.list_for_iteration = list_for_iteration
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if(self.idx < len(self.list_for_iteration)):
            self.idx += 1
            return self.list_for_iteration[self.idx-1]
        else:
            raise StopIteration

a = List_Iterator([1, 2, 3, 4, 5])        
for num in a:
    print(num)