class Iterable:
    def __init__(self, collection):
        self.collection = collection

    def __iter__(self):
        return Iterator(collection)

class Iterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = 0
        self.max_index = len(collection)

    def __next__(self):
        if self.index >= self.max_index:
            raise StopIteration

        item = self.collection[self.index]
        self.index += 1
        return item

collection = (4, 5, 6)
iterable = Iterable(collection)
for item in iterable:
    print(item)
